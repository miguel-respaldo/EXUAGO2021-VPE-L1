#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
#se presenta el titulo del funcionamineto para saber de que es el codigo
#despues se genera la entrada de texto con instrucciones
print("Programa para comparar dos numeros")
com1 = input("Ingresa tu primer numero: ")
com2 = input("Ingresa tu segundo numero: ")
#revisa si se genera una igualdad
if com1 == com2:
    print("Los dos numeros son iguales")
#se revisa si el primero es mas grande que el segundo
elif com1 > com2:
    print("El primer numero es mas grande que el segundo")
#se revisa si el primero es menor que el segundo
elif com1 < com2:
    print("El primer numero es menor que el segundo")
#se agrega un el se por si no se cumplen las condiciones
else:
    print("Error en la matrix")
