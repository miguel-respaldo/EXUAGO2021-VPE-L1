#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#Programa que obtiene el valor de una posicion dada de la serie Fibonacci

#Funcion Fibonacci que recibe el valor de la posicion asignada
def fibonacci(n):
    num1 = 0  
    num2 = 1
    numf = 0
    
    #Ciclo que obtiene el valor de la posicion dada
    
    if n <= 0: 
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        for x in range(n - 2):  
            numf = num1 + num2
            num1 = num2
            num2 = numf
        return numf

def main():
    #Entrada del valor de la posicion
    pos = int(input("Ingresa el valor de la posicion: "))
    
    #Impresion del resultado obtenido a traves de funcion fibonacci
    print("El numero de la posicion {} de la serie fibonacci es {}".format(pos,
        fibonacci(pos)))


if __name__ == "__main__":
    main()

