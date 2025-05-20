from Acciones import combate, golpear
from Personajes.mago import Mago
from Personajes.curandero import Curandero
from Personajes.guerrero import Guerrero
from Personajes.enemigo import Enemigo
import Acciones
#creado enemigo
enemigo = Enemigo("Shaggy", 10, 8,5,10,100,6)
#creando un guerrero
guerrero = Guerrero("Amy", 20, 5, 2, 15, 120,5)
#creando un mago
mago = Mago("Sheldon", 8,20, 10, 6, 80, 1)
#creando un curandero
curandero = Curandero("Bobby", 5,10,20,8,100, 5, 5)

print("Estadisticas\n"
      "____________\n")
print("Enemigo")
enemigo.atributos()
print("\nMago")
mago.atributos()
print("\nGuerrero")
guerrero.atributos()
print("\nCurandero")
curandero.atributos()

def elegir_personaje():
    opcion = input("¿A quién quieres usar? \n\t(1) Mago \n\t(2) Guerrero \n\t(3) Curandero \n")
    if opcion == "1":
        return mago
    elif opcion == "2":
        return guerrero
    elif opcion == "3":
        return curandero
    else:
        print("Opción no válida, se usará el mago por defecto.")
        return mago

personaje = elegir_personaje()

while True:
    opcion = input("¿Qué quieres hacer?\n\t(1) Atacar auto\n\t(2) Atacar\n\t(3) Curar \n\t(4) Salir \n")
    if opcion == "1":
        combate(personaje, enemigo)
        if personaje.esta_vivo():
              personaje.subir_nivel(1)
    elif opcion == "2":
        personaje.cambiar_arma()
        golpear(personaje,enemigo)
        golpear(enemigo,personaje)
        if enemigo.esta_muerto():
              personaje.subir_nivel(1)
    elif opcion == "3":
        mago.restaurar_vida(20)
        golpear(enemigo,personaje)
    elif opcion == "4":
        break