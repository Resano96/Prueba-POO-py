from Acciones import combate, golpear
from Personajes.mago import Mago
from Personajes.curandero import Curandero
from Personajes.guerrero import Guerrero
from Personajes.enemigo import Enemigo

#creado enemigo
enemigo = Enemigo("Shaggy", 8, 3,7,4,100,7)
#creando un guerrero
guerrero = Guerrero("Amy", 20, 10, 10, 5, 500,5)
#creando un mago
mago = Mago("Sheldon", 10,15, 3, 3, 400, 5)
#creando un curandero
curandero = Curandero("Bobby", 4,10,4,6,450, 5, 10)


curandero.subir_nivel_curandero(2)
curandero.atributos()

curandero.cambiar_arma()
curandero.atributos()

combate(curandero,mago)

#combate(mago,guerrero)

#mago.atributos()
#mago.curacion(20)
#mago.atributos()
#consulta = input("Que personaje quieres revisar?\n mago, guerrero, curandero o enemigo").lower()
#if consulta == "mago":
#      mago.atributos()
#elif consulta == "guerrero":
#      guerrero.atributos()
#elif consulta == "curandero":
#      curandero.atributos()
#elif consulta == "enemigo":
#      enemigo.atributos()
#else:
#      print(consulta , " no es ninguno de los preguntados")
#Pegar re
#guerrero.atributos()
#golpear(mago, guerrero)
#guerrero.atributos()