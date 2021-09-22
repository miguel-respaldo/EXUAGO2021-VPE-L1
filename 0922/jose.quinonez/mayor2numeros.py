#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
PROGRAMA QUE CALCULA EL NUMERO MAYOR ENTRE 2 DATOS
"""

#OBTENCION DE DATOS

print("Programa que obtiene el número mayor de dos datos")
dato1 = eval(input("Ingrese el numero 1: "))
dato2 = eval(input("Ingrese el numero 2: "))

#CALCULO DEL NUMERO MAYOR

if dato1 > dato2:
    print("El numero mayor es:", dato1)
elif dato2 > dato1:
    print("El numero mayor es:", dato2)
else:
    print("Los numeros son iguales")


