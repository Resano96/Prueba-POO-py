#crear la clase con sus atributos
class Personaje:
    nombre = "Default"
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0
#metodo constructor __init__
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        #con __hacemos que no se pueda acceder a los valores desde fuera de la clase
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida

    def atributos (self):
        print(self.__nombre, ":", sep="")
        print("-Fuerza:",self.__fuerza)
        print("-Inteligencia:", self.__inteligencia)
        print("-Defensa:", self.__defensa)
        print("-Vida", self.__vida)

    def subir_nivel(self, fuerza, inteligencia, defensa, vida):
        print(self.__nombre, "ha subido de nivel")
        self.__fuerza = self.__fuerza + fuerza
        self.__inteligencia = self.__inteligencia + inteligencia
        self.__defensa = self.__defensa + defensa
        self.__vida = self.__vida + vida
        print()

    def esta_vivo(self):
        return self.__vida > 0

    def __morir(self):
        self.__vida = 0
        print((self.__nombre), "ha muerto")
        print()

    def daño(self, enemigo):
        return self.__fuerza - enemigo.__defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.__vida = enemigo.__vida - daño
        print(self.__nombre, "ha realizado" , daño , "puntos de daño a", enemigo.__nombre)
        print()
        if enemigo.esta_vivo():
            print("la vida de ", enemigo.__nombre, "es" , enemigo.__vida)
        else:
            enemigo.__morir()

#-----------------------------------------------------------------------------------------------------------------------

    def get_fuerza(self):
        return self.__fuerza

    def set_fuerza(self, fuerza):
        if fuerza < 0 :
            print("Error, no vale fuerza negativa")
        else:
            self.__fuerza = fuerza

    def get_inteligencia(self):
        return self.__inteligencia

    def get_defensa(self):
        return self.__defensa

    def get_vida(self):
        return self.__vida
    def get_name(self):
        return self.__nombre

#-----------------------------------------------------------------------------------------------------------------

class Guerrero(Personaje):
#super copia los atributos de la clase superior, no hace falta usar self
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2)Matadragones, daño 10"))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Numero de arma incorrecto")

    def atributos(self):
        super().atributos()
        print("-Espada:", self.espada)

    def daño(self, enemigo):
        return self.get_fuerza() * self.espada - enemigo.get_defensa()

#----------------------------------------------------------------------------------------------------------------------
class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        super().atributos()
        print("-Libro:", self.libro)

    def daño(self, enemigo):
        return self.get_inteligencia() * self.libro - enemigo.get_defensa()

#--------------------------------------------------------------------------------------------------------------------
#creado de primer personaje
personaje =Personaje("Resa",10,5,3,200)
enemigo = Personaje("Shaggy", 8, 3,5,70)
#creando un guerrero
guerrero = Guerrero("Amy", 20, 10, 10, 1000, 6)
#creando un mago
mago = Mago("Sheldon", 10,15, 3, 1000, 8)

#POLIMORFISMO, VARIAS CLASES USAN EL MISMO METODO
#----------------------------------------------------------------------------------------------------------------------
def combate(jugador1, jugador2):
    turno = 0
    while jugador1.esta_vivo() and jugador2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Accion de ", jugador1.get_name(), ":" , sep="")
        jugador1.atacar(jugador2)
        print(">>> Accion de ", jugador2.get_name(), ":" , sep="")
        jugador2.atacar(jugador1)
        turno = turno +1

    if jugador1.esta_vivo():
        print("\nHa ganado", jugador1.get_name())
    elif jugador2.esta_vivo():
        print("\nHa ganado", jugador2.get_name())
    else:
        print("\nEmpate")

#sacar valores de una clase

#print("El nombre del jugador es", personaje1.nombre)
#print("La fuerza del jugador es", personaje1.fuerza)

personaje.atributos()
personaje.subir_nivel(2,1,3,2)
personaje.atributos()
print("cambio de fuerza a -5")
# personaje.set_fuerza(-5)
personaje.atributos()
guerrero.atributos()
mago.atributos()
mago.subir_nivel(1,5,2,10)
mago.subir_nivel(1,5,2,10)

combate(guerrero, mago)
