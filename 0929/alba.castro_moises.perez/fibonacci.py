#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#se define la funcion con las 2 primeras posiciones con excepciones
# 0 1 1 2 3 5
# 0 1 2 3 4 5
#Autores: Alba castro
#         Moises Perez


#Funcion de la serie de Fibonacci, calculo por medio de ciclos

def fibonacci(n):

    #Excepciones para valores iniciales (conocidos)
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    #caso para valores pertenecientes a la serie
    else: 
        #valores iniciales para la serie f1 = valor i; f2= valor i-1
        #f3 valor de salida. 
        f1 = 0
        f2 = 0
        f3 = 0

        #se realiza un ciclo para las sumas de cada una de las posiciones
        #ciclo para el cálculo de los valores de la serie, hasta el valor
        # indicado

        for i in range(n):
            f1 = i
            f2 = i-1
            f3 = f1+f2
        #salida de ciclo, se obttiene el resultado final 
        return f3

#se pide al usuario la posicion que se quiere imprimir y se manda a llamar de la funcion de fibonacci
def main():
    #instrucciones para el usuario
    numero = int(input("Escribe un número para calcular su serie de fibonacci: "))
    #Salida de valor
    print("La posición de la serie de fibonacci es ", fibonacci(numero)) 
    #format(numero,fibonacci(numero)))
        
if __name__ == "__main__":
    main()
