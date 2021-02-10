from django.http import HttpResponse


def get_value():
    return 123


def homePageView(request):
    value = get_value()
    return HttpResponse(f"Hello, {value}!")
