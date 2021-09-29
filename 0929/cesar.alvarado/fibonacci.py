#!/usr/bin/env python3i
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Programa que muestra la serie de fibonacci de un determinado numero
Team: RobertoVazquez&CesarAlvarado
"""
print("Este programa crea la sucecion fibonacci hasta el numero dado por el usuario")
#Definiciona de la funcion fibonacci con parametro lim
def fibonacci(lim):
    a = 0   #variable de inicio de sucesion
    b = 1   #variable de inicio de sucesion
    #ciclo para recorrer hasta el valor de deseado
    for i in range(lim):
#        if(a==0&&b==1):
#            print(a)
#            print(b)
        suma = a+b  #suma de valores iniciales
        a = b       #a se le da el valor de b
        b = suma    #b toma el valor de la sumatoria
        print(b)    #aprovechamos el for para imprimir en lista
    return b        #retornamos b

#Se pide el valor al usuario
numero = eval(input("Ingrese un numero: "))
#se imprime el valor final obtenido
print("El valor para la posicion {} es {}".format(numero,fibonacci(numero)))






