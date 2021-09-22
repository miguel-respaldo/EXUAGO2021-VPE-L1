#!/usr/bin/env python3

#Se pide al usuario ingresar 2 numeros
num1 = eval(input("Ingresa numero 1:  "))
num2 = eval(input("Ingresa numero 2:  "))

# se hace la comparativa de los numeros

if num1 > num2:
    print("Num 1 es mayor que Num 2")
elif num1 < num2:
    print("Num 2 es mayor que Num 1")
else:
    print("Los dos numeros son iguales")
