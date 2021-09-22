#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""
print("|INGRESA DOS NUMEROS PARA COMPARAR|")

#CAPTURA DE DATOS INGRESADOS POR EL USUARIO
a = eval(input("Ingresa primer numero: "))
b = eval(input("Ingresa segundo numero: "))

#COMPARA LOS NUMEROS PARA DECIDIR CUAL ES MAYOR 
if (a > b):
    print("El numero ", a, "es mayor que ", b)
elif (b > a):
    print("El numero ", b, "es mayor que ", a)
    
else:
    print("Los numeros son iguales!!!")

