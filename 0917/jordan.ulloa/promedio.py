#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
#titulo para indicar el funcionamiento del programa
print('Ingresa 5 numeros para calcular el promedio')

#input, lineas para cada numero que se ingresa, numero 1 numero 2 numero 3 etc.
numero1 = eval(input("Ingrese primer numero:"))
numero2 = eval(input("Ingrese segundo numero:"))
numero3 = eval(input("Ingrese tercero numero:"))
numero4 = eval(input("Ingrese cuarto numero:"))
numero5 = eval(input("Ingrese quinto numero:"))

# imprime la suma de todos los numero, dividiendo estos entre 5, calculando asi el promerdio
print("Promedio:", ((numero1 + numero2 + numero3 + numero4 + numero5)/5))
