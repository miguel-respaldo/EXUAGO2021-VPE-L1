#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
#titulo de programa que introdusca un numero y que diga de que mes es
print("Ingrese un numero para saber a que mes pertenece")
#ingresar el numeor de mes
num = eval(input("Ingresar el numero: "))
#lista de los meses
mes  = ["Enero","Febrero","Marzo","Abril","Mayo","Junio",
        "Julio","Agosto","Septiembre","Obtubre","Noviembre","Diciembre"]
#evaluacion del mes
if num < 13:
    mes1 = mes[num-1]
#condiciones para verificar que el numero de mes no sea muy grande
if num > 12:
    print("Tu numero es muy grande")
else: 
    print("Tu mes es:", mes1)
    
