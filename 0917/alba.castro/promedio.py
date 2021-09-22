#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#se explica el programa
print("El siguiente programa realizara el promedio de 5 numeros ingresados")

#se piden los numeros a calcular
numero1 = eval(input("Ingresa el primer numero: "))

numero2 = eval(input("Ingresa el segundo numero: "))

numero3 = eval(input("Ingresa el tercer numero: "))

numero4 = eval(input("Ingresa el cuarto numero: "))

numero5 = eval(input("Ingresa el ultimo numero: "))

#calculo e ipresion del promedio
print("El promedio es el siguiente:")
print((numero1 + numero2 + numero3 + numero4 + numero5)/5)
