from zooAnimales import animal

class Ave(animal):
    total = 0
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, color_plumas):
        super().__init__(nombre, edad, habitat, genero)
        self.color_plumas = color_plumas
        Ave.total += 1

    def __init__(self):
        Ave.total += 1

    @staticmethod
    def cantidad_aves():
        return Ave.aguilas + Ave.halcones + Ave.total

    @staticmethod
    def crear_halcon(nombre, edad, genero):
        halcon = Ave()
        halcon.color_plumas = "café glorioso"
        halcon.habitat = "montañas"
        halcon.nombre = nombre
        halcon.edad = edad
        halcon.genero = genero
        halcon.halcones += 1
        return halcon

    @staticmethod
    def crear_aguila(nombre, edad, genero):
        aguila = Ave()
        aguila.color_plumas = "blanco y amarillo"
        aguila.habitat = "selva"
        aguila.nombre = nombre
        aguila.edad = edad
        aguila.genero = genero
        aguila.aguilas += 1
        return aguila

    def movimiento(self):
        return "volar"
