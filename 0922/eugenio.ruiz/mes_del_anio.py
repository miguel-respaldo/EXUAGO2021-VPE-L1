#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
#
#ITESO Diplomado en verificiacion PreSilicio
#Python
#Eugenio Alejandro Ruiz Mejia
#Jordan Ulloa
#Programa que diga el mes del anio 


#Pedir numero al usuario
print("Programa que dice el mes del anio")
num = eval(input("Ingrese un numero: ")) #Solicita num al usuario

#Lista de meses
meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto",
        "Septiembre","Octubre","Noviembre","Diciembre"]

#Imprime el resultado
mesletra = meses[num-1] #Guarda la palabra del mes
print = ("El numero ", num, "es ", mesletra)
