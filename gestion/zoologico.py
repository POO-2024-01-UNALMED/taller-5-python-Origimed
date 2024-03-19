class Zoologico:
    total = 0

    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.zonas = []

    def cantidadTotalAnimales(self):
        return Zoologico.total

    def agregarZonas(self, zona):
        self.zonas.append(zona)

    def getZona(self):
        return self.zonas

    @staticmethod
    def getTotal():
        return Zoologico.total

    @staticmethod
    def setTotal(total):
        Zoologico.total = total

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getUbicacion(self):
        return self.ubicacion

    def setUbicacion(self, ubicacion):
        self.ubicacion = ubicacion


class Zona:
    def __init__(self, nombre, zoo):
        self.nombre = nombre
        self.zoo = zoo
        self.animales = []

    def agregarAnimal(self, animal):
        self.animales.append(animal)

    def cantidadAnimales(self):
        return len(self.animales)
