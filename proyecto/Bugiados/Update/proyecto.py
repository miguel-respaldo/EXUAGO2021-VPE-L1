#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
'''
Team Bugiados by AlvaradoCesar&PerezMoises
MIPS Architecture Operations
'''
import argparse
import ast

def main():
    """
    Se utiliza argparse para aceptar argumentos
    desde linea de comandos, en este caso se 
    recibe el nombre del archivo de entrada
    como segundo argumento
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("Archivin", help="Ingrese su nombredearchivo.txt")
    parser.add_argument("-t","--text",action="store_true",
            dest="gen_text", default=False, help="Generar tu txt")
    parser.add_argument("-o","--output",action="store",dest="nombre_de_salida",
            default="salida.o",help="Name del archivo de salida")
    global args
    args = parser.parse_args()
    content = args.Archivin #gaurdamos el arg en content
    with open(content) as txt1:
        lines = txt1.readlines()
    k = 0
    predato=[]
    #El sig for asigna valor a labels y las elimina de la lista
    for i in lines:
        predato.append(lines[k].split(":"))#save in predato every: 
        if "MAIN" in predato[k]:
            global MAIN
            MAIN = k+1
            predato[k].remove("MAIN")
        if "INC" in predato[k]:
            global INC 
            INC = k+1
            predato[k].remove("INC")         
        if "DEC" in predato[k]:
            global DEC
            DEC = k+1
            predato[k].remove("DEC")
        if "EXIT" in predato[k]:
            global EXIT
            EXIT = k+1
            predato[k].remove("EXIT")
        if "FUNC" in predato[k]:
            global FUNC
            FUNC = k+1
            predato[k].remove("FUNC")
        k+=1
    
    """
    Debido a que quitar las etiquetas nos creo una lista con listas
    se inplementa un for para quitarlas
    """
    k=0
    plana = []
    for item in predato:
        plana += item
    
    """
    Iteracion en la lista principal, separamos por ,
    se identifica el mnemonico y se aplica la funcion correspondiente
    pasando a ella los argumentos necesarios
    """
    for i in plana:
        dato = plana[k].split(",")
        if "add" in dato:
            add(dato[1],dato[2],dato[3])
        if "addi" in dato:
            addi(dato[1],dato[2],dato[3])
        if "and" in dato:
            andF(dato[1],dato[2],dato[3])
        if "beq" in dato:
            beq(dato[1],dato[2],dato[3])
        if "bne" in dato:
            bne(dato[1],dato[2],dato[3])
        if "j" in dato: 
            j(dato[1])
        if "jal" in dato:
            jal(dato[1])
        if "jr" in dato:
            jr(dato[1])
        if "lb" in dato:
            lb(dato[1],dato[2],dato[3])
        if "or" in dato:
            orF(dato[1],dato[2],dato[3])
        if "sb" in dato:
            sb(dato[1],dato[2],dato[3])
        if "sll" in dato:
            sll(dato[1],dato[2],dato[3])
        if "srl" in dato:
            srl(dato[1],dato[2],dato[3])  
        k += 1 
    print("------Main Function Succesfully executed---------")
"""
Inicio de funciones para identificar los nemonicos 
se requiere pasar los parámetros a cada una de las funciones
la parte anterior nos ayudo previamente a identificarlos 
"""

def add(rd, rs, rt):
    """
    Se identifica el valor numerico
    de los argumentos para convertirlos
    a binario y rellenarlos con los while
    """
    rd = rd[1:2]
    rs = rs[1:2]
    rt = rt[1:2]
    a = decimal_a_binario(int(rd))
    b = decimal_a_binario(int(rs))
    c = decimal_a_binario(int(rt))
    addvalues(a, 3, 0)
    addvalues(b, 3, 0)
    addvalues(c, 3, 0)
    #Acomodo del registro de 18 bits por arreglo de listas 
    arg = "0000" + str(b[0]) + str(b[1]) + str(b[2]) + str(c[0]) + str(c[1]) + str(c[2])
    arg = arg + str(a[0]) + str(a[1]) + str(a[2]) + "00000\n"
    #Escritura en archivo de salida correspondiente
    writefunc(arg)

def andF(rd,rs,rt):
    rd = rd[1:2]
    rs = rs[1:2]
    rt = rt[1:2]
    a = decimal_a_binario(int(rd))
    b = decimal_a_binario(int(rs))
    c = decimal_a_binario(int(rt))
    addvalues(a, 3, 0)
    addvalues(b, 3, 0)
    addvalues(c, 3, 0)
    arg = "0010" + str(b[0])+str(b[1])+str(b[2])+str(c[0])+str(c[1])+str(c[2])
    arg = arg + str(a[0]) + str(a[1]) + str(a[2]) + "00000\n"
    writefunc(arg)

def orF(rd, rs, rt):
    rd = rd[1:2]
    rs = rs[1:2]
    rt = rt[1:2]
    a = decimal_a_binario(int(rd))
    b = decimal_a_binario(int(rs))
    c = decimal_a_binario(int(rt))
    addvalues(a, 3, 0)
    addvalues(b, 3, 0)
    addvalues(c, 3, 0)
    arg = "1100" + str(b[0])+str(b[1])+str(b[2])+str(c[0])+str(c[1])+str(c[2])
    arg = arg + str(a[0]) + str(a[1]) + str(a[2]) + "00000\n"
    writefunc(arg)
   
def sll(rd, rs, rt):
    rd = rd[1:2]
    rs = rs[1:2]
    rt = rt[1:2]
    a = decimal_a_binario(int(rd))
    b = decimal_a_binario(int(rs))
    c = decimal_a_binario(int(rt))
    addvalues(a, 3, 0)
    addvalues(b, 3, 0)
    addvalues(c, 3, 0)
    arg = "1110" + str(c[0])+str(c[1])+str(c[2])+str(b[0])+str(b[1])+str(b[2])
    arg = arg + str(a[0]) + str(a[1]) + str(a[2]) + "00000\n"
    writefunc(arg)  

def srl(rd, rs, rt):
    rd = rd[1:2]
    rs = rs[1:2]
    rt = rt[1:2]
    a = decimal_a_binario(int(rd))
    b = decimal_a_binario(int(rs))
    c = decimal_a_binario(int(rt))
    addvalues(a, 3, 0)
    addvalues(b, 3, 0)
    addvalues(c, 3, 0)
    arg = "1111" + str(c[0])+str(c[1])+str(c[2])+str(b[0])+str(b[1])+str(b[2])
    arg = arg + str(a[0]) + str(a[1]) + str(a[2]) + "00000\n"
    writefunc(arg) 

def addi(rt,rs,imm):
    rs = rs[1:2] 
    rt = rt[1:2]
    a = decimal_a_binario(int(rs))
    b = decimal_a_binario(int(rt))
    addvalues(a, 3, 0)
    addvalues(b, 3, 0)
    arg = "0001" + str(a[0]) + str(a[1]) + str(a[2])
    arg = arg + str(b[0]) + str(b[1]) + str(b[2])
    """
    En caso de que argumento imm sea
    un numero la siguiente estructura 
    lo formatea a binario si viene dado como
    caso 1 0xn, caso 2 -n y caso 3 n
    """
    imm1 = imm[0:2]
    if imm1 == "0x": 
        s = ast.literal_eval(imm)
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
    writefunc(arg)

def bne(rt,rs,imm): 
    rs = rs[1:2] 
    rt = rt[1:2]
    a = decimal_a_binario(int(rs))
    b = decimal_a_binario(int(rt))
    addvalues(a, 3, 0)
    addvalues(b, 3, 0)
    arg = "0101" + str(b[0]) + str(b[1]) + str(b[2])
    arg = arg + str(a[0]) + str(a[1]) + str(a[2])
    imm1 = imm
    if imm1 == "MAIN\n":
        l = decimal_a_binario(MAIN)
        while len(l) != 8:
            l.insert(0,0) 
    if imm1 == "INC\n":
        l = decimal_a_binario(INC)
        while len(l) != 8:
            l.insert(0,1)
    if imm1 == "DEC\n":
        l = decimal_a_binario(DEC)
        while len(l) != 8:
            l.insert(0,0) 
    if imm1 == "EXIT\n":
        l = decimal_a_binario(EXIT)
        while len(l) != 8:
            l.insert(0,0) 
    if imm1 == "FUNC\n":
        l = decimal_a_binario(FUNC)
        while len(l) != 8:
            l.insert(0,0) 
    arg = arg + str(l[0]) + str(l[1]) + str(l[2]) + str(l[3])
    arg = arg + str(l[4]) + str(l[5]) + str(l[6]) + str(l[7]) + "\n"
    writefunc(arg)

def beq(rt,rs,imm):
    rs = rs[1:2] 
    rt = rt[1:2]
    a = decimal_a_binario(int(rs))
    b = decimal_a_binario(int(rt))
    addvalues(a, 3, 0)
    addvalues(b, 3, 0)
    arg = "0100" + str(b[0]) + str(b[1]) + str(b[2])
    arg = arg + str(a[0]) + str(a[1]) + str(a[2])
    imm1 = imm
    if imm1 == "MAIN\n":
        l = decimal_a_binario(MAIN)
        while len(l) != 8:
            l.insert(0,0) 
    if imm1 == "INC\n":
        l = decimal_a_binario(INC)
        while len(l) != 8:
            l.insert(0,0)
    if imm1 == "DEC\n":
        l = decimal_a_binario(DEC)
        while len(l) != 8:
            l.insert(0,0) 
    if imm1 == "EXIT\n":
        l = decimal_a_binario(EXIT)
        while len(l) != 8:
            l.insert(0,0) 
    if imm1 == "FUNC\n":
        l = decimal_a_binario(FUNC)
        while len(l) != 8:
            l.insert(0,0) 
    arg = arg + str(l[0]) + str(l[1]) + str(l[2]) + str(l[3])
    arg = arg + str(l[4]) + str(l[5]) + str(l[6]) + str(l[7]) + "\n"
    writefunc(arg)

def j(imm): 
    arg = "0110" 
    imm1 = imm
    if imm1 == "MAIN\n":
        l = decimal_a_binario(MAIN)
        while len(l) != 14:
            l.insert(0,0) 
    if imm1 == "INC\n":
        l = decimal_a_binario(INC)
        while len(l) != 14:
            l.insert(0,0)
    if imm1 == "DEC\n":
        l = decimal_a_binario(DEC)
        while len(l) != 14:
            l.insert(0,0) 
    if imm1 == "EXIT\n":
        l = decimal_a_binario(EXIT)
        while len(l) != 14:
            l.insert(0,0) 
    if imm1 == "FUNC\n":
        l = decimal_a_binario(FUNC)
        while len(l) != 14:
            l.insert(0,0) 
    arg = arg +str(l[0]) + str(l[1]) + str(l[2]) + str(l[3])
    arg = arg + str(l[4]) + str(l[5]) + str(l[6]) + str(l[7]) 
    arg = arg + str(l[8]) + str(l[9]) + str(l[10]) + str(l[11])
    arg = arg + str(l[12])+ str(l[13]) + "\n"
    writefunc(arg)

def jal(imm):
    arg = "0111" 
    imm1 = imm
    if imm1 == "MAIN\n":
        l = decimal_a_binario(MAIN)
        while len(l) != 14:
            l.insert(0,0) 
    if imm1 == "INC\n":
        l = decimal_a_binario(INC)
        while len(l) != 14:
            l.insert(0,0)
    if imm1 == "DEC\n":
        l = decimal_a_binario(DEC)
        while len(l) != 14:
            l.insert(0,0) 
    if imm1 == "EXIT\n":
        l = decimal_a_binario(EXIT)
        while len(l) != 14:
            l.insert(0,0) 
    if imm1 == "FUNC\n":
        l = decimal_a_binario(FUNC)
        while len(l) != 14:
            l.insert(0,0) 
    arg = arg +str(l[0]) + str(l[1]) + str(l[2]) + str(l[3])
    arg = arg + str(l[4]) + str(l[5]) + str(l[6]) + str(l[7]) 
    arg = arg + str(l[8]) + str(l[9]) + str(l[10]) + str(l[11])
    arg = arg + str(l[12])+ str(l[13]) + "\n"
    writefunc(arg)

def jr(imm):
    arg = "1010" 
    imm  = imm[1:2]
    l = decimal_a_binario(int(imm))
    while len(l) != 14:
        l.append(0)
    arg = arg +str(l[0]) + str(l[1]) + str(l[2]) + str(l[3])
    arg = arg + str(l[4]) + str(l[5]) + str(l[6]) + str(l[7]) 
    arg = arg + str(l[8]) + str(l[9]) + str(l[10]) + str(l[11])
    arg = arg + str(l[12])+ str(l[13]) + "\n"
    writefunc(arg)

def sb(rt,imm,rs): 
    rs = rs[1:2] 
    rt = rt[1:2]
    a = decimal_a_binario(int(rs))
    b = decimal_a_binario(int(rt))
    addvalues(a, 3, 0)
    addvalues(b, 3, 0)
    arg = "1101" + str(a[0]) + str(a[1]) + str(a[2])
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
    writefunc(arg)

def lb(rt,imm,rs): 
    rs = rs[1:2] 
    rt = rt[1:2]
    a = decimal_a_binario(int(rs))
    b = decimal_a_binario(int(rt))
    addvalues(a, 3, 0)
    addvalues(b, 3, 0)
    arg = "1011" + str(a[0]) + str(a[1]) + str(a[2])
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
    writefunc(arg)

        
#Funcion para convertir numeros decimales a binarios
def decimal_a_binario(num_dec):
    modulos = []
    num_bin = 0
    multiplicador = 1
    if num_dec != 0:
        while num_dec != 0:
            modulos.insert(0,num_dec % 2)
            num_dec //= 2
        return modulos
    else:
        modulos.insert(0,0)
        """
        Al finalizar, se regresa una matriz con los valores
        binarios a modo de matriz [0 x n]
        """
        return modulos
#Función para completar de bits matriz de conversión a binario
def addvalues(m, lg, v):
    while len(m) != lg:
        m.insert(0, v)
#Función para escribir el código de salida.  
def writefunc(arg):
    if args.Archivin == "codigo1.txt":
        write_down("salida1.txt", arg)
    elif args.Archivin == "codigo2.txt":
        write_down("salida2.txt", arg)
    elif args.Archivin == "codigo3.txt":
        write_down("salida3.txt", arg)
    else:
        write_down("salida4.txt",arg)
#Funcion para escribir archivos de salida (.txt)
def write_down(filename, arg):
    print(arg)
    if args.Archivin == "codigo1.txt":
        f = open('salida1.txt', 'a')
    elif args.Archivin == "codigo2.txt":
        f = open('salida2.txt', 'a')
    elif args.Archivin == "codigo3.txt":
        f = open('salida3.txt', 'a')
    else:
        f = open('salida4.txt', 'a')   
    f.write(arg)
    f.close()
#
if __name__ == "__main__":
    main()
