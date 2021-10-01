#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#definicion de serie de fibonacci
def fibonacci(num):

    #si el numero ingresado es menor a 2 regresa un 1
    if num <= 2:
        num = 1
    
    #si no lo que hace es sumar las dos posiciones anteriores asta la posicion desada
    else:
        num = fibonacci(num - 1) + fibonacci(num - 2)
    
    #resa el resultado
    return num

#funcion principal
def main():

    #pide el dato y lo guarda
    numero = int(input("Escribe el numero a calacular de la serie de fibonacci:  "))
    
    #si el numero es menor a uno retorna un print
    if numero < 1:
        print("chale krnal eso no te lo venimos manejando")
    else:
        print("la posicion {} de la serie de fibonacci es: {}".format(numero,fibonacci(numero)))

if __name__=="__main__":
    main()
