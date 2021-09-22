#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
# Autores: Gustavo Solorio & Alexis Lopez

#Descripcion del programa y captura del numero
print("***Programa para Determinar par o Impar***\n")
Numero = eval(input("Ingresa un numero a evaluar: "))

#Evaluacion del numero para saber si es par
if Numero%2 == 0 :
    print ("El numero es par")
else : #si no se cumple la condicion anterior por obviedad es impar
    print("El numero es impar")


