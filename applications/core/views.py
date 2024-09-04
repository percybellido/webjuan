from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def productos(request):
    return render(request, 'core/productos.html')

def clientes(request):
    return render(request, 'core/clientes.html')

def ventas(request):
    return render(request, 'core/ventas.html')

def blog(request):
    return render(request, 'core/blog.html')

def contacto(request):
    return render(request, 'core/contacto.html')
