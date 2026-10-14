from django.contrib import admin
from shop.models import Cliente, Atención

# Register your models here.


@admin.register(Cliente)

class AdminCliente (admin.ModelAdmin):
    list_display=['id', 'nombre', 'rut', 'correo', 'saldo','atendido']
    list_filter=['nombre']
    search_fields=['atendido']

@admin.register(Atención)

class AdminAtención (admin.ModelAdmin):
    list_display=['id', 'dueño', 'mascota', 'descripcion', 'precio','fecha']
    list_filter=['dueño', 'mascota']
    search_fields=['fecha']
