from django.contrib.auth.models import User
from django.db import models


class ShortenLink(models.Model):
    link = models.URLField()
    shorten_link = models.URLField(blank=True, null=True, unique=True, )
    owner_ip = models.CharField(blank=True,)

    def __str__(self):
        return self.link

    def save(self):
        if not self.shorten_link:
            self.shorten_link =