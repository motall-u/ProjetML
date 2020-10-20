from django.urls import path, include
from .views import image_upload_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', image_upload_view, name= 'image_upload_view'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)