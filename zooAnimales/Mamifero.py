from zooAnimales.animal import Animal


class Mamifero(Animal):
    caballos = 0
    leones = 0
    total = 0

    def __init__(self, nombre="", edad=0, habitat="", genero="", pelaje="", patas=0):
        super().__init__(nombre, edad, habitat, genero)
        self.pelaje = pelaje
        self.patas = patas
        Mamifero.total += 1

    def __init__(self):
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
    

    

"""""
from gestion.zona import Zona
from gestion.zoologico import Zoologico 
from zooAnimales.anfibio import Anfibio
from zooAnimales.ave import Ave
from zooAnimales.Mamifero import Mamifero
from zooAnimales.pez import Pez
from zooAnimales.reptil import Reptil
zoo = Zoologico("Zoologico Central", "Chicago")
z1 = Zona("zona1")
z2 = Zona("zona2")
zoo.agregarZonas(z1)
zoo.agregarZonas(z2)
z1.agregarAnimales(Mamifero.crearCaballo("test", 11, "M"))
z1.agregarAnimales(Mamifero.crearCaballo("test", 11, "M"))
z1.agregarAnimales(Mamifero.crearLeon("test", 11, "M"))
z1.agregarAnimales(Ave.crearHalcon("test", 11, "M"))
z1.agregarAnimales(Ave.crearHalcon("test", 11, "M"))
z1.agregarAnimales(Ave.crearAguila("test", 11, "M"))
z1.agregarAnimales(Ave.crearAguila("test", 11, "M"))
z1.agregarAnimales(Anfibio.crearRana("test", 11, "M"))
z2.agregarAnimales(Anfibio.crearSalamandra("test", 11, "M"))
z2.agregarAnimales(Reptil.crearIguana("test", 11, "M"))
z2.agregarAnimales(Reptil.crearSerpiente("test", 11, "M"))
z2.agregarAnimales(Pez.crearSalmon("test", 11, "M"))
z2.agregarAnimales(Pez.crearBacalao("test", 11, "M"))
Mamifero.crearCaballo("test", 11, "M")
Ave.crearHalcon("test", 11, "M")
Anfibio.crearRana("test", 11, "M")
Reptil.crearIguana("test", 11, "M")
Pez.crearBacalao("test", 11, "M")

print(Mamifero.caballos)"""