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
OPCODE = tuple(("0000","0001","0010","0011","0100","0101","0110","0111","1010","1011","1100","1101","1110","1111"))

REGISTROS = tuple(("x0","x1","x2","x3","x4","x5","x6","x7"))
REGISTROS_BINARIOS = tuple(("000","001","010","011","100","101","110","111"))

def get_opcode(mnemonico):
    ret = -1
    for x in range(len(MNEMONICOS)):
        if MNEMONICOS[x] == mnemonico.strip().lower():
            ret = OPCODE[x]
            break
    return ret

def get_registro(reg, bits = 3):
    ret = -1
    if "0x" in reg:
        return  bin(int(reg.split("0x")[1], 16) )[2:].zfill(bits)
    elif "x" in reg:
        for x in range(len(REGISTROS)):
            if REGISTROS[x] == reg.strip().lower():
                ret = REGISTROS_BINARIOS[x]
        return ret.zfill(bits)
    elif "-" in reg:
        return bin(int(reg) % (1 << bits ))[2:]
    else:
        return bin(int(reg))[2:].zfill(bits)

def offset(tag, count, bits, txt, flag = 0):
    i = 1

    file = open(txt,"r")

    for line in file.readlines():
        if tag in line and count != i:
            if flag:
                return get_registro(str(i-count), bits)
            else:
                return get_registro(str(i), bits)
        i += 1


def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("archivo", help="Archivo de Entrada")
    parser.add_argument("-t", "--text", action="store_true", dest="gen_texto",
            default=False, help="Generar codigo de texto")
    parser.add_argument("-o", "--output", action="store", dest="nombre_de_salida",
            default="salida.o", help="Nombre de archivo salida")

    args = parser.parse_args()

    print(args.archivo)
    print(args.nombre_de_salida)
    print(args)

    open_file = open(args.archivo)
    f = open(args.nombre_de_salida,"w") 
    j = 1

    for line in open_file.readlines():
    #b = a.readlines()
        line = line.replace("\t", "").replace(" ", "").replace("\n","")
        if(":" in line):
            
            line = line.split(":")[1].split(",")
        else:
            line = line.split(",")
        
        if(line[0] in MNEMONICOS):
            
            if(line[0] == "add"):#revisar pos4
                f.write(get_opcode(line[0]) + get_registro(line[2]) + get_registro(line[3]) + get_registro(line[1], 8) + "\n" )
            
            elif(line[0] == "addi"):
                f.write(get_opcode(line[0]) + get_registro(line[2]) + get_registro(line[1]) + get_registro(line[3], 8)  + "\n" )
            
            elif(line[0] == "and"):#revisar pos4
                f.write(get_opcode(line[0]) + get_registro(line[2]) + get_registro(line[3]) + get_registro(line[1], 8)  + "\n" )
            
            elif(line[0] == "andi"):
                f.write(get_opcode(line[0]) + get_registro(line[2]) + get_registro(line[1]) + get_registro(line[3], 8)  + "\n" )
            
            elif(line[0] == "beq"):
                f.write(get_opcode(line[0]) + get_registro(line[1]) + get_registro(line[2]) + offset(line[3], j, 8, args.archivo, 1) + "\n" )
            
            elif(line[0] == "bne"):
                f.write(get_opcode(line[0]) + get_registro(line[1]) + get_registro(line[2]) + offset(line[3], j, 8, args.archivo,  1) + "\n" )
            
            elif(line[0] == "j"):
                f.write(get_opcode(line[0]) + offset(line[1], j, 14, args.archivo) + "\n" )
            
            elif(line[0] == "jal"):
                f.write(get_opcode(line[0]) + offset(line[1], j, 14, args.archivo) + "\n" )
            
            elif(line[0] == "jr"):
                f.write(get_opcode(line[0]) + get_registro(line[1]) + get_registro("0", 11) + "\n" )
            
            elif(line[0] == "lb"):
                f.write(get_opcode(line[0]) + get_registro(line[3]) + get_registro(line[1]) + get_registro(line[2], 8) + "\n" )
            
            elif(line[0] == "or"):
                f.write(get_opcode(line[0]) + get_registro(line[2]) + get_registro(line[3]) + get_registro(line[1], 8) + "\n" )
            
            elif(line[0] == "sb"):
                f.write(get_opcode(line[0]) + get_registro(line[3]) + get_registro(line[1]) + get_registro(line[2], 8) + "\n" )
            
            elif(line[0] == "sll"):
                f.write(get_opcode(line[0]) + get_registro(line[3]) + get_registro(line[2]) + get_registro(line[1], 8) + "\n" )
            
            elif(line[0] == "srl"):
                f.write(get_opcode(line[0]) + get_registro(line[3]) + get_registro(line[2]) + get_registro(line[1], 8) + "\n" )
        j =+ 1
    f.close() 
    open_file.close()        

        

if __name__ == "__main__":
    main()

