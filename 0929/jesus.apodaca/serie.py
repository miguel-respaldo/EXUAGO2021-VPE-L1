#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#Programa para obtener el numero en la posicion dada al programa dentro de la serie de fibonacci
#autores jesus apodaca y leonardo quiñonez
#se define la funcion que obtiene el valor dentro de la serie
def fibonacci(n):
#solo funciona para valores mayores que 2 porque no daria el resultado correcto con este algoritmo programado    
    if n>2:
        a = 1
        b = 1
        c = 1
#se usa el n-2 porque es a partir de ahì que comienza a dar valores destintos de 1
        for x in range(n-2):
            c = a
            a = a + b
            b = c
            
        n = a
#se le asigna el valor de 1 para la posicion 1 y 2       
    else: 
        n=1
    return n

def main():
    #solicita el valor de la posicion dentro de la serie de fibonacci
    numero = int(input("Escribe un número para calcular su serie de fibonacci: "))
    #imprime el valor que tiene la posicion
    print("La posición {} de la serie de fibonacci es {}".format(numero,
        fibonacci(numero)))


if __name__ == "__main__":
    main()

                     
