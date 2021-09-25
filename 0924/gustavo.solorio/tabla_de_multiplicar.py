#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
#Tablas de multiplicar
#Gustavo Alejandro Solorio Ramos

#Se solicita la tabla que se quiere mostrar
eleccion = eval(input("Escribe la tabla de multiplicar que quieres: "))
x=1

#Hace la multiplicacion con un while
while x<11 :
    resultado = eleccion * x
    print("{:d} x {:d} = {:d}".format( eleccion,x,resultado))
    x+=1
else :
    print("fin")
