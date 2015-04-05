from django.shortcuts import render
from django.http.response import  HttpResponse


# Create your views here.


def home(request):
    view = "home"
    html = "<html><body>This is %s view</body></html>" % view
    return HttpResponse(html)