from django.contrib import admin
from .models import Cliente, Producto, Factura, LineaFactura

class LineaInline(admin.TabularInline):
    model = LineaFactura
    extra = 1

class FacturaAdmin(admin.ModelAdmin):
    inlines = [LineaInline]
    list_display = ('id','cliente','fecha','total')

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Factura, FacturaAdmin)

# Register your models here.
