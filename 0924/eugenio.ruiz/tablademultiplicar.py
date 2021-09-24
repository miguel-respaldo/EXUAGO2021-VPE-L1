#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#Diplomado en verificacion presilicio
#Python
#Programa que imprime las tablas de multiplicar
#Eugenio Alejandro Ruiz Mejia

#solicitar datos al usuario
multiplo = eval(input("Ingresa la tabla a imprimir: "))

for x in range(0,10): #ciclo for inicia en 0 hasta 10
    print(x+1," x ", multiplo, "es igual a ", (x+1)*multiplo) #imprime result


