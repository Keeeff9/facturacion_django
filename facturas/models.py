from django.db import models
from django.urls import reverse

class Cliente(models.Model):
    nombre = models.CharField(max_length=120)
    email = models.EmailField(blank=True)
    direccion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=120)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='facturas')
    fecha = models.DateField(auto_now_add=True)

    def total(self):
        return sum(item.subtotal() for item in self.lineas.all())

    def get_absolute_url(self):
        return reverse('factura_detalle', args=[str(self.id)])

    def __str__(self):
        return f'Factura #{self.id} - {self.cliente}'

class LineaFactura(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name='lineas')
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.producto.precio * self.cantidad

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre}'
