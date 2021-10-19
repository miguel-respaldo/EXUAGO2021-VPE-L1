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
#from definicion import * 
#import definicion


MNEMONICOS = tuple(("add","addi","and","andi","beq","bne","j","jal","jr","lb","or","sb","sll","srl"))

OPCODE = tuple((0000,0001,0010,0011,0100,0101,0110,0111,1010,1011,1100,1101,1110,1111))

REGISTROS_BINARIOS = tuple((000,001,010,011,100,101,110,111))
REGISTROS = tuple(("x0","x1","x2","x3","x4","x5","x6","x7"))
def get_opcode(mnemonico):
    ret = -1
    for x in range(len(MNEMONICOS)):
        if MNEMONICOS[x] == mnemonico.strip().lower():
            ret = OPCODE[x]
            break
    return ret

def get_registro(reg):
    ret = -1
    for x in range(len(REGISTROS)):
        if REGISTROS[x] == reg.strip().lower():
            ret = REGISTROS_BINARIOS[x]
            break
    return ret

def get_c2(num):
    

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
        
        if(line[0] in MNEMONICOS):
            
            if(line[0] == "add"):
                f.write(get_opcode(line[0]) + get_registro(line[0]))
        #print (type(line))
        #print (len(line))
        #print(line)
    #print (MNEMONICOS)




if __name__ == "__main__":
    main()

