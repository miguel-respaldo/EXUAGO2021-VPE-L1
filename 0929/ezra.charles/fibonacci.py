#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Programa que recibe un numero y encuentra su sucesion de fibonacci 
by Francisco Lopez y Ezra Charles
"""
def fibonacci(numero):
    if numero <= 1:
        return numero
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)


def fibonacci_iterativo(numero):
    resultado = 0
    temp1 = 0
    temp2 = 0

    for i in range(numero + 1):
        if(i == 0):
            temp1 = 0
        elif(i == 1):
            temp2 = 1
        else:
            resultado = temp1 + temp2
            temp1 = temp2 
            temp2 = resultado

    return resultado


def main():
    """
    Funcion principal
    """
    numero = int(input("Escribe un número para calcular su serie de fibonacci: "))
    print("La posición {} de la serie de fibonacci es {}".format(numero, fibonacci_iterativo(numero)))


if __name__ == "__main__":
    main()

