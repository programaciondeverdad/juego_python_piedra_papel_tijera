from django.shortcuts import render
from .models import *
# from .models import Jugador
# from .models import Application


# Create your views here.
def index(request):
	return render(request, 'app/index.html', {})

def jugar(request):
	application = Application()
	elementoJ1 = request.POST.get('elementoJ1')

	jugador1 = Jugador(elementoJ1)
	result = application.jugar(jugador1)
	return render(request, 'app/index.html', {
		'result': result, 
		'jugador1Elemento': elementoJ1, 
		'jugador2Elemento': application.jugador2.elemento.getNombre()
		})