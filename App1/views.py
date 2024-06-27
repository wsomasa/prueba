from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistroForm, ContactoForm
from django.core.mail import send_mail
from django.conf import settings
#vista principal

def home(request):
    return render(request, 'home.html')


def inicio_view(request):
 
    return render(request, 'inicio.html')


    
def mainView(request):
    return render(request, 'index.html')

def bootstrapView(request):
    return render(request, 'indexbootstrap.html')

def contacto(request):
    
    return render(request, 'contacto.html')

def areas_practica(request):
    
    return render(request, 'areas_practica.html')

def testimonios(request):
    return render(request, 'testimonios.html')

def inmobiliaria(request):
    
    return render(request, 'inmobiliaria.html')

#formulario registro

def registro(request):
    if request.method =='POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            mensaje = form.cleaned_data['mensaje']
            
        return render(request, 'exito.html')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})


#formulario contacto

def formulario_contacto(request):
    if request.method =='POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            mensaje = form.cleaned_data['mensaje']

            # Envia el correo electrónico
            asunto = 'Nuevo mensaje de contacto web'
            mensaje_email = f'Nombre: {nombre}\nEmail: {email}\nTeléfono: {telefono}\nMensaje: {mensaje}'
            remitente = settings.EMAIL_HOST_USER
            destinatarios = ['wsomas@gmail.com', 'Emmacori22@gmail.com', 'emmacorinabustosardila@gmail.com']  # Puedes añadir más destinatarios si es necesario

            send_mail(asunto, mensaje_email, remitente, destinatarios)
            
            
            
            
            return render(request, 'formulario_exitoso.html')
    else:
        form = ContactoForm()
    return render(request, 'formulario_contacto.html', {'form': form})    

def formulario_exitoso():
    return render('formulario_exitoso')    
    

