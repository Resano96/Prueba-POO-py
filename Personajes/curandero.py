from .base import Personaje
class Curandero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, fe, defensa, vida, baculo, curacion):
        super().__init__(nombre, fuerza, inteligencia, fe, defensa, vida)
        self.baculo = baculo
        self.curacion = curacion

    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Curaloto, daño 2 curacion 6. (2)Mataloto, daño 6 curacion 2"))
        if opcion ==1:
            self.baculo = 2
            self.curacion = 6
        elif opcion == 2:
            self.baculo = 6
            self.curacion = 2
        else:
            print("Opcion de arma incorrecto")
    def atributos(self):
        super().atributos()
        print("-Daño de baculo:",self.baculo)
        print("-Curacion del baculo", self.curacion)
    def daño(self, enemigo):
        return self.get_fe()*self.baculo - enemigo.get_defensa()
