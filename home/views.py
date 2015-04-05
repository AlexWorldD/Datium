from django.shortcuts import render
from django.http.response import  HttpResponse


# Create your views here.


def home(request):
    view = "Hi, Datium!"
    html = "<html><body>%s</body></html>" % view
    return HttpResponse(html)