from .base import Personaje
class Curandero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, fe, defensa, vida, baculo, curacion):
        super().__init__(nombre, fuerza, inteligencia, fe, defensa, vida)
        self.baculo = baculo
        self.curacion = curacion

    def cambiar_arma(self):
        opcion = int(input("Elige un arma: \n(1) Curaloto, daño 2 curacion 6 \n(2)Mataloto, daño 6 curacion 2"))
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



    def subir_nivel(self, Nivel):
        multiplicador_por_nivel = 1.05
        fuerza = (Nivel + 1 ) * multiplicador_por_nivel
        inteligencia = (Nivel + 1) * multiplicador_por_nivel
        fe = ( Nivel + 3) * multiplicador_por_nivel
        defensa = (Nivel + 2) * multiplicador_por_nivel
        vida = (Nivel + 100) * multiplicador_por_nivel
        super().subir_nivel(fuerza, inteligencia, fe, defensa, vida)

    def restaurar_vida(self, vida):

        self.__vida = self.__vida + vida+ self.curacion
        print("Te has curado ", self.__vida, "de vida")
