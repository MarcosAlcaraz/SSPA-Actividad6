# Archivo manager.py
from particula import Particula


class Manager:

    def __init__(self):
        self.__particulas = []

    def agregarInicio(self, particula: Particula):
        self.__particulas.insert(0, particula)

    def agregarFinal(self, particula: Particula):
        self.__particulas.append(particula)

    def imprimir(self):
        for particula in self.__particulas:
            print(particula)
            
    def __str__(self):
        return "".join(
            str(particula) for particula in self.__particulas
        )
            
# particula0 = Particula(87, 10, 12, 50, 60, 80, 255, 45, 30)
# particula1 = Particula(78, 1, 21, 5, 6, 8, 0, 54, 3)

# manager = Manager()
# manager.agregarInicio(particula1)
# manager.agregarFinal(particula0)
# manager.imprimir()