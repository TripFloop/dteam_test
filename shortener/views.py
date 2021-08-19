from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from dteam_test.utils import get_client_ip
from shortener.models import ShortenLink
from shortener.serializers import ShortenLinkSerializer


class ShortenLinkCreateView(APIView):

    def post(self, request):
        serializer = ShortenLinkSerializer(data=request.data)
        if serializer.is_valid():
            owner_ip = get_client_ip(request)
            if not ShortenLink.objects.filter(owner_ip=owner_ip):
                serializer.save(owner_ip=owner_ip)


class ShortenerListAPIView(APIView):

    def get(self, request):
        queryset = ShortenLink.objects.all().order_by("-shorten_try")[:10]
        serializer = ShortenLinkSerializer(queryset, many=True)
        return Response(serializer.data)


class ShortenLinksRedirectView(View):

    def get(self, request, *args, **kwargs):
        shorten_slug = kwargs.get("shorten_slug")
        link = ShortenLink.objects.filter(shorten_slug=shorten_slug).first()
        if link:
            return redirect(link.link)
        return Http404

class ShortenLinksShortenedView(APIView):

    def get(self):
