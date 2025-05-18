from Acciones import combate
from Personajes.mago import Mago
from Personajes.curandero import Curandero
from Personajes.guerrero import Guerrero
from Personajes.enemigo import Enemigo
import Acciones
#creado enemigo
enemigo = Enemigo("Shaggy", 8, 3,7,4,100,7)
#creando un guerrero
guerrero = Guerrero("Amy", 20, 10, 10, 5, 500,5)
#creando un mago
mago = Mago("Sheldon", 10,15, 3, 3, 400, 5)
#creando un curandero
curandero = Curandero("Bobby", 4,10,4,6,450, 5, 10)

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

combate(mago,guerrero)
mago.subir_nivel(1,5,2,10,10)
mago.atributos()
mago.pocion_vida(20)
mago.atributos()