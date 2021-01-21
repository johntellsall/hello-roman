from django.test import Client, TestCase


class YourTestClass(TestCase):
    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_happy_path(self):
        c = Client()
        resp = c.get("/")
        assert resp.content.startswith(b"Hello")
