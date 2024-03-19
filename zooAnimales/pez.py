from zooAnimales.animal import Animal


class Pez(Animal):
    salmones = 0
    bacalaos = 0
    total = 0

    def __init__(self, nombre="", edad=0, habitat="", genero="", colorEscamas="", cantidadAletas=0):
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.cantidadAletas = cantidadAletas
        Pez.total += 1

    @staticmethod
    def cantidadPeces():
        return Pez.bacalaos + Pez.salmones + Pez.total

    @staticmethod
    def crearSalmon(nombre, edad, genero):
        salmon = Pez()
        salmon.colorEscamas = "rojo"
        salmon.cantidadAletas = 6
        salmon.habitat = "oceano"
        salmon.nombre = nombre
        salmon.edad = edad
        salmon.genero = genero
        salmon.salmones += 1
        return salmon

    @staticmethod
    def crearBacalao(nombre, edad, genero):
        bacalao = Pez()
        bacalao.colorEscamas = "gris"
        bacalao.cantidadAletas = 6
        bacalao.habitat = "oceano"
        bacalao.nombre = nombre
        bacalao.edad = edad
        bacalao.genero = genero
        bacalao.bacalaos += 1
        return bacalao

    def movimiento(self):
        return "nadar"
