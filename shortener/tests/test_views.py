from rest_framework.test import APIClient, APITestCase
from django.test import Client
from django.contrib.sites.models import Site
from django.apps import apps
from django.urls import reverse


class ShortenLinkCreateAndRedirectTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.usual_client = Client()
        self.test_data = {"url": "https://google.com"}
        self.wrong_data = {"url": "this_is_not_url"}
        site_obj = Site.objects.all().first()
        site_obj.domain = "test_domain.com"
        site_obj.name = "test_domain.com"
        site_obj.save()

    def test_create_link(self):
        response = self.client.post(reverse("shortener:create_link"), data=self.test_data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            self.client.get(
                reverse("redirect-link",
                        args=(response.data["shortened_url"][response.data["shortened_url"].rfind("/") + 1:],)
                        )
            ).headers["location"], "https://google.com"
        )

    def test_create_not_valid_link(self):
        response = self.client.post(reverse("shortener:create_link"), data=self.wrong_data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_create_existing_link(self):
        response = self.client.post(reverse("shortener:create_link"), data=self.test_data, format="json")
        self.assertEqual(response.status_code, 201)
        first_shortened_link = response.data["shortened_url"]
        self.assertEqual(
            self.client.get(
                reverse("redirect-link",
                        args=(response.data["shortened_url"][response.data["shortened_url"].rfind("/") + 1:],)
                        )
            ).headers["location"], "https://google.com"
        )
        response = self.client.post(reverse("shortener:create_link"), data=self.test_data, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["shortened_url"], first_shortened_link)

    def test_redirect_non_exist(self):
        response = self.usual_client.get(reverse("redirect-link", args=("non_exist",)))
        self.assertEqual(response.status_code, 404)


class ShortenLinkListTestCase(APITestCase):

    def setUp(self):
        ShortenLink = apps.get_model(app_label="shortener", model_name="ShortenLink")
        self.client = APIClient()
        for index in range(20):
            ShortenLink.objects.create(
                url=f"https://test_domain.com/{index}",
                owner_ip=f"127.0.{index}.1",
                shorten_try=index
            )
        site_obj = Site.objects.all().first()
        site_obj.domain = "test_domain.com"
        site_obj.name = "test_domain.com"
        site_obj.save()

    def test_links_list(self):
        response = self.client.get(reverse("shortener:list_links"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 10)


class ShortenLinkCountTestCase(APITestCase):

    def setUp(self):
        ShortenLink = apps.get_model(app_label="shortener", model_name="ShortenLink")
        self.client = APIClient()
        for index in range(3):
            ShortenLink.objects.create(
                url=f"https://test_domain.com/{index}",
                owner_ip=f"127.0.1.1",
                shorten_try=index
            )
        site_obj = Site.objects.all().first()
        site_obj.domain = "test_domain.com"
        site_obj.name = "test_domain.com"
        site_obj.save()

    def test_links_count(self):
        response = self.client.get(reverse("shortener:count_links"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["numbers of shortened urls"], 1)
