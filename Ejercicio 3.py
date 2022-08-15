"""
Ejercicio 1

Sentencias Selectivas

Realice un programa que solicite la edad (Dato de tipo entero) de una persona y determine si es niño, adolescente, adulto o anciano, según el siguiente rango de edades:

*   0 a 12 años imprimir Es niño
*   13 a 17 años imprimir Es adolescente
*   18 a 80 años imprimir Es adulto
*   Mayor que 80 imprimir Es anciano

Nota: Utilice una estructura if - elif - else para realizar este ejercicio.
"""

print("***** INICIO DEL PROGRAMA *****")
edad = int (input("\n¿Cuál es tu edad?: "))

if edad <= 12:
  print("\nEres un niño")
elif edad <= 17:
  print("\nEres un adolescente")
elif edad <= 80:
  print("\nEres un adulto")
else:
  print("\nEres un Anciano")

print("\n----- FIN DEL PROGRAMA -----")