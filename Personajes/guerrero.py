from .base import Personaje
class Guerrero(Personaje):
#super copia los atributos de la clase superior, no hace falta usar self
    def __init__(self, nombre, fuerza, inteligencia, fe, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, fe, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2)Matadragones, daño 10, (3)Destrozatodo, daño 12, (4)Defensa (solo usar si eres un cacas), defensa 15"))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        elif opcion == 3:
            self.espada = 12
        elif opcion ==4:
            self.defensa = 15

        else:
            print("Numero de arma incorrecto")

    def atributos(self):
        super().atributos()
        print("-Espada:", self.espada)

    def daño(self, enemigo):
        return self.get_fuerza() * self.espada - enemigo.get_defensa()

    def subir_nivel(self, Nivel):
        multiplicador_por_nivel = 1.05
        fuerza = (Nivel + 3 ) * multiplicador_por_nivel
        inteligencia = (Nivel + 1) * multiplicador_por_nivel
        fe = ( Nivel + 1) * multiplicador_por_nivel
        defensa = (Nivel + 2) * multiplicador_por_nivel
        vida = (Nivel + 100) * multiplicador_por_nivel
        super().subir_nivel(fuerza, inteligencia, fe, defensa, vida)

