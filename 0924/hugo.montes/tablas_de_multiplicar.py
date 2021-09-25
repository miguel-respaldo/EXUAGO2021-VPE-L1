#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#programa que muestra las multiplicaciones

print("tablas de multiplicar")

#ingresa el numero de la tabla que desa saber
num = int(input("ingrese el numero de la tabla que desea saber: \n"))

#se pone el if para ver que el numero ingresado sea del 0 al 10

if num <= 10:

#el for es para imprimir recursivamente junto con su rango le pone un limite
    for r in range(11):
      
        #imprime la tabla
        print(r, "*" , num, "=", r*num)
else: print("No esta implementada la tabla que desea.")
