from django.contrib import admin
from .models import Contacto

from io import BytesIO
from django.contrib import admin
from import_export import resources 
from django.http import HttpResponse
import csv
from .models import Contacto
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer,PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.units import inch


def exportar_contactos_como_pdf(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="contactos.pdf"'
    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    stylesN = styles['Normal']
    justified_style = ParagraphStyle(
        name='Justified',
        parent=styles['Normal'],
        aligment=TA_JUSTIFY,
        spaceAfter=12
    )

    for obj in queryset:
        elements.append(Paragraph(f"<b>Nombre:</b> {obj.nombre}", stylesN))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(f"<b>Email:</b> {obj.email}", stylesN))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(f"<b>Teléfono:</b> {obj.telefono}", stylesN))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(f"<b>Mensaje:</b> {obj.mensaje}", stylesN))
        elements.append(Spacer(1, 12))
        
        mensaje = Paragraph(obj.mensaje.replace("\n", "<br />"), justified_style)
        elements.append(mensaje)
        elements.append(Spacer(1, 12))     
        
        elements.append(Paragraph(f"<b>Fechar Creación:</b> {obj.fecha_creacion}", stylesN))
        elements.append(Spacer(1, 24))

        elements.append(PageBreak())

    doc.build(elements)
    return response

exportar_contactos_como_pdf.short_description = "Exportar seleccionados como PDF"

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'mensaje', 'fecha_creacion')
    search_fields = ('nombre',)
    list_filter = ('nombre',) 
    list_per_page = 4
    actions=[exportar_contactos_como_pdf]
    
admin.site.register(Contacto, ContactoAdmin)


    

# Register your models here.
# Cambiar el título de la interfaz de administración
admin.site.site_title = "Aplicación Web"
admin.site.site_header = "Registro y control de entradas"
admin.site.index_title = "Modulos"