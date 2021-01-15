from django.conf import settings
from django.conf.urls.static import static
from upload import views as uploader_views
from django.urls import path

urlpatterns = [
    path('upload', uploader_views.upload, name='upload'),
    path('', uploader_views.UploadView.as_view(), name='fileupload'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# print(settings.MEDIA_URL, settings.MEDIA_ROOT)
