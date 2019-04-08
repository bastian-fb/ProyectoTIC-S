from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,'nombre_app/index.html')
def tiendas(request):
	return render(request,'nombre_app/tiendas.html')
def recetas(request):
	return render(request,'nombre_app/recetas.html')
def eventos(request):
	return render(request,'nombre_app/eventos.html')
def comunidad(request):
	return render(request,'nombre_app/comunidad.html')


