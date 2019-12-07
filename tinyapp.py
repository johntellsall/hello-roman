# from https://simpleisbetterthancomplex.com/article/2017/08/07/a-minimal-django-application.html
# 
from django.http import HttpResponse

DEBUG = True
SECRET_KEY = '4l0ngs3cr3tstr1ngw3lln0ts0l0ngw41tn0w1tsl0ng3n0ugh'
ROOT_URLCONF = __name__

def home(request):
    return HttpResponse('Welcome to the Tinyapp\'s Homepage!')

urlpatterns = []