#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
# Autores: Gustavo Solorio & Josue Charles

#Introduccion del programa y captura del numero correspondiente
print("**Programa para imprimir el mes con letras\n")
mes=eval(input("Por favor escribe el numero del mes\n"))

#Se hacen los 12 casos correspondientes a cada mes, en caso de 
#ser >12 o <1 arroja "Mes invalido"
if mes == 1 :
    print("El mes corresponde a Enero\n")
elif mes == 2 :
    print("El mes corresponde a Febrero\n")
elif mes == 3 :
    print("El mes corresponde a Marzo\n")
elif mes == 4 :
    print("El mes corresponde a Abril\n")
elif mes == 5 :
    print("El mes corresponde a Mayo\n")
elif mes == 6 :
    print("El mes corresponde a Junio\n")
elif mes == 7 :
    print("El mes corresponde a Julio\n")
elif mes == 8 :
    print("El mes corresponde a Agosto\n")
elif mes == 9 :
    print("El mes corresponde a Septiembre\n")
elif mes == 10 :
    print("El mes corresponde a Octubre\n")
elif mes == 11 :
    print("El mes corresponde a Noviembre\n")
elif mes == 12 : 
    print("El mes corresponde a Diciembre\n")
else :
    print("Numero de mes no válido\n")
