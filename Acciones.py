#crear la clase con sus atributos

#metodo constructor __init__



#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------

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




