from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from App_Area import views

 
urlpatterns = [

    path('', views.area, name='area'),
    #path('post/<int:post_id>/', views.area_detail, name='area_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    