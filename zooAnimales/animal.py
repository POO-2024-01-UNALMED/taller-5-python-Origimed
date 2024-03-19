


class Animal:
    total_animales = 0

    def __init__(self, nombre, edad, habitat, genero):
        Animal.total_animales += 1
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero

    @staticmethod
    def totalPorTipo():
        from zooAnimales.Mamifero import Mamifero
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.ave import Ave
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil
        return "Mamiferos: {}\nAves: {}\nReptiles: {}\nPeces: {}\nAnfibios: {}".format(
            Mamifero.cantidad_mamiferos(),
            Ave.cantidad_aves(),
            Reptil.cantidad_reptiles(),
            Pez.cantidad_peces(),
            Anfibio.cantidad_anfibios()
        )

    comp = "Mamiferos: 4\n" + \
           "Aves: 4\n" + \
           "Reptiles: 2\n" + \
           "Peces: 2\n" + \
           "Anfibios: 3"

    def __str__(self):
        return "Mi nombre es {}, tengo una edad de {}, habito en {} y mi genero es {}".format(
            self.nombre, self.edad, self.habitat, self.genero)

    def movimiento(self):
        return "desplazarse"

    @staticmethod
    def getTotalAnimales():
        return Animal.total_animales

    @staticmethod
    def setTotalAnimales(total_animales):
        Animal.total_animales = total_animales

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getEdad(self):
        return self.edad

    def setEdad(self, edad):
        self.edad = edad

    def getHabitat(self):
        return self.habitat

    def setHabitat(self, habitat):
        self.habitat = habitat

    def getGenero(self):
        return self.genero

    def setGenero(self, genero):
        self.genero = genero
