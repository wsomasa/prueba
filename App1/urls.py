from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from App1 import views
#from App_blog import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('inicio_views/', views.inicio_view, name='inicio_views'),
    #path('bootstrap/', views.bootstrapView), 
    path('areas/', views.areas_practica, name='areas_practica'),
    path('contacto/', views.contacto, name='contacto'),
    path('testimonios/', views.testimonios, name='testimonios'),
    path('inmobiliaria/', views.inmobiliaria, name='inmobiliaria'),
    path('registro/', views.formulario_contacto, name='registro'),
    path('formulario_exitoso/', views.formulario_exitoso, name='exito'),
    #path('inicio/', views.iniciomain, name='inicio'), 
    #path('blog/', include('App_blog.urls')),
    
    
    #path('inicio_views/', views.inicio_view, name='inicio_views'), 
    #path('App_clc', views.login_view, name='login'),
    #path('inicio/', views.inicio_view, name='inicio'),  # Ruta para la página de inicio de tu aplicación
    #path('pacientes/', views.lista_pacientes, name='lista_pacientes'), 
    #path('consultas/', views.lista_consultas, name='lista_pacientes'),
    #path('cirugias/', views.lista_cirugias, name='lista_cirugias'),
    #path('index/', views.index, name= 'index'),
    #path('servicios/', views.servicios, name='servicios'),
    #path('directorio/', views.directorio, name='directorio'),
    #path('contacto/', views.contact_view, name='contacto'),

]
 # a continuacion creamos la url para descargar los archivos
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
