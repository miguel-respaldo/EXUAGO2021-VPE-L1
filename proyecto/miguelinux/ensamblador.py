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


PC=1
ETIQUETAS=[]
DIR_ETIQUETAS=[]

def get_byte_line(opcode, arg1, arg2,arg3):
    return bytearray(3)

def get_str_line(opcode, arg1, arg2,arg3):
    ret = ""
    if   opcode == 0: # add
        ret += "{:04b}".format(opcode)
        ret += "{:03b}".format(arg2)
        ret += "{:03b}".format(arg3)
        ret += "{:03b}".format(arg1)
        ret += "00000"
    elif opcode == 1: # addi
        ret += "{:04b}".format(opcode)
        ret += "{:03b}".format(arg2)
        ret += "{:03b}".format(arg1)
        if arg3 < 0:
            arg3 = (arg3^0xff + 1) & 0xff
            ret += "{:08b}".format(arg3)
        else:
            ret += "{:08b}".format(arg3)
    elif opcode == 2: # and
        ret += "{:04b}".format(opcode)
        ret += "{:03b}".format(arg2)
        ret += "{:03b}".format(arg3)
        ret += "{:03b}".format(arg1)
        ret += "00000"
    elif opcode == 3: # andi
        ret += "{:04b}".format(opcode)
        ret += "{:03b}".format(arg2)
        ret += "{:03b}".format(arg1)
        if arg3 < 0:
            arg3 = (arg3^0xff + 1) & 0xff
            ret += "{:08b}".format(arg3)
        else:
            ret += "{:08b}".format(arg3)
    elif opcode == 4: # beq
        ret += "{:04b}".format(opcode)
        ret += "{:03b}".format(arg1)
        ret += "{:03b}".format(arg2)
        if arg3 < PC:
            arg3 = -arg3
            arg3 = (arg3^0xff + 1) & 0xff
            ret += "{:08b}".format(arg3)
        else:
            arg3 -= PC
            ret += "{:08b}".format(arg3)
    elif opcode == 5: # bne
        ret += "{:04b}".format(opcode)
        ret += "{:03b}".format(arg1)
        ret += "{:03b}".format(arg2)
        if arg3 < PC:
            arg3 = -arg3
            arg3 = (arg3^0xff + 1) & 0xff
            ret += "{:08b}".format(arg3)
        else:
            arg3 -= PC
            ret += "{:08b}".format(arg3)
    elif opcode == 6: # j
        ret += "{:04b}".format(opcode)
        ret += "{:014b}".format(arg1)
    elif opcode == 7: # jal
        ret += "{:04b}".format(opcode)
        ret += "{:014b}".format(arg1)
    elif opcode == 10: # jr
        ret += "{:04b}".format(opcode)
        ret += "{:03b}".format(arg1)
        ret += "00000000000"
    elif opcode == 11: # lb
        ret += "{:04b}".format(opcode)
        ret += "{:03b}".format(arg3)
        ret += "{:03b}".format(arg1)
        if arg2 < 0:
            arg2 = (arg2^0xff + 1) & 0xff
            ret += "{:08b}".format(arg2)
        else:
            ret += "{:08b}".format(arg3)
    elif opcode == 12: # or
        ret += "{:04b}".format(opcode)
        ret += "{:03b}".format(arg2)
        ret += "{:03b}".format(arg3)
        ret += "{:03b}".format(arg1)
        ret += "00000"
    elif opcode == 13: # sb
        ret += "{:04b}".format(opcode)
        ret += "{:03b}".format(arg3)
        ret += "{:03b}".format(arg1)
        if arg2 < 0:
            arg2 = (arg2^0xff + 1) & 0xff
            ret += "{:08b}".format(arg2)
        else:
            ret += "{:08b}".format(arg3)
    elif opcode == 14: # sll
        ret += "{:04b}".format(opcode)
        ret += "{:03b}".format(arg3)
        ret += "{:03b}".format(arg2)
        ret += "{:03b}".format(arg1)
        ret += "00000"
    elif opcode == 15: # srl
        ret += "{:04b}".format(opcode)
        ret += "{:03b}".format(arg3)
        ret += "{:03b}".format(arg2)
        ret += "{:03b}".format(arg1)
        ret += "00000"

    return ret


def get_label(label):
    """
    Función obtiene el valor de una etiqueta
    """
    ret = -1
    for x in range(len(ETIQUETAS)):
        if ETIQUETAS[x].lower() == label.strip().lower():
            ret = DIR_ETIQUETAS[x]
            break
    return ret


def parse_file(archivo_e, archivo_s, texto):
    """
    Función que parse el archivo fuente
    """

    global PC
    global ETIQUETAS
    global DIR_ETIQUETAS

    opcode=0
    arg1=0
    arg2=0
    arg3=0

    modo = "wb"
    if texto:
        modo = "wt"

    fentrada = open(archivo_e,"r")
    fsalida = open(archivo_s, modo)

    for linea in fentrada:
        # Buscamos etiquetas
        if ":" in linea:
            ETIQUETAS.append(linea.split(":")[0].strip())
            DIR_ETIQUETAS.append(PC)

    # Regresamos al inicio del archivo
    fentrada.seek(0)

    for linea in fentrada:

        # Quitamos el enter
        linea = linea.strip()

        # Buscamos etiquetas
        if ":" in linea:
            linea = linea.split(":")[1].strip()

        # Separamos por comas
        lista_linea = linea.split(",")

        for x in range(len(lista_linea)):
            if   x == 0:
                # Buscamos mnemonico
                opcode = mnemonicos.get_opcode(lista_linea[x])
                if opcode == -1:
                    print("El mnemonico \"",lista_linea[0].strip(),"\" es invalido")
                    fentrada.close()
                    fsalida.close()
                    os.remove(archivo_s)
                    exit(1)

                str_opcode = "{:04b}".format(opcode)
            elif x == 1:
                arg1 = mnemonicos.get_registro(lista_linea[x])

                if arg1 == -1:
                    arg1 = get_label(lista_linea[x])

                if arg1 == -1:
                    arg1 = eval(lista_linea[x].strip())

            elif x == 2:
                arg2 = mnemonicos.get_registro(lista_linea[x])

                if arg2 == -1:
                    arg2 = get_label(lista_linea[x])

                if arg2 == -1:
                    arg2 = eval(lista_linea[x].strip())
            elif x == 3:
                arg3 = mnemonicos.get_registro(lista_linea[x])

                if arg3 == -1:
                    arg3 = get_label(lista_linea[x])

                if arg3 == -1:
                    arg3 = eval(lista_linea[x].strip())
            
        if texto:
            linea_salida = get_str_line(opcode, arg1, arg2,arg3)
            linea_salida += "\n"
        else:
            linea_salida = get_byte_line(opcode, arg1, arg2,arg3)
        fsalida.write(linea_salida)
        PC += 1

    fentrada.close()
    fsalida.close()



def main():
    """
    Función principal del programa
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("archivo", help="Archivo de entrada")
    parser.add_argument("-t", "--text",
                        action="store_true", dest="gen_texto", default=False,
                        help="Generar código en texto")
    parser.add_argument("-o", "--output",
                        action="store", dest="nombre_de_salida", default="salida.o",
                        help="Nombre de archivo de salida")

    args = parser.parse_args()
    
    if not os.path.exists(args.archivo):
        print(f"No se encuentra el archivo {args.archivo}")
        exit(1)

    parse_file(args.archivo, args.nombre_de_salida, args.gen_texto)

if __name__ == "__main__":
    main()

