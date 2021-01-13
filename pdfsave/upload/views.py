from django.shortcuts import render
from . import savetodb as a
from django.http import HttpResponse
import datetime

# Create your views here.


def home(request):
    # a.savetodb()
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
