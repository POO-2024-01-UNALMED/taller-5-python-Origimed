from zooAnimales import animal

class Mamifero(animal):
    caballos = 0
    leones = 0
    total = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self.pelaje = pelaje
        self.patas = patas
        Mamifero.total += 1

    @staticmethod
    def cantidadMamiferos():
        return Mamifero.caballos + Mamifero.leones + Mamifero.total

    @staticmethod
    def crearCaballo(nombre, edad, genero):
        caballo = Mamifero()
        caballo.pelaje = True
        caballo.patas = 4
        caballo.habitat = "pradera"
        caballo.nombre = nombre
        caballo.edad = edad
        caballo.genero = genero
        caballo.caballos += 1
        return caballo

    @staticmethod
    def crearLeon(nombre, edad, genero):
        leon = Mamifero()
        leon.pelaje = True
        leon.patas = 4
        leon.habitat = "selva"
        leon.nombre = nombre
        leon.edad = edad
        leon.genero = genero
        leon.leones += 1
        return leon
