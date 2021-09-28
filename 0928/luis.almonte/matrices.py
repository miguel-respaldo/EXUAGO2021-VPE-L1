#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
PROGRAMA PARA LLENAR UNA MATRIZ CON DATOS INGRESADOS POR EL USUARIO
"""

print("|DEFINE LA LONGITUD DE LA MATRIZ DESEADA|")

#SE DEFINE LA CANTIDAD DE FILAS Y COLUMNAS DE LA MATRIZ
filas = int(input("Ingresa la cantidad de filas de tu matriz: "))

columnas = int(input("Ingresa la cantidad de columnas de tu matriz: "))

#SE CREA LA MATRIZ 
matriz = []

#POR CADA FILA SE AGREGA UNA LISTA VACIA A LA LISTA INICIAL
for i in range (filas):
    matriz.append([])
    for j in range (columnas): #LOS DATOS SE AGREGAN A LA MATRIZ
        matriz[i].append(input("Ingresa los datos de tu matriz: "))

#SE MUESTRA EN PANTALLA LA MATRIZ CON SUS DATOS
for elemento in range (filas):
    print(matriz[elemento])
