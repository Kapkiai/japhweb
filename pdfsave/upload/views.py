from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Upload
from django.conf import settings
from pathlib import Path
from . import savetodb as a
from django.http import HttpResponse
import datetime
import threading
from django.shortcuts import render


filepath = settings.MEDIA_ROOT
class UploadView(CreateView):

    model = Upload
    fields = ['upload_file', ]
    success_url = reverse_lazy('fileupload')
    # context_object_name = 'dbobj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Upload.objects.all()
        return context
    print("Hello", Path(filepath + '/data.docx').exists())
    # Upload.objects.all().delete()


def upload(request):
    print("Inside Upload")
    t = threading.Thread(target=updatedb, args=(), daemon=True)
    t.start()

    # now = datetime.datetime.now()
    # html = "<html><body>Upload Successfulat %s.</body></html>" % now
    # return HttpResponse(html)
    return render(request, 'home.html')


def updatedb():
    if Path(filepath + '/data.docx').exists():
        try:
            a.savetodb()
            Upload.objects.all().delete()
        except Exception as t:
            print("Error", t)
