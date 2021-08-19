import re
from rest_framework.serializers import ModelSerializer

from .utils import generate_endpoint
from .models import ShortenLink


class ShortenLinkSerializer(ModelSerializer):
    class Meta:
        model = ShortenLink
        fields = ["url"]


class ShortenLinkCreateSerializer(ShortenLinkSerializer):

    def validate(self, data):
        if not re.search(r'[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&\=]*)',
                         data["url"]):
            raise serializers.ValidationError("Enter a valid URL")
        return data

    def create(self, validated_data):
        shorten_link_obj = ShortenLink.objects.create(
            owner_ip=validated_data.get("owner_ip"),
            url=validated_data.get("url"),
            shorten_slug=generate_endpoint()
        )
        return shorten_link_obj
