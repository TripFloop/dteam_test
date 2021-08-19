import random
import string

from django.conf import settings
from django.contrib.sites.models import Site


def generate_endpoint():
    endpoint = ''.join([
        random.choice(string.ascii_letters) for _ in range(
            settings.SHORTEN_LINK_ENDPOINT_LENGTH
        )
    ])
    return endpoint


def build_full_shorten_link(endpoint):
    domain = Site.objects.get_current().domain
    schema = 'http' if settings.DEBUG else 'https'
    return f'{schema}://{domain}/{endpoint}'


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
