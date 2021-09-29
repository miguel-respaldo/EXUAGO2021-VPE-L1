#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# Autores: Victor Sandoval & Gustavo Solorio
# SPDX-License-Identifier: GPL-3.0-or-later
# 0 1 1 2 3 5 8 13 21 34 55 89 144
# **Se considera la posicion '0' = 0
#

#Se define la funcion para calcular la serie de fibonacci
def fibonacci(numero):
    x=0 #Valor conocido de la posicion 0
    y=1 #Valor conocido de la posicion 1
    suma=0 # Valor actual de la serie de fibonacci
    #Como empieza a guardar los numeros en la posicion 2, se declara una lista
    #Para ingresar los primeros valores ya conocidos
    serie_fibonacci = [0,1]
    for i in range(numero):
        suma=x+y
        serie_fibonacci.append(suma)
        x=y
        y=suma
    return serie_fibonacci[numero]

def main():
    print ("Se considera la posicion '0' = 0")
    numero = int(input("Escribe un número para calcular su serie de fibonacci: "))
    #Se imprime la serie con la posicion solicitada
    print("La posición {} de la serie de fibonacci es {}".format(numero,
        fibonacci(numero)))
    
if __name__ == "__main__":
    main()
