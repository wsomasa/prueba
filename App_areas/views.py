from django.shortcuts import render
from .models import Areas

def areas_view(request):
    
    areas = Areas.objects.all() 
    return render(request, 'areas_practica.html', {'areas': areas})
