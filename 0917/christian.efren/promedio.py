# !/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
# SPDX-License-Identifier: GPL-3.0-or-later
# Christian Efrén

"""
Ejemplo de un módulo
"""

#.1 Codigo par realizar el promedio de 5 numeros

print("Promedio de 5 numeros")


#.2 En esta sección solicitamos los 5 numeros para realizar la operación

num1 = eval(input("ingresa el primer  número: "))
num2 = eval(input("ingresa el segundo número: "))
num3 = eval(input("ingresa el tercer  número: "))
num4 = eval(input("ingresa el cuarto  número: "))
num5 = eval(input("ingresa el quinto  número: "))


#.3 Se imprime mientras realiza la operación para realizar el promedio
print("el promedio del número es el siguiente",(num1 + num2 + num3 + num4 + num5)/5 )
