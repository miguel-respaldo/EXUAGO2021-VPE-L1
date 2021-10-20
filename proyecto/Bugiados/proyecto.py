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



def main():
    opcode = ['0000','0001','0010','0011','0100','0101','0110']
            #add    #addi   #and    #andi #beq  #bne    #j
    opcode2= ['0111','1010','1011','1100','1101','1110','1111']
            #jal    #jr     #lb     #or     #sb #sll    #srl
    maquina = []
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
    print(lines)
    print("-------------DEBUG--------------")
    
    print("///Para separar esas listas en mas listas")
    print("y acceder a sus elementos")
    print("cadena original:\n",lines[0].rstrip())
    for i in lines:
        lista1_1 = lines[k].split(",")
       
        #print(lista1_1[k])
        if "add" in lista1_1:
            #sublist = lista1_1.split(",")            
            #print(lista1_1[0]) #me imprime el mnemonico
            print(lista1_1[1])
            print(lista1_1[2])
            print(lista1_1[3])
            machin = open("cod1.txt","a")
            machin.write("\n")
            machin.write(opcode[0])
            machin.close()
        if "addi" in lista1_1:
            machin = open("cod1.txt","a")
            machin.write("\n")
            machin.write(opcode[1])
            #machin.write("\n")
            machin.close()
        if "and" in lista1_1:
            machin = open("cod1.txt","a")
            machin.write("\n")
            machin.write(opcode[2])
            machin.close()
        if "andi" in lista1_1:
            machin = open("cod1.txt","a")
            machin.write("\n")
            machin.write(opcode[3])
            machin.close()  
        if "beq" in lista1_1:
            machin = open("cod1.txt","a")
            machin.write("\n")
            machin.write(opcode[4])
            machin.close() 
        if "bne" in lista1_1:
            machin = open("cod1.txt","a")
            machin.write("\n")
            machin.write(opcode[5])
            machin.close() 
        if "j" in lista1_1:
            machin = open("cod1.txt","a")
            machin.write("\n")
            machin.write(opcode[6])
            machin.close() 
        if "jal" in lista1_1:
            machin = open("cod1.txt","a")
            machin.write("\n")
            machin.write(opcode2[0])
            machin.close() 
        if "jr" in lista1_1:
            machin = open("cod1.txt","a")
            machin.write("\n")
            machin.write(opcode2[1])
            machin.close()       
        if "lb" in lista1_1:
            machin = open("cod1.txt","a")
            machin.write("\n")
            machin.write(opcode2[2])
            machin.close()   
        if "or" in lista1_1:
            machin = open("cod1.txt","a")
            machin.write("\n")
            machin.write(opcode2[3])
            machin.close()      
        if "sb" in lista1_1:
            machin = open("cod1.txt","a")
            machin.write("\n")
            machin.write(opcode2[4])
            machin.close()      
        if "sll" in lista1_1:
            machin = open("cod1.txt","a")
            machin.write("\n")
            machin.write(opcode2[5])
            machin.close()      
        if "srl" in lista1_1:
            machin = open("cod1.txt","a")
            machin.write("\n")
            machin.write(opcode2[6])
            machin.close()      
        
        k += 1
    
    print("--------------------------------")


"""
#next f performs a bdecimal to binary convertion
def tobin(num):
    binary = 0
    multip = 1
    #first a full division is required 
    while num != 0:  #se ejecuta hasta que no halla cociente
        binary = binary + num % 2 * multip
        num = num // 2
        multip = multip * 10
        #ref1
        print(type(binary))
    return binary
"""

if __name__ == "__main__":
    main()
