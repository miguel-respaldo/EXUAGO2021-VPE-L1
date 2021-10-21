#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
'''
Team Bugiados by AlvaradoCesar&PerezMoises
MIPS Architecture Operations
PROYECTO    PROYECTO    PROYECTO
'''
import argparse
import sys
import ast


def main():
    #imprime el contenido de un archivo que entro como argumento
    parser = argparse.ArgumentParser()
    #metodo add_argument es usado pa especificar cuales opc de
    #commandline el programa esta dispuesto a ejecutar
    #el siguiente parametro acepta un .txt de entrada
    parser.add_argument("Archivin", help="Ingrese su nombredearchivo.txt")
    #el sig parametro le genera un archivin de txt
    parser.add_argument("-t","--text",action="store_true",
            dest="gen_text", default=False, help="Generar tu txt")
    #el sig argumento es para tunear el name de tu txt de salida
    parser.add_argument("-o","--output",action="store",dest="nombre_de_salida",
            default="salida.o",help="Name del archivo de salida")
    
    #metodo parse_args retorna datos con opciones especificadas
    #se guarda el retorno en args
    args = parser.parse_args()


    content = args.Archivin #gaurdamos el arg en content
    with open(content) as txt1:
        lines = txt1.readlines()
    k = 0
    print("--------------DEBUG VISUAL HELP--------------")
    print(lines)
    
    print("///Para separar esas listas en mas listas")
    print("y acceder a sus elementos")
    print("cadena original:\n",lines[0].rstrip())
    for i in lines:
        dato = lines[k].split(",")
       
        #print(lista1_1[k])
        if "add" in dato:
            add(dato[1],dato[2],dato[3])
            print("---ADD_PARAMETERS---")
            print(dato[1],dato[2],dato[3])
            print("--------END ADD------")
        if "addi" in dato:
            addi(dato[1],dato[2],dato[3])
        if "and" in dato:
            andF(dato[1],dato[2],dato[3])
            print("----AND_PARAMETERS----")
            print(dato[1],dato[2],dato[3])
            print("--------END And------")
        if "andi" in dato:
            continue
        if "beq" in dato:
            continue
        if "bne" in dato:
            continue
        if "j" in dato:
            continue
        if "jal" in dato:
            continue
        if "jr" in dato:
            continue
        if "lb" in dato:
            continue
        if "or" in dato:
            orF(dato[1],dato[2],dato[3])
        if "sb" in dato:
            continue
        if "sll" in dato:
            sll(dato[1],dato[2],dato[3])
        if "sb" in dato:
            continue
        if "srl" in dato:
            srl(dato[1],dato[2],dato[3])
        
        k += 1
    
    print("------Main Function Succesfully executed---------")


#moy's implementation

def add(rd, rs, rt):
    rd = rd[1:2]
    rs = rs[1:2]
    rt = rt[1:2]
    a = decimal_a_binario(int(rd))
    b = decimal_a_binario(int(rs))
    c = decimal_a_binario(int(rt))
    while len(a) != 3: 
        a.insert(0,0)
    while len(b) != 3:
        b.insert(0,0)
    while len(c) != 3:
        c.insert(0,0)
    arg = "0000" + str(b[0]) + str(b[1]) + str(b[2]) + str(c[0]) + str(c[1]) + str(c[2])
    arg = arg + str(a[0]) + str(a[1]) + str(a[2]) + "00000\n"
    write_down("salida.txt", arg)
    
def andF(rd,rs,rt):
    rd = rd[1:2]
    rs = rs[1:2]
    rt = rt[1:2]
    a = decimal_a_binario(int(rd))
    b = decimal_a_binario(int(rs))
    c = decimal_a_binario(int(rt))
    while len(a) != 3: 
        a.insert(0,0)
    while len(b) != 3:
        b.insert(0,0)
    while len(c) != 3:
        c.insert(0,0)
    arg = "0010" + str(b[0]) + str(b[1]) + str(b[2]) + str(c[0]) + str(c[1]) + str(c[2])
    arg = arg + str(a[0]) + str(a[1]) + str(a[2]) + "00000\n"
    write_down("salida.txt", arg)
    
