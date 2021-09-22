#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
# Autor Gustavo Alejandro Solorio Ramos}

#Descripcion del programa e ingreso de datos
print("***Programa para comparar 2 numeros***\n")
Numero1 = eval(input("Ingresa el primer numero: "))
Numero2 = eval(input("Ingresa el segundo numero: "))

#Comparacion de ambos numeros para arrojar el resultado
print("El numero 1 es mayor que el Numero2") if Numero1 > Numero2 else print ("El Numero2 es mayor que el Numero1") if Numero2 > Numero1 else print("Los numeros son iguales")
