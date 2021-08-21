from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

from shortener import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("shortener.urls", namespace="shortener")),
    path('<slug:shorten_slug>/', views.ShortenLinksRedirectView.as_view(), name='redirect-link')
]
