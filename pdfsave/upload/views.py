from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Upload, Transactions
from django.conf import settings
from pathlib import Path
from . import savetodb as a
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
import datetime
import threading
from django.shortcuts import render
# REST
from .serializers import TransactionsSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics


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

# @api_view(['GET',])
# def data(request, format=None):
#     if request.method == 'GET':
#         tranc = Transactions.objects.all()
#         serializer = TransactionsSerializer(tranc, many=True)
#         return Response(serializer.data)


class TransactionsList(generics.ListCreateAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer
