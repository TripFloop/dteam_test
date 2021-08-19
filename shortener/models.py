from django.contrib.auth.models import User
from django.db import models, IntegrityError
from django.db.models import F

from .utils import generate_endpoint


class ShortenLink(models.Model):
    url = models.URLField()
    shorten_slug = models.SlugField(blank=True, null=True, unique=True, )
    owner_ip = models.GenericIPAddressField()
    shorten_try = models.PositiveIntegerField(blank=True, null=True, default=1)

    def __str__(self):
        return self.url

    def get_shorten(self):
        self.shorten_try = F("shorten_try") + 1
        self.save(update_fields=["shorten_try", ])

    def save(self, *args, **kwargs):
        if not self.shorten_slug:
            self.shorten_slug = generate_endpoint()

        try:
            super().save(*args, **kwargs)
        except IntegrityError:
            self.save(*args, **kwargs)
