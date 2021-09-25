#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
#se agrega el titulo de la tabla de multiplicar

print("ingrese un numero para saber su tabla de multiplicar, solo tablas del uno al diez")

#se agrega el ingreso del dato para el usuario
num = eval(input("Ingrese el numero: "))

#se agregan lo smultiplos
tabla2 = ["1","2","3","4","5","6","7","8","9","10"]

#se realiza un for para realizar cada multiplicacion
if num < 11:
    for i in tabla2:
        print(int(i) * num)
else:
    print("numero muy grande")
