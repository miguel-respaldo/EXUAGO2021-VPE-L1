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

if __name__ == "__main__":
    main()

