from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from App1 import views


urlpatterns = [

    path('', views.home, name='home'),
    path('inicio_views/', views.inicio_view, name='inicio_views'),
    path('areas/', views.areas_practica, name='areas_practica'),
    path('contacto/', views.contacto, name='contacto'),
    path('testimonios/', views.testimonios, name='testimonios'),
    path('inmobiliaria/', views.inmobiliaria, name='inmobiliaria'),
    path('registro/', views.formulario_contacto, name='registro'),
    path('formulario_exitoso/', views.formulario_exitoso, name='exito'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
