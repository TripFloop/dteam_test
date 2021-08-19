from django.urls import path

from shortener import views

urlpatterns = [
    path('shorten_url/', views.ShortenLinksCreateView.as_view(), name="create_link"),
    path('shortened_urls_count/', views.ShortenLinksCountView.as_view(), name="count_links"),
    path('most_shortened_urls_list/', views.ShortenLinksListView.as_view(), name="list_links")
]