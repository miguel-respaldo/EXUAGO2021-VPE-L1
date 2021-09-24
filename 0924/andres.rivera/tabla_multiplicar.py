#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Programa que imprime las tablas de multiplicar

"""

#Programa que despliega las tablas de multiplicar
print("Programa que desplega las tablas de multiplicar.\n")

#Se le pide al usuario el numero de la tabla que desea desplegar
tab = int (input("Ingresa el numero de la tabla que deseas desplegar: "))

#Se despliega un mensaje de la tabla
print("TABLA DE MULTIPLICAR DEL", tab,":")

#Ciclo for para desplegar cada elemento
for x in range(1, 11):
    print (x, "x", tab, "=", (x*tab))





