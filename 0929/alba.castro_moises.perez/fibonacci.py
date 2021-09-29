#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#Serie fibonacci Alba Castro y Moises Perez
# 0 1 1 2 3 5 8 13 21
# 0 1 2 3 4 5 6  7  8

#se define la funcion con las 2 primeras posiciones con excepcion
def fibonacci(n):
    
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    else: 
        f1 = 0
        f2 = 0
        f3 = 0
        #se realiza un ciclo para las sumas de cada una de las posiciones
        for i in range(n):
            f1 = i
            f2 = i-1
            f3 = f1+f2
        
        return f3

#se pide al usuario la posicion que se quiere imprimir y se manda a llamar de la funcion de fibonacci
def main():
    numero = int(input("Escribe un número para calcular su serie de fibonacci: "))
    
    print("La posición de la serie de fibonacci es ", fibonacci(numero)) 
    #format(numero,fibonacci(numero)))
        
if __name__ == "__main__":
    main()
