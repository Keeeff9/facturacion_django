from facturas.models import Cliente, Producto, Factura, LineaFactura
from random import choice, randint
from decimal import Decimal

# --- Limpiar datos previos ---
LineaFactura.objects.all().delete()
Factura.objects.all().delete()
Producto.objects.all().delete()
Cliente.objects.all().delete()

# --- Crear clientes ---
clientes_data = [
    ("Luca Rossi", "luca.rossi@example.com", "Via Roma 12, Milano"),
    ("Giulia Bianchi", "giulia.bianchi@example.com", "Corso Italia 45, Firenze"),
    ("Marco Esposito", "marco.esposito@example.com", "Via Napoli 8, Napoli"),
    ("Sara Moretti", "sara.moretti@example.com", "Piazza San Marco, Venezia"),
    ("Alessandro Conti", "alessandro.conti@example.com", "Via Torino 23, Torino"),
    ("Francesca Ricci", "francesca.ricci@example.com", "Via della Pace 77, Bologna"),
    ("Andrea Romano", "andrea.romano@example.com", "Viale Europa 11, Roma"),
    ("Chiara Ferri", "chiara.ferri@example.com", "Piazza Garibaldi, Genova"),
]

clientes = [
    Cliente.objects.create(nombre=nombre, email=email, direccion=dir)
    for nombre, email, dir in clientes_data
]

# --- Crear productos (platos italianos) ---
productos_data = [
    ("Pizza Margherita", Decimal("24.00")),
    ("Pizza Quattro Formaggi", Decimal("28.00")),
    ("Spaghetti alla Carbonara", Decimal("22.00")),
    ("Lasagna alla Bolognese", Decimal("26.00")),
    ("Risotto ai Funghi", Decimal("25.50")),
    ("Gnocchi al Pesto", Decimal("23.50")),
    ("Tiramisu", Decimal("15.00")),
    ("Panna Cotta", Decimal("14.00")),
    ("Bruschetta al Pomodoro", Decimal("12.00")),
    ("Vino Rosso della Casa", Decimal("30.00")),
    ("Acqua Frizzante", Decimal("8.00")),
    ("Caffè Espresso", Decimal("6.00")),
]

productos = [
    Producto.objects.create(nombre=nombre, precio=precio)
    for nombre, precio in productos_data
]

# --- Crear facturas ---
for i in range(1, 25):  # Crea 24 facturas de ejemplo
    cliente = choice(clientes)
    factura = Factura.objects.create(cliente=cliente)

    # Cada factura tiene entre 2 y 6 platos distintos
    platos_en_factura = choice(range(2, 7))
    seleccion = [choice(productos) for _ in range(platos_en_factura)]

    for producto in seleccion:
        cantidad = randint(1, 3)
        LineaFactura.objects.create(
            factura=factura,
            producto=producto,
            cantidad=cantidad
        )

print("✅ Se crearon datos de ejemplo para el restaurante italiano con éxito.")
print(f"Clientes: {Cliente.objects.count()}")
print(f"Productos: {Producto.objects.count()}")
print(f"Facturas: {Factura.objects.count()}")
print(f"Líneas de factura: {LineaFactura.objects.count()}")
