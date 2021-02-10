from django.test import Client, TestCase

from myapp import views


class YourTestClass(TestCase):
    def test_happy_path(self):
        c = Client()
        resp = c.get("/")
        assert resp.content.startswith(b"Hello")


def test_value():
    value = views.get_value()
    assert 0 <= value <= 9999