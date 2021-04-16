from django.test import TestCase
from django.urls import resolve
from lists.views import home_page # (2)
from django.http import HttpRequest
from django.template.loader import render_to_string

# Create your tests here.
class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response =self.client.get("/")
        self.assertTemplateUsed(response,'home.html')

