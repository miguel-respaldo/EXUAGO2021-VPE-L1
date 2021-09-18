#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

print("Ingresa 5 numeros")#  cantidad de numeros a ingresar
# Posteriormente se ingresan los numero de uno en uno
numero1 = eval(input("Ingresa numero 1: "))
numero2 = eval(input("Ingresa numero 2: "))
numero3 = eval(input("Ingresa numero 3: "))
numero4 = eval(input("Ingresa numero 4: "))
numero5 = eval(input("Ingresa numero 5: "))

# Se realiza la suma de los cinco numeros y se promedian para guardarlos en
# la variable promedio
promedio = ((numero1 + numero2 + numero3 + numero4 + numero5) / 5 )
print("el promedio es", promedio)# Se imprime el promedio de los 5 numeros
