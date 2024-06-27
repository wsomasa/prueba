from django.contrib import admin
from .models import Areas

class AreaAdmin(admin.ModelAdmin):
    list_display= ('especialidad', 'contenido', 'imagen')
     

admin.site.register(Areas, AreaAdmin)