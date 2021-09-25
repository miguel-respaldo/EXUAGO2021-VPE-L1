#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#Progrma que regrese las tablas de multiplicar dependiendo el numero asignado
print("Programa qeu regresa la tabla de multiplicar del numero asignado")

#Se pide el numero para la tabla de multiplicar
numero = eval(input("Escribe el numero: "))

#Se toma el numero y se ingresa para la tabla
for n in range(1,11):
    multiplicacion = numero * n
    print("", numero , " X " , "", n, " =  ", multiplicacion)
