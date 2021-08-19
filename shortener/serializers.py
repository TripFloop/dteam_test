from rest_framework.serializers import ModelSerializer

from dteam_test.utils import generate_endpoint
from .models import ShortenLink


class ShortenLinkSerializer(ModelSerializer):
    class Meta:
        model = ShortenLink
        fields = ["link", ]


class ShortenLinkCreateSerializer(ShortenLinkSerializer):

    def create(self, validated_data):
        shorten_link_obj = ShortenLink.objects.create(
            owner_ip=validated_data.get("owner_ip"),
            url=validated_data.get("url"),
            shorten_slug=generate_endpoint()
        )
        return shorten_link_obj
