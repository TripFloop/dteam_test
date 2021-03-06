import re
from rest_framework.serializers import ModelSerializer
from django.core.exceptions import ValidationError

from .utils import generate_endpoint
from .models import ShortenLink


class ShortenLinkSerializer(ModelSerializer):

    class Meta:
        model = ShortenLink
        fields = ["url"]

    def validate(self, data):
        if not re.search(r'^(https?:\/\/)?([\w\.]+)\.([a-z]{2,6}\.?)(\/[\w\.]*)*\/?$',
                         data["url"]):
            raise ValidationError("Enter a valid URL")
        return data

    def create(self, validated_data):
        shorten_link_obj = ShortenLink.objects.create(
            owner_ip=validated_data.get("owner_ip"),
            url=validated_data.get("url"),
            shorten_slug=generate_endpoint()
        )
        return shorten_link_obj


