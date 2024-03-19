from zooAnimales.animal import Animal

class Anfibio(Animal):
    total = 0
    ranas = 0
    salamandras = 0

    def __init__(self, nombre="", edad=0, habitat="", genero="", color_piel="", venenoso=False):
        super().__init__(nombre, edad, habitat, genero)
        self.color_piel = color_piel
        self.venenoso = venenoso
        Anfibio.total += 1

    @staticmethod
    def cantidadAnfibios():
        return Anfibio.salamandras + Anfibio.ranas + Anfibio.total

    @staticmethod
    def crearRana(nombre, edad, genero):
        rana = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        Anfibio.ranas += 1
        return rana

    @staticmethod
    def crearSalamandra(nombre, edad, genero):
        salamandra = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        Anfibio.salamandras += 1
        return salamandra

    def movimiento(self):
        return "saltar"
