from django.shortcuts import render, HttpResponse

from .form import ProductSearchForm
# Create your views here.

def index(request):
    return HttpResponse("Hello Word")

def search(request):
    if request.method == 'POST':
        form = ProductSearchForm(request.POST)
        if form.is_valid():
            # Aquí implementa la lógica para buscar en Google Shopping
            # y filtrar los resultados de La Casa del Electrodoméstico
            # Guarda los resultados en la base de datos y muestra al usuario
            # la URL de Google Shopping y el ID de La Casa del Electrodoméstico.
            # Retorna el resultado renderizado.
            pass
    else:
        form = ProductSearchForm()
    return render(request, 'search.html', {'form': form})