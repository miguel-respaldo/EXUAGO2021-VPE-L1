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
    lista = []
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
        lines = txt1.readlines())
    k = 1
    print("-------------DEBUG--------------")
    print("///Para separar esas listas en mas listas")
    print("y acceder a sus elementos")
    #print("cadena original:\n",lines[0].rstrip())
    for i in lines:
        lista1_1 = lines[k].split(",")
        print(lista1_1)
        if "add" in lista1_1:
            print(k)
            print("llamando a add")
            add(lista1_1)
        k += 1
    
    print("--------------------------------")

def add(liston):
    print("hola soy add veo que esta lista tiene")
    print(liston[0],liston[1],liston[2],liston[3])
    print("vamos a jugar un rato con esto")
    print("ya que tenemos",liston[0],"opcode sera")
    opcode = (0,0,0,0) #tupla
    print(opcode)
    print(type(opcode))
    
def kesk(kosa):




if __name__ == "__main__":
    main()
