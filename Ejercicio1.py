#Ejercicio 1

#En una variable guarde una cadena en la cual describa su motivación para estudiar la carrera de computación
motivo= 'Curiosidad por comprender como funciona la tecnología de nuesto día a día'
#imprima en pantalla a la frase completa.
print (motivo)
#Duplique la frase por medio de una operación de repetición e imprima en pantalla.
print (motivo*2)
#Concatene la frase " Gracias por su atención. " al final de su frase e imprima en pantalla.
print (motivo + ", gracias por su atención")
#Aplique al menos tres subdivisiones a su frase e imprima en pantalla.

#1
print (motivo[15])
#2
print (motivo[0:25])
#3
print (motivo[7:])

#Ejercicio 2

#declare dos valores con valores de tipo entero o real
a=45
b=89
#Sume ambas variables e imprima el resultado
print (a+b)
#Reste ambas variables e imprima el resultado
print (a-b)
#Multiplique ambas variables e imprima el resultado
print (a*b)
#Divida ambas variables e imprima el resultado
print (a/b)
#Divida por medio de la división de piso a ambas variables e imprima el resultado
print (b//a)
#Saque el módulo e imprima el resultado
print (b%a)
#Eleve a ambas variables a la potencia 3 e imprima el resultado
print (a**3)
print (b**3)

#Ejercicio 3

#Tome las variables declaradas en el ejercicio 2
a=45
b=89
#Variable 1 igual a Variable 2
print (a==b)
#Variable 1 diferente a Variable 2
print (a!=b)
#Variable 2 mayor que Variable 1
print (b>a)
#Variable 2 menor que Variable 1
print (b<a)
#Variable 1 mayor o igual que Variable 2
print (a>=b)
#Variable 1 menor o igual que Variable 2
print (a<=b)

#Ejercicio 4

#Tome las variables declaradas en el ejercicio 2
a=45
b=89
#no(V1 - 5 >= V2 + 9 y V2 != V1)
print (( not (a-5>=b+9 and b!=a)))
#(V2 x 5 < V1 / 3) o no(V1 == V2 potencia 2)
print ((b*5<a/3) or (not (a==b**2)))
