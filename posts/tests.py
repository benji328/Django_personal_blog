from django.test import TestCase
from django.urls import reverse


class PostPageTests(TestCase):
    def test_projects_page_loads(self):
        response = self.client.get(reverse("projects"))
        self.assertEqual(response.status_code, 200)

    def test_covid_visualization_page_loads(self):
        response = self.client.get(reverse("covid19_map"))
        self.assertEqual(response.status_code, 200)

    def test_data_storage_page_loads(self):
        response = self.client.get(reverse("data_storage"))
        self.assertEqual(response.status_code, 200)
