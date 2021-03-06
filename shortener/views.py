from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .utils import get_client_ip, build_full_shorten_link
from shortener.models import ShortenLink
from shortener.serializers import ShortenLinkSerializer


class ShortenLinkCreateView(APIView):

    def post(self, request):
        serializer = ShortenLinkSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            if not ShortenLink.objects.filter(url=request.data["url"]):
                shorten_link_obj = serializer.save(owner_ip=get_client_ip(request))
                status = 201
            else:
                shorten_link_obj = ShortenLink.objects.filter(url=request.data["url"]).first()
                shorten_link_obj.get_shorten_count()
                status = 200
            return Response({"shortened_url": build_full_shorten_link(shorten_link_obj.shorten_slug)}, status)
        return Response(serializer.errors, 400)


class ShortenLinkListView(APIView):

    def get(self, request):
        queryset = ShortenLink.objects.all().order_by("-shorten_try")[:10]
        serializer = ShortenLinkSerializer(queryset, many=True)
        return Response(serializer.data, 200)


class ShortenLinksRedirectView(View):

    def get(self, request, *args, **kwargs):
        shorten_slug = kwargs.get("shorten_slug")
        link = ShortenLink.objects.filter(shorten_slug=shorten_slug).first()
        if link:
            redirect_url = link.url
            if not redirect_url.startswith("http"):
                redirect_url = "https://" + redirect_url
            return redirect(redirect_url)
        raise Http404


class ShortenLinksShortenedCountView(APIView):

    def get(self, request):
        count = ShortenLink.objects.all().distinct("owner_ip").count()
        return Response({"numbers of shortened urls": count})
