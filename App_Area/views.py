from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from App_Area.models import Area

def area(request):

    posts=Area.objects.all() #aquí importamos todos los post creados
    return render(request, 'area/area.html', {'posts': posts})


"""def area_detail(request, area_id):
    post = get_object_or_404(Area, id=area_id)
    return render(request, 'area/area_detail.html', {'post': post})
"""