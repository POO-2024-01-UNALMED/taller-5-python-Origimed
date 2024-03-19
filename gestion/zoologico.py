class Zoologico:
    total = 0

    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.zonas = []

    def cantidad_total_animales(self):
        return Zoologico.total

    def agregar_zona(self, zona):
        self.zonas.append(zona)

    def obtener_zonas(self):
        return self.zonas

    @staticmethod
    def obtener_total():
        return Zoologico.total

    @staticmethod
    def establecer_total(total):
        Zoologico.total = total

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_ubicacion(self):
        return self.ubicacion

    def establecer_ubicacion(self, ubicacion):
        self.ubicacion = ubicacion


class Zona:
    def __init__(self, nombre, zoo):
        self.nombre = nombre
        self.zoo = zoo
        self.animales = []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def cantidad_animales(self):
        return len(self.animales)
