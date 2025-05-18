from .base import Personaje

class Enemigo(Personaje):
#super copia los atributos de la clase superior, no hace falta usar self
    def __init__(self, nombre, fuerza, inteligencia, fe, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, fe, defensa, vida)
        self.espada = espada

    def cambiar_arma(self, opcion):
        opcion = int(input("Dificultad\n1\n2\n"))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Numero de dificultad incorrecto")

    def atributos(self):
        super().atributos()
        print("-Espada:", self.espada)

    def daño(self, enemigo):
        return self.get_fuerza() * self.espada - enemigo.get_defensa()
