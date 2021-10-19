#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""
import argparse
import sys
from definicion import * 
#import definicion

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("archivo", help="Archivo de Entrada")
    parser.add_argument("-t", "--text", action="store_true", dest="gen_texto",
            default=False, help="Generar codigo de texto")
    parser.add_argument("-o", "--output", action="store", dest="nombre_de_salida",
            default="salida.o", help="Nombre de archivo salida")

    args = parser.parse_args()

    ##print(args.archivo)
    ##print(args.nombre_de_salida)
    #print(args)

    open_file = open(args.archivo)
    
    for line in open_file.readlines():
    #b = a.readlines()
        line = line.replace("\t", "").replace(" ", "").replace("\n","")
        if(":" in line):
            line = line.split(":")[1].split(",")
        else:
            line = line.split(",")
        print (line) 

    etiqueta = get_opcode(ret)
    print(etiqueta)




if __name__ == "__main__":
    main()