def orF(rd, rs, rt):
    rd = rd[1:2]
    rs = rs[1:2]
    rt = rt[1:2]
    a = decimal_a_binario(int(rd))
    b = decimal_a_binario(int(rs))
    c = decimal_a_binario(int(rt))
    while len(a) != 3: 
        a.insert(0,0)
    while len(b) != 3:
        b.insert(0,0)
    while len(c) != 3:
        c.insert(0,0)
    arg = "1100" + str(b[0]) + str(b[1]) + str(b[2]) + str(c[0]) + str(c[1]) + str(c[2])
    arg = arg + str(a[0]) + str(a[1]) + str(a[2]) + "00000\n"
    write_down("salida.txt", arg)
    
def sll(rd, rs, rt):
    rd = rd[1:2]
    rs = rs[1:2]
    rt = rt[1:2]
    a = decimal_a_binario(int(rd))
    b = decimal_a_binario(int(rs))
    c = decimal_a_binario(int(rt))
    while len(a) != 3: 
        a.insert(0,0)
    while len(b) != 3:
        b.insert(0,0)
    while len(c) != 3:
        c.insert(0,0)
    arg = "1110" + str(c[0]) + str(c[1]) + str(c[2]) + str(b[0]) + str(b[1]) + str(b[2])
    arg = arg + str(a[0]) + str(a[1]) + str(a[2]) + "00000\n"
    write_down("salida.txt", arg)
 
def srl(rd, rs, rt):
    rd = rd[1:2]
    rs = rs[1:2]
    rt = rt[1:2]
    a = decimal_a_binario(int(rd))
    b = decimal_a_binario(int(rs))
    c = decimal_a_binario(int(rt))
    while len(a) != 3: 
        a.insert(0,0)
    while len(b) != 3:
        b.insert(0,0)
    while len(c) != 3:
        c.insert(0,0)
    arg = "1111" + str(c[0]) + str(c[1]) + str(c[2]) + str(b[0]) + str(b[1]) + str(b[2])
    arg = arg + str(a[0]) + str(a[1]) + str(a[2]) + "00000\n"
    write_down("salida.txt", arg)

def addi(rt,rs,imm): #[xn,xn,c]
    rs = rs[1:2] #[x1]
    rt = rt[1:2]
    a = decimal_a_binario(int(rs))
    b = decimal_a_binario(int(rt))
    while len(a) != 3: 
        a.insert(0,0)
    while len(b) != 3:
        b.insert(0,0)
    arg = "0001" + str(a[0]) + str(a[1]) + str(a[2])
    arg = arg + str(b[0]) + str(b[1]) + str(b[2])
    imm1 = imm[0:2]
    if imm1 == "0x": 
        s = ast.literal_eval(imm) #?
        s = decimal_a_binario(int(s))
        while len(s) != 8:
            s.insert(0,0)
    else: 
        imm1 = imm[0:1]
        print(imm1)
        if imm1 == "-":
            imm1 = imm[1:2]
            print(imm1)
            s = decimal_a_binario(int(imm1))
            while len(s) != 8: 
                s.insert(0, 1)
        else:
            s = decimal_a_binario(int(imm1))
            while len(s) != 8: 
                s.insert(0, 0)
    arg = arg + str(s[0]) + str(s[1]) + str(s[2]) + str(s[3])
    arg = arg + str(s[4]) + str(s[5]) + str(s[6]) + str(s[7]) + "\n"
    write_down("salida.txt", arg)
    



def decimal_a_binario(num_dec):
    modulos = []
    num_bin = 0
    multiplicador = 1
    if num_dec != 0:
        while num_dec != 0:
            # num_bin = num_bin + num_dec % 2 * multiplicador
            #num_dec //= 2
            #multiplicador *= 10
            modulos.insert(0,num_dec % 2)
            num_dec //= 2
        return modulos
    else:
        modulos.insert(0,0)
        return modulos
        
        
   #ESTE ES MI MODO DE IMPRIMIR
   
def write_down(filename, arg):
    print(arg)
    f = open ('salida.txt', 'a')
    f.write(arg)
    f.close()

#ending moy's implementation
if __name__ == "__main__":
    main()
