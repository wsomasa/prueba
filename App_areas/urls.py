from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from App_areas import views


 
urlpatterns = [

    path('areas/', views.areas_view, name='areas'),
     
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    