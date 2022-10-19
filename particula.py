# Archivo particula.py
from algoritmos import distancia_euclidiana

class Particula:    
    def __init__(self, id=0, origen_x=0, origen_y=0, destino_x=0, destino_y=0, velocidad=0,red=0,green=0,blue=0):
        self.__id = id
        self.__origen_x = origen_x
        self.__origen_y = origen_y
        self.__destino_x = destino_x
        self.__destino_y = destino_y
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__distancia = distancia_euclidiana(origen_x, origen_y, destino_x, destino_y)
        
    def __str__(self):
        return ('\n\nParticula\n' + 
                '\nID       : ' + str(self.__id) +
                '\nOrigen X : ' + str(self.__origen_x) +
                '\nOrigen Y : ' + str(self.__origen_y) +
                '\nDestino X: ' + str(self.__destino_x) +
                '\nDestino Y: ' + str(self.__destino_y) +
                '\nVelocidad: ' + str(self.__velocidad) + 
                '\nRed      : ' + str(self.__blue) +
                '\nGreen    : ' + str(self.__green) +
                '\nBlue     : ' + str(self.__blue) +
                '\nDistancia: ' + str(self.__distancia)
                )