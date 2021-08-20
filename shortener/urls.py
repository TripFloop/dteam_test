from django.urls import path

from shortener import views

app_name = "shortener"

urlpatterns = [
    path('shorten_url/', views.ShortenLinkCreateView.as_view(), name="create_link"),
    path('shortened_urls_count/', views.ShortenLinksShortenedCountView.as_view(), name="count_links"),
    path('most_shortened_urls_list/', views.ShortenLinkListView.as_view(), name="list_links")
]