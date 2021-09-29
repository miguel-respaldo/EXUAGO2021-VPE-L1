#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""
#funcion que realiza el calculo de la sucesion de fibonacci
def fibo(numero):
    #inicializacion de variables para guardar el ultimo valor y el penultimo
    last = 1
    pen = 0
    #ciclo para calcular el valor dada la posicion
    for i in range(numero+1):
        #condicionales para posicion 0 y 1
        if i == 0:
            res = 0
            continue
        elif i == 1:
            res = 1
            continue
        #Obtencion del resultado
        res = last + pen
        #guardado de la nueva ultima posicion y la nueva penultima posicion
        pen = last
        last = res
        #retorno de variable resultado
    return res

def main():
    #Obtencion de la posicion de la sucesion por parte del usuario
    n = int(input("Ingrese la posicion a consultar de la sucesion fibonacci "))
    #llamado a funcion fibo
    res = fibo(n)
    #impresion del resultado
    print(f"El valor para la posicion {n} es {res}")

if __name__ == "__main__":
    main()

