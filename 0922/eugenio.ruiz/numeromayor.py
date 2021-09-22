#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
# SPDX-License-Identifier: GPL-3.0-or-later
#
#INTEL BOOTCAMP ITESO Verificacion PreSilicio
#Phyton
#Eugenio Alejandro Ruiz Mejia

#Solicitar datos
print("Ingrese el valor de cada numero para indicar cual es el mayor")
num1=eval(input("Ingrese el primer numero: ")) 
num2=eval(input("ingrese el segundo numero: "))

if num1 > num2:             #primer comparacion
    print("El numero mayor es: ",num1)
elif num1 == num2:          #segunda comparacion
    print("Los numeros son iguales")
else:                       #tercer comparacion
    print("El numero mayor es: ",num2)


