from django.contrib import admin

from django.contrib import admin
from .models import Categorias, Area

class CategoriasAdmin(admin.ModelAdmin):
    list_display= ('nombre',)
    #readonly_fields= ('created', 'update')

class AreaAdmin(admin.ModelAdmin):
    list_display= ('titulo', 'contenido', 'autor', 'imagen')
    #readonly_fields= ('created', 'update')

admin.site.register(Categorias, CategoriasAdmin)

admin.site.register(Area, AreaAdmin)