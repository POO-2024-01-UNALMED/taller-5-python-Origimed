from zooAnimales.animal import Animal


class Reptil(Animal):
    iguanas = 0
    serpientes = 0
    total = 0

    def __init__(self, nombre="", edad=0, habitat="", genero="", colorEscamas="", largoCola=0):
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.largoCola = largoCola
        Reptil.total += 1

    @staticmethod
    def cantidadReptiles():
        return Reptil.iguanas + Reptil.serpientes + Reptil.total

    @staticmethod
    def crearIguana(nombre, edad, genero):
        iguana = Reptil()
        iguana.colorEscamas = "verde"
        iguana.largoCola = 3
        iguana.habitat = "humedal"
        iguana.nombre = nombre
        iguana.edad = edad
        iguana.genero = genero
        iguana.iguanas += 1
        return iguana

    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        serpiente = Reptil()
        serpiente.colorEscamas = "blanco"
        serpiente.largoCola = 1
        serpiente.habitat = "jungla"
        serpiente.nombre = nombre
        serpiente.edad = edad
        serpiente.genero = genero
        serpiente.serpientes += 1
        return serpiente

    def movimiento(self):
        return "reptar"
