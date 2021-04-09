from django.test import TestCase
from django.urls import resolve
from lists.views import home_page # (2)
from django.http import HttpRequest

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolve_to_home_page_view(self):
        found = resolve("/") #(1)
        self.assertEqual(found.func,home_page) #(1)

    def test_home_page_returns_correct_html(self):
        request=HttpRequest()
        response =home_page(request)
        html =response.content.decode("utf-8")
        self.assertTrue(html.startswith("<html>"))
        self.assertIn("<title>To-Do lists</title>",html)
        self.assertTrue(html.endswith("</html>"))

