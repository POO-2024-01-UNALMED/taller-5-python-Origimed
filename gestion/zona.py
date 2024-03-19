from gestion.zoologico import Zoologico


class Zona:
    def __init__(self, nombre, zoo=""):
        self.nombre = nombre
        self.zoo = zoo
        self.animales = []

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getZoo(self):
        return self.zoo

    def setZoo(self, zoo):
        self.zoo = zoo

    def getAnimales(self):
        return self.animales

    def setAnimales(self, animales):
        self.animales = animales

    def agregarAnimales(self, animal):
        self.animales.append(animal)
        Zoologico.total += 1

    def cantidadAnimales(self):
        return len(self.animales)
