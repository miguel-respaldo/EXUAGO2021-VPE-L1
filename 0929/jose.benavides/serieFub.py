#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#fn = fn-1 + fn-2
#Funcion recursiva para la serie de Fibonacci
def fibo(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibo(num - 1) + fibo(num - 2)

#Se pide al usuario que ingrese un dato
n = eval(input("Ingrese un numero y te regresare el elemento correspondiente a la serie de Fibonacci: "))

#Se guarda el retorno de la funcion 
elemento = fibo(n)

#Se imprime el resultado 
print(f"El {n} corresponde a {elemento} en la serie de Fibonacci")
