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
    print("------------DEBUG--------------------")
    print("///Para ver que imprimen los add.argument de argparse")
    print("arch de in: ",args.Archivin) #imprime nombre arch de in
    print("name arch de salida: ",args.nombre_de_salida)#imprime nombre q diste a arch out
    print("arch de out:\n",args.gen_text)#imprime arch out
    print(args.Archivin)
    print("--------------------------------")


    content = args.Archivin #gaurdamos el arg en content
    with open(content) as txt1:
        lines = txt1.readlines()
    print("-------------DEBUG--------------")
    print("///Para imprimir todo el texto como string")
    #print(lines.rstrip())#imprime toda la lista
    print("///Podemos separar sus lineas como listas")
    print(lines[0].rstrip())#imprime elemento 0 de lista sin\n
    print(lines[1].rstrip())
    print(lines[6])
    print("--------------------------------")


    print("-------------DEBUG--------------")
    print("///Para separar esas listas en mas listas")
    print("y acceder a sus elementos")
    print("cadena original:\n",lines[0].rstrip())
    listat1_1 = lines[0].split(",")
    print("lista separada por ,: \n",listat1_1)
    print("--------------------------------")
    print("Elemento by element:")
    print(listat1_1[0])
    print(listat1_1[1])
    print(listat1_1[2])
    print(listat1_1[3])
    




if __name__ == "__main__":
    main()
