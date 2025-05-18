from .base import Personaje

class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, fe, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, fe, defensa, vida)
        self.libro = libro

    def atributos(self):
        super().atributos()
        print("-Libro:", self.libro)

    def daño(self, enemigo):
        return self.get_inteligencia() * self.libro - enemigo.get_defensa()

