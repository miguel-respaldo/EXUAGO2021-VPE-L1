#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Solicitar al usuario las dimensiones de la matriz
fil=int(input("Ingresa el numero de filas: "))
col=int(input("Ingresa el numero de columnas: "))

# Indica al usuario de que tamano es su matriz
print(f"Tu matriz sera de {fil}x{col}")

#Crear listas vacias
lista_final=[]
lista=[]

#Se ira recorriendo por fila cada columna y capturando el dato
for x in range (fil):
    lista_final.append([])
    lista_final[x]=lista
    for y in range(col):
        print(f"Ingresa la posicion [fila][columna] -> [{x}][{y}]", end="")
        pos=int(input())
        lista.append(pos)
    lista=[]
    
print (lista_final)
