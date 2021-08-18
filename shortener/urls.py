from django.urls import path

from shortener import views

urlpatterns = [
    path('shorten_url/', views.ShortenLinksCreateView.as_view(), name="create_link"),
    path('{}',),
    path('most')
]