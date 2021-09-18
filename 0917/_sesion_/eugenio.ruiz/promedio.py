#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""
#17 de Septiembre del 2021
#Calcular promedio de 5 numeros

#Solicita datos necesarios
num1 = eval(input("Ingresa numero 1: ")) #solicita 1er numero
num2 = eval(input("Ingresa numero 2: ")) #solicita 2do numero
num3 = eval(input("Ingresa numero 3: ")) #solicita 3er numero
num4 = eval(input("Ingresa numero 4: ")) #solicita 4to numero
num5 = eval(input("Ingresa numero 5: ")) #solicita 5to numero

#Imprime mensaje con promedio de los 5 numeros
print("El promedio es ",((num1+num2+num3+num4+num5)/5)) #imprime promedio
