#Ejercicio 1

#1.-Determinar 2 conjuntos con al menos 5 elementos distintos cada uno
print("Definiendo los conjuntos:")
conj_a= {23,48,34,98,78}
conj_b= {45,67,128,99,156}

print(f"Conjunto A: {conj_a} \nConjunto B: {conj_b}")

#2.-Declare un tercer conjunto a partir de un objeto iterable
conj_c = set(range(2,51,2))
print(f"Conjunto C: {conj_c}")

#3.-Declare un cuarto conjunto de tipo inmutable por medio de la función frozenset()
conj_d = frozenset({16,89,56,43,17,567})
print(f"Conjunto D: {conj_d}")

#4.-Evalúe si los elementos 5, ‘A’ y 17 pertenecen a alguno de los 4 conjuntos declarados.
print("\nEvalauando la pertenecia de un elemento:")
print(f"\n¿5 pertenece a los conjuntos?\n Para el conjunto A: {5 in conj_a}\n Para el conjunto B: {5 in conj_b}\n Para el conjunto C: {5 in conj_c}\n Para el conjunto D: {5 in conj_d}")
print(f"\n¿'A' pertenece a los conjuntos?\n Para el conjunto A: {'A' in conj_a}\n Para el conjunto B: {'A' in conj_b}\n Para el conjunto C: {'A' in conj_c}\n Para el conjunto D: {'A' in conj_d}")
print(f"\n¿17 pertenece a los conjuntos?\n Para el conjunto A: {17 in conj_a}\n Para el conjunto B: {17 in conj_b}\n Para el conjunto C: {17 in conj_c}\n Para el conjunto D: {17 in conj_d}")

#5.-Añada un nuevo elemento al primer conjunto por medio de la función add().
print("\nUso de la función add()")
conj_a.add(12367)
print(f"Se agregó 12367 al Conjunto A: {conj_a}")

#6.-Elimine a un elemento del segundo conjunto por medio de la función discard().
print("\nUso de la función discard()")
conj_b.discard(128)
print(f"Se eliminó 128 del conjunto B: {conj_b}")

#7.-Elimine a un elemento del tercer conjunto por medio de la función remove().
print("\nUso de la función remove()")
conj_c.remove(36)
print(f"Se eliminó 36 del conjunto C: {conj_c}")

#8.-Elimine a un elemento del primer conjunto por medio de la función pop().
print("\nUso de la función pop()")
conj_a.pop()
print(f"Se eliminó un elemento al azar del Conjunto A: {conj_a}")

#9.-Elimine a todos los elementos del tercer conjunto por medio de la función clear().
print("\nUso de la función clear()")
conj_c.clear()
print(f"Se eliminaron todos los elementos del Conjunto C: {conj_c}")

#10.-Verifique la longitud del primer conjunto por medio de la función len().
print("\nNúmero de elementos en un conjunto")
print(f"Elementos del conjunto A: {len(conj_a)}")

#11.-Copie los elementos del segundo conjunto al tercer conjunto por medio de la función copy()
print("\nUso de la función copy()")
conj_c = conj_b.copy()
print(f"Se copiaron los elementos del conjunto B al Conjunto C.\nConjunto B:{conj_b}\nConjunto C:{conj_c}")

#12.-Actualice los elementos del primer conjunto con los elementos del segundo conjunto por medio de la función update().
print("\nUso de la función update()")
conj_a.update(conj_b)
print(f"Se actualizaron los elementos del conjunto A con los elementos del conjunto B: {conj_a}")

#13.-Encuentre el valor máximo y mínimo del 1er, 2do y 4to conjunto por medio de las funciones max() y min() respectivamente.
print("\nMáximo y Mínimo")
print(f"Valor Máximo del conjunto A: {max(conj_a)}\nValor Mínimo del conjunto A: {min(conj_a)}")
print(f"Valor Máximo del conjunto B: {max(conj_b)}\nValor Mínimo del conjunto B: {min(conj_b)}")
print(f"Valor Máximo del conjunto D: {max(conj_d)}\nValor Mínimo del conjunto D: {min(conj_d)}")

#14.-Itere sobre todos los elementos del primer conjunto e imprímalos.
print("\nIteración de conjuntos")
print("Elementos del conjunto A:")
for element in conj_a:
  print(element)

#Ejercicio 2

#1.-Agregue una celda de código y declare los siguientes conjuntos:
A = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
B = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
C = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}
print("Declaración de conjuntos:")
print(f"Conjunto A: {A}\nConjunto B: {B}\nConjunto C: {C}")

#2.-Realice la operación A∪B∪C (unión) e imprima la respuesta.
print(f"\nUnión de todos los conjuntos: {A|B|C}")

#3.-Realice la operación B∩C∩A (intersección) e imprima la respuesta.
print(f"\nIntersección de todos los conjuntos: {B&C&A}")

#4.-Realice la operación B\A (diferencia) e imprima la respuesta.
print(f"\nDiferencia del Conjunto B respecto al conjunto A: {B-A}")

#5.-Realice la operación C ^ A (diferencia simétrica) e imprima la respuesta.
print(f"\nDiferencia simétrica del Conjunto C y el conjunto A: {C^A}")

#6.-Realice la operación A == B (igualdad) e imprima la respuesta.
print(f"\n¿El conjutno A y el Conjunto B son iguales?: {A==B}")

#7.-Indique si B es un subconjunto de A.
print(f"\n¿El conjunto B es un subconjunto del conjunto A?: {B.issubset(A)}")

#8.-Indique si C es un superconjunto de B.
print(f"\n¿El conjunto C es un superconjunto del conjunto B?: {C.issuperset(B)}")

#9.-Indique si A es un conjunto disconexo de B y C.
print(f"\n¿El conjunto A es disconexo del conjunto B?: {A.isdisjoint(B)}\n¿El conjunto A es disconexo del conjunto C?: {A.isdisjoint(C)}")

