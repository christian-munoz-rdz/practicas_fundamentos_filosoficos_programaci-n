
"""
Sentencia for

Ejercicio 1

Solicite al usuario que ingrese una frase e imprima cuantas veces aparece cada vocal (a, e, i, o, u).

Ejemplo de salida en pantalla:


Ingresa una frase: Hola a todos

La letra a aparece 2 veces

La letra e aparece 0 veces

La letra i aparece 0 veces

La letra o aparece 3 veces

La letra u aparece 0 veces
"""

frase = input("Deme una frase: ")
frase = frase.strip()
frase = frase.lower()
a = 0
e = 0 
i = 0
o = 0
u = 0

for letra in frase:
  if letra == "a":
    a += 1
  elif letra == "e":
    e += 1
  elif letra == "i":
    i += 1
  elif letra == "o":
    o += 1
  elif letra == "u":
    u += 1

print(f"\nLa letra a aparece {a} veces")
print(f"\nLa letra e aparece {e} veces")
print(f"\nLa letra i aparece {i} veces")
print(f"\nLa letra o aparece {o} veces")
print(f"\nLa letra u aparece {u}veces")

"""Ejercicio 2

Muestre en pantalla todos los números impares que se encuentran del 1 al 80.


"""

print("Los números impares presentes del 1 al 80 son:")
for i in range(1,81):
  if i % 2 !=0:
    print(i)