import os
#Variables Globlales se pueden utilizar en cualquier parte del código
conj_TP = set() #Conjuntos Vacíos
conj_TB = set()
conj_TML = set()
conj_TCSS = set()

def TaPython(): #Función para el taller de python
    N_asist=int(input("\n---Taller de Python---\n¿Cuantos asistentes desea registrar?\nCANTIDAD DE ASISTENTES: "))
    for A in (range(N_asist)):
        n = A + 1
        nombre = input("Nombre asistente %d:"%n)
        conj_TP.add(nombre)
    return (conj_TP)

def TaBlender(): #Función para el taller de blender
    N_asist=int(input("\n---Taller de Blender---\n¿Cuantos asistentes desea registrar?\nCANTIDAD DE ASISTENTES: "))
    for A in (range(N_asist)):
        n = A + 1
        nombre = input("Nombre asistente %d: "%n)
        conj_TB.add(nombre)
    return (conj_TB)

def TaML(): #Función para el taller de Machine learning
    N_asist=int(input("\n---Taller de Machine Learning---\n¿Cuantos asistentes desea registrar?\nCANTIDAD DE ASISTENTES: "))
    for A in (range(N_asist)):
        n = A + 1
        nombre = input("Nombre asistente %d: "%n)
        conj_TML.add(nombre)
    return (conj_TML)

def TaCss(): #Función para el taller de Css
    N_asist=int(input("\n---Taller de CSS---\n¿Cuantos asistentes desea registrar?\nCANTIDAD DE ASISTENTES: "))
    for A in (range(N_asist)):
        n = A + 1
        nombre = input("Nombre asistente %d: "%n)
        conj_TCSS.add(nombre)
    return (conj_TCSS)

def registro(): #Función para el registro
    print("\n¿A cuál taller desea registrarse?")
    R=int(input("1.-Taller de Python  \n2.-Taller de Blender \n3.-Taller de Machine Learning \n4.-Taller de CSS \nSelección: "))
    if R == 1:
        TP = TaPython()
        print(TP)
    elif R == 2:
        TB = TaBlender()
        print(TB)
    elif R == 3:
        TM = TaML()
        print(TM)
    elif R == 4:
        TC = TaCss()
        print(TC)
    else: 
        print("Ingrese una opción válida")
    
    exit = int(input("\n¿Desea realizar otro registro?\n1. Sí   2. No\nSelección: "))
    if exit == 1:
        registro()
    elif exit == 2:
        evento()
    else:
        print("Opción no válida")
    
def info():

    total = conj_TP | conj_TB | conj_TML | conj_TCSS
    interseccion = conj_TP & conj_TB & conj_TML & conj_TCSS
    diferencia_simetrica = conj_TP ^ conj_TB ^ conj_TML ^ conj_TCSS
    solo_python = [i for i in diferencia_simetrica if i in conj_TP]
    solo_blender = [i for i in diferencia_simetrica if i in conj_TB]
    solo_ml = [i for i in diferencia_simetrica if i in conj_TML]
    solo_css =[i for i in diferencia_simetrica if i in conj_TCSS]

    print(f"\nTaller de Python: {len(conj_TP)} Registrados")
    print(f"Nombres de los registrados en el Taller de Python:") 
    for i in conj_TP:
        print("*",i)

    print(f"\nTaller de Blender: {len(conj_TB)} Registrados")
    print(f"Nombres de los registrados en el Taller de Blender:") 
    for i in conj_TB:
        print("*",i)

    print(f"\nTaller de Machile Learning: {len(conj_TML)} Registrados")
    print(f"Nombres de los registrados en el Taller de Machine Learning:")
    for i in conj_TML:
        print("*",i) 
    
    print(f"\nTaller de CSS: {len(conj_TCSS)} Registrados")
    print(f"Nombres de los registrados en el Taller de CSS:")
    for i in conj_TCSS:
        print("*",i)

    print(f"\nEstas personas asistirán a todos los talleres:")
    for i in interseccion:
        print("*",i)
    
    print("\nEstas personas asistirán a un solo taller:") 
    for i in diferencia_simetrica:
        print("*",i)
    
    print("\nRegistrados solo en el taller de Python:") 
    for i in solo_python:
        print("*",i)
    
    print("\nRegistrados solo en el taller de Blender:") 
    for i in solo_blender:
        print("*",i)
    
    print("\nRegistrados solo en el taller de Machine learning:") 
    for i in solo_ml:
        print("*",i)
    
    print("\nRegistrados solo en el taller de Css:")
    for i in solo_css:
        print("*",i)

    print(f"\nTotal de asistentes al evento: {len(total)}")
    print("Lista de nombres:")
    for i in total:
        print("*",i)
    
#Programa Principal
def evento():
    while True:
        print("\n¡Bienvenido al Evento DIVEC!\n¿Qué desea hacer?\n1.-Registrarse a un curso\n2.-Consultar la información de registro\n3.-Salir del programa")
        opc = int (input("---->"))
        if opc == 1:
            registro()
        elif opc == 2:
            info()
        elif opc == 3:
            print("Abandonando el programa...")
            break
        else:
            print("Ingrese una opción válida")
        

def run():

    evento()

if __name__ == '__main__':
    run()

#Limpiar pantalla
#Manejar el error de el numero de asistentes
