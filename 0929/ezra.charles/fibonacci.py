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

# Funcion de fibonacci recursivo 
def fibonacci(numero):
    if numero <= 1: # cuando el caso es 0 o 1 el fibonacci es el mismo indice 0 y 1 respectivamente
        return numero
    else: # llamado recursivo para la suma de los dos ultimos numeros de fibonacci
        return fibonacci(numero - 1) + fibonacci(numero - 2)

# Funcion de fibonacci iterativo 
def fibonacci_iterativo(numero):
    resultado = 0
    temp1 = 0 # suma 1 de fibonacci
    temp2 = 0 # suma 2 de fibonacci

    for i in range(numero + 1):
        if(i == 0): # cuando el caso es fibonacci de 0 el resultado es 0
            temp1 = 0
        elif(i == 1): # cuando el caso es fibonacci de 1 el resultado es 1
            temp2 = 1
            resultado = 1
        else: # cuando el caso es fibonacci mayor a 1
            resultado = temp1 + temp2 # el resultado es la suma de los 2 numeros de fibonacci anteriores
            temp1 = temp2 # se desplaza la suma (la ultima se convierte en penultima)
            temp2 = resultado # el resultado se convierte en la ultima suma para la siguiente iteracion

    return resultado


def main():
    """
    Funcion principal
    """
    # pedir al usuario el numero de la sucesion de fibonacci e imprimir
    numero = int(input("Escribe un número para calcular su serie de fibonacci: "))
    print("La posición {} de la serie de fibonacci es {}".format(numero, fibonacci_iterativo(numero)))


if __name__ == "__main__":
    main()

