#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#Se pide 5 datos numericos al usuario
num1 = eval(input("Ingresa primero número: "))
num2 = eval(input("Ingresa segundo  número: "))
num3 = eval(input("Ingresa tercero  número: "))
num4 = eval(input("Ingresa cuarto número: "))
num5 = eval(input("Ingresa quinto número: "))

#Se guarda en variable prom el promedio de los datos pedidos
prom = (num1 + num2 + num3 +num4 +num5)/5

#se imprimer con un mensaje el promedio
print("El promedio de los 5 numeros son",prom)


