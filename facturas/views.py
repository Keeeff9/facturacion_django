from django.shortcuts import render, get_object_or_404, redirect
from .models import Factura
from .forms import FacturaForm, LineaFacturaFormSet

def lista_facturas(request):
    facturas = Factura.objects.select_related('cliente').all().order_by('-fecha')
    return render(request, 'facturas/lista.html', {'facturas': facturas})

def factura_detalle(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    return render(request, 'facturas/detalle.html', {'factura': factura})

def nueva_factura(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        formset = LineaFacturaFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            factura = form.save()
            lineas = formset.save(commit=False)
            for linea in lineas:
                linea.factura = factura
                linea.save()
            
            return redirect(factura.get_absolute_url())
    else:
        form = FacturaForm()
        formset = LineaFacturaFormSet()
    return render(request, 'facturas/nueva.html', {'form': form, 'formset': formset})
