from django.contrib import admin
from .models import ShortenLink


# Register your models here.

class ShortenLinkAdmin(admin.ModelAdmin):
    model = ShortenLink
    fields = ["url", "owner_ip", "shorten_slug"]


admin.site.register(ShortenLink, ShortenLinkAdmin)
