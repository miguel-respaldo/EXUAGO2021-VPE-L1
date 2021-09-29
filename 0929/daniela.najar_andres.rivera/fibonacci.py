#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Daniela Najar
Andres Rivera
Programa que devuelve un numero de fibonacci que es ingresado por el usuario.
"""

#Se define la funcion que realizara la secuencia de fibonacci
def fibonacci(n):
    #Si la posicion es 0 o 1 regresa dichos valores
    if n == 0:
        return 0
    elif n == 1:
        return 1

    #si no, realiza la secuencia de fibonacci para los demas y devuelve el
    #resultado
    else:
        n1=0
        n2=1
        n3=0
        for x in range(n):
            n3 = n1 + n2
            n1 = n2
            n2 = n3
        return n1

#Se le pide la posicion del numero de fibonacci al usuario que desea desplegar
numFib = int (input (f"Ingresa la posicion del numero de fibonacci que desea conocer: "))

#Se despliega el resultado de la funcion.
print(f"El numero de fibonacci correspondiente a la posicion {numFib} es {fibonacci(numFib)}")
