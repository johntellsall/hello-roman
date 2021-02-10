import re
from django.test import Client, TestCase

from myapp import views


class YourTestClass(TestCase):
    def test_happy_path(self):
        c = Client()
        resp = c.get("/")
        assert resp.content.startswith(b"Hello")
        assert re.search("Hello.+[0-9]+", str(resp.content))


def test_value():
    value = views.get_value()
    assert 0 <= value <= 9999