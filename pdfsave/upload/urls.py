from django.conf import settings
from django.conf.urls.static import static
from upload import views as uploader_views
from django.urls import path
#REST
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('upload', uploader_views.upload, name='upload'),
    path('', uploader_views.UploadView.as_view(), name='fileupload'),
    path('data', uploader_views.TransactionsList.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)

# print(settings.MEDIA_URL, settings.MEDIA_ROOT)
