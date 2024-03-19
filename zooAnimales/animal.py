from zooAnimales import *
from zooAnimales import anfibio
from zooAnimales import ave
from zooAnimales import Mamifero
from zooAnimales import reptil
from zooAnimales import pez
class Animal:
    total_animales = 0

    def __init__(self, nombre, edad, habitat, genero):
        Animal.total_animales += 1
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero

    @staticmethod
    def total_por_tipo():
        return "Mamiferos: {}\nAves: {}\nReptiles: {}\nPeces: {}\nAnfibios: {}".format(
            Mamifero.cantidad_mamiferos(),
            ave.cantidad_aves(),
            reptil.cantidad_reptiles(),
            pez.cantidad_peces(),
            anfibio.cantidad_anfibios()
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
    def get_total_animales():
        return Animal.total_animales

    @staticmethod
    def set_total_animales(total_animales):
        Animal.total_animales = total_animales

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        self.edad = edad

    def get_habitat(self):
        return self.habitat

    def set_habitat(self, habitat):
        self.habitat = habitat

    def get_genero(self):
        return self.genero

    def set_genero(self, genero):
        self.genero = genero
