#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# SPDX-License-Identifier: GPL-3.0-or-later
#
#ITESO DIPLOMADO VERIFICACION PRESILICIO 
#PYTHON
#EUGENIO ALEJANDRO RUIZ MEJIA
#JUAN LUIS MAGANA 
#PROGRAMA QUE DIGA SI UN NUMERO ES PAR O IMPAR

print("Programa que detecta si un numero es par o impar")
num1 = eval(input("Ingrese el numero: "))   #solicita num

#Analisis del numero
#Si mod = 0 entonces el numero no tiene residuo al dividir
#El numero sera par, cualquier otro caso sera impar

if num1%2 == 0:
    print("El numero introducido es par")
else:
    print("El numero es impar")


