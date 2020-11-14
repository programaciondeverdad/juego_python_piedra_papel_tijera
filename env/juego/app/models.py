from django.db import models
from app.modelos import *
import random

# Create your models here.
class Application(object):
    array_elementos = []

    def __init__(self):
        self.array_elementos = [
            Piedra(),
            Papel(),
            Tijera()
        ]

    def jugar(self, jugador1):
        self.jugador1 = jugador1

        self.jugador2 = JugadorNPC()
        self.jugador2.elegirElemento(self.array_elementos)

        return self.jugador1.elemento.jugarContra(self.jugador2.elemento)
        

class Jugador(object):
    def __init__(self, elementoJugador):
        print(elementoJugador)
        if(elementoJugador == 'Piedra'):
            elemento = Piedra()
            print('Piedra')
        elif(elementoJugador == 'Papel'):
            elemento = Papel()
            print('Papel')
        else:
            elemento = Tijera()
            print('Tijera')

        self.elemento = elemento
        
class JugadorNPC(object):
    def elegirElemento(self, array_elementos = []):
        self.elemento = random.choice(array_elementos)

# Polimorfismo
# Herencia
class Elemento(object):
    def getNombre(self):
        return ''

    def jugarContra(self, elemento):
        return false


class Piedra(Elemento):
    def getNombre(self):
        return 'Piedra'

    def jugarContra(self, elemento):
        return elemento.getNombre() == 'Tijera' # Solo le gana a tijera
        # Simplificado de:
        # if(elemento.getNombre() == 'Tijera')
        #    return true
        # else
        #    return false

    # def __str__(self):
    #     return 'Piedra'


class Papel(Elemento):
    def getNombre(self):
        return 'Papel'
        
    def jugarContra(self, elemento):
        return elemento.getNombre() == 'Piedra' # Solo le gana a piedra

class Tijera(Elemento):
    def getNombre(self):
        return 'Tijera'
        
    def jugarContra(self, elemento):
        return elemento.getNombre() == 'Papel' # Solo le gana a papel