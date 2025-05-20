from .base import Personaje

class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, fe, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, fe, defensa, vida)
        self.libro = libro

    def cambiar_arma(self):
        opcion = int(input("Elige un arma: \n(1) Matabichillos, daño 3 \n(2)Matabichillosgrandes, daño 5"))
        if opcion == 1:
            self.libro = 6
        elif opcion == 2:
            self.libro = 10
        else:
            print("Opcion de arma incorrecto")

    def atributos(self):
        super().atributos()
        print("-Libro:", self.libro)

    def daño(self, enemigo):
        return self.get_inteligencia() * self.libro - enemigo.get_defensa()

    def subir_nivel(self, Nivel):
        multiplicador_por_nivel = 1.05
        fuerza = (Nivel + 1 ) * multiplicador_por_nivel
        inteligencia = (Nivel + 3) * multiplicador_por_nivel
        fe = ( Nivel + 1) * multiplicador_por_nivel
        defensa = (Nivel + 2) * multiplicador_por_nivel
        vida = (Nivel + 100) * multiplicador_por_nivel
        super().subir_nivel(fuerza, inteligencia, fe, defensa, vida)
