#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#Trabajo en equipo serie Alejandro Orozco y Christian Efren Saldivar

#Se inicia la definicio clase de fibonacci
def fibo(n):
#Iniciamos las dos primeras posiciones de la serie
    a=1
    b=1
    if n ==1:
        print("1")
    elif n ==2:
        print("1","1")
    else:
        
        print(a)
        print(b)
    for i in range(n-2):
#Se hace la suma de un valor anterior y el nuevo
            total=a+b 
            b=a
            a=total
            print(total)
    print(f"La posicion {n} es el numero {total}")
#Se imprime en que posicion esta el numero ingresado
num=int(input("Ingresa la posicion que desea ver de la Serie: "))
#Se hace llamado a la funcion con valores
fibo(num)

