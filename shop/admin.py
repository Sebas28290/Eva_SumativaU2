from django.contrib import admin
from shop.models import Cliente, Atención

# Register your models here.


@admin.register(Cliente)

class AdminCliente (admin.ModelAdmin):
    list_display=['id', 'nombre', 'rut', 'correo', 'FormatoSaldo','atendido']
    list_filter=['nombre']
    search_fields=['nombre','atendido']

    def FormatoSaldo (self, obj):
        return f"${obj.saldo:,}".replace(',','.')
    
@admin.register(Atención)

class AdminAtención (admin.ModelAdmin):
    list_display=['id', 'dueño', 'mascota', 'descripcion', 'FormatoPrecio','fecha']
    list_filter=['fecha',]
    search_fields=['mascota',]

    def FormatoPrecio (self, obj):
        return f"${obj.precio:,}".replace(',','.')