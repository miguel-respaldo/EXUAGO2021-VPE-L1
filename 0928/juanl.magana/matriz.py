#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""

def main():
    #declaracion de variable matriz
    matriz = [ ]
    #Ingreso del tamano de la matriz por parte del usuario
    filas = int(input("Ingrese numero de filas: "))
    columnas = int(input("Ingrese numero de columnas: "))
    
    #creacion de matriz de acuerdo al tamano ingresado
    for i in range(filas):
        matriz.append([0]*columnas)
    #llenado de la matriz con datos ingresados por el usuario
    for i in range(filas):
        for j in range(columnas):
            matriz[i][j] = int(input(f"Ingrese dato para posicion {i+1},{j+1}: "))
    # impresion de la matriz
    print(matriz)


if __name__ == "__main__":
    main()

