from zooAnimales import animal

class Anfibio(animal):
    total = 0
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, color_piel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self.color_piel = color_piel
        self.venenoso = venenoso
        Anfibio.total += 1

    @staticmethod
    def cantidad_anfibios():
        return Anfibio.salamandras + Anfibio.ranas + Anfibio.total

    @staticmethod
    def crear_rana(nombre, edad, genero):
        rana = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        Anfibio.ranas += 1
        return rana

    @staticmethod
    def crear_salamandra(nombre, edad, genero):
        salamandra = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        Anfibio.salamandras += 1
        return salamandra

    def movimiento(self):
        return "saltar"
