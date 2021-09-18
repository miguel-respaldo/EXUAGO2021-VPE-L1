#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#Programa que calcula el promedio de 5 valores

print("Ingresa 5 numeros para obtener un promedio: ")

#Ingresar valores del tipo int o float solamente

valor1 = eval(input("ingresa el primer numero:" ))
valor2 = eval(input("ingresa el primer numero:" ))
valor3 = eval(input("ingresa el primer numero:" ))
valor4 = eval(input("ingresa el primer numero:" ))
valor5 = eval(input("ingresa el primer numero:" ))


print("El promedio de los valores ingresados es:",(valor1 + valor2 + valor3 + valor4 + valor5)/5)


