# from https://simpleisbetterthancomplex.com/article/2017/08/07/a-minimal-django-application.html
#
from django.conf.urls import url
from django.http import HttpResponse

DATABASES = {}
DEBUG = True
SECRET_KEY = "e5443ba7add3095e83ac6aee14f627345"
ROOT_URLCONF = __name__
TEST_RUNNER = "testing.DatabaselessTestRunner"


def home(request):
    return HttpResponse("Welcome to 855!")


urlpatterns = [
    url(r"^$", home),
]