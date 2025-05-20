class Personaje:
    nombre = "Default"
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0

    def __init__(self, nombre, fuerza, inteligencia, fe, defensa, vida):
        #con __hacemos que no se pueda acceder a los valores desde fuera de la clase
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__fe = fe
        self.__defensa = defensa
        self.__vida = vida

    def atributos (self):
        print(self.__nombre, ":", sep="")
        print("-Fuerza:",self.__fuerza)
        print("-Inteligencia:", self.__inteligencia)
        print("-Fe:" , self.__fe)
        print("-Defensa:", self.__defensa)
        print("-Vida", self.__vida)

    def subir_nivel(self, fuerza, inteligencia, fe, defensa, vida):
        print(self.__nombre, "ha subido de nivel")
        self.__fuerza = self.__fuerza + fuerza
        self.__inteligencia = self.__inteligencia + inteligencia
        self.__fe = self.__fe + fe
        self.__defensa = self.__defensa + defensa
        self.__vida = self.__vida + vida
        print()

    def esta_vivo(self):
        return self.__vida > 0

    def esta_muerto(self):
        return self.__vida < 0

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

    def restaurar_vida(self, vida):
        print("Te has curado ",  vida , "de vida")
        self.__vida = self.__vida + vida

#-------------------------------------------------------------------------------------------------------

    def get_fuerza(self):
        return self.__fuerza

    def set_fuerza(self, fuerza):
        if fuerza < 0 :
            print("Error, no vale fuerza negativa")
        else:
            self.__fuerza = fuerza

    def get_inteligencia(self):
        return self.__inteligencia

    def get_fe(self):
        return self.__fe

    def get_defensa(self):
        return self.__defensa

    def get_vida(self):
        return self.__vida
    def get_name(self):
        return self.__nombre



