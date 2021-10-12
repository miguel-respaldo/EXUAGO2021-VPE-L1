#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Este traduce del ISA de MIPS a codigo máquina.
"""

import os
import argparse
import mnemonicos

GEN_TEXTO=False
NOMBRE_DE_SALIDA=""
ARCHIVO_DE_ENTRADA=""
PC=1
ETIQUETAS=[]
DIR_ETIQUETAS=[]


def parse_file(archivo):

    global PC
    global ETIQUETAS
    global DIR_ETIQUETAS

    file = open(archivo,"r")
    for linea in file:

        # Quitamos el enter
        linea = linea.strip()

        # Buscamos etiquetas
        if ":" in linea:
            ETIQUETAS.append(linea.split(":")[0].strip())
            DIR_ETIQUETAS.append(PC)
            linea = linea.split(":")[1].strip()

        # Separamos por comas
        lista_linea = linea.split(",")

        # Buscamos mnemonico
        opcode = mnemonicos.get_opcode(lista_linea[0])
        if opcode == -1:
            print("El mnemonico \"",lista_linea[0].strip(),"\" es invalido")
            file.close()
            exit(1)

        PC += 1
        print(lista_linea)




def main():
    """
    Función principal del programa
    """
    global GEN_TEXTO
    global NOMBRE_DE_SALIDA
    global ARCHIVO_DE_ENTRADA
    parser = argparse.ArgumentParser()
    parser.add_argument("archivo", help="Archivo de entrada")
    parser.add_argument("-t", "--text",
                        action="store_true", dest="gen_texto", default=False,
                        help="Generar código en texto")
    parser.add_argument("-o", "--output",
                        action="store", dest="nombre_de_salida", default="salida.o",
                        help="Nombre de archivo de salida")

    args = parser.parse_args()
    GEN_TEXTO=args.gen_texto
    NOMBRE_SALIDA=args.nombre_de_salida
    ARCHIVO_DE_ENTRADA=args.archivo
    
    if not os.path.exists(ARCHIVO_DE_ENTRADA):
        print(f"No se encuentra el archivo {ARCHIVO_DE_ENTRADA}")
        exit(1)

    parse_file(ARCHIVO_DE_ENTRADA)

if __name__ == "__main__":
    main()

