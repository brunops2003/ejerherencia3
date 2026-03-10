
from clases.herencia2.persona import Persona

class Autoparticular(Persona):
    def __init__(self, clave, nombre, edad, marca ,color, placa):
            super().__init__(clave, nombre, edad)

            self.marca = marca
            self.color = color
            self.placa = placa 

    def __str__(self):
        return super().__str__()+""+self.marca+" "+self.color+" "+self.placa 

    def subirseAuto(self):
        print("Subiendo al auto")

    def arrancarAuto(self):
        print("Encendiendo el auto")
        print("Arrancando el auto")

    def llegarDestino(self):
        print("Bajando el auto")