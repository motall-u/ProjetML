from django.urls import path, include
from .views import image_upload_view, test_home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('analyse/', image_upload_view, name= 'analyse'),
    path('',test_home, name='home')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)