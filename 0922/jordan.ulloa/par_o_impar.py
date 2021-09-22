#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Programa para detectar un par o impar
print("Ingresa un numero para saber si es par o impar")

#se ingresa el valor por el usuario para evaluarse
com1 = eval(input("Ingresar el numero : "))

#se realiza la división para obtener el residuo
com1 = com1 % 2

# se ejecutan las condiciones para evaluar si el numero es par o impar
if com1 == 1:
    print("El numero es Impar")
elif com1 == 0:
    print("El numero es Par")
else:
    print("No se encontro resultado")
