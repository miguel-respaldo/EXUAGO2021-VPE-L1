#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# Author: Moisés Emmanuel Pérez Ramos
# Fecha: 
"""
Ejemplo de un modulo
"""
def addi(rt,rs,imm): 
    rs = rs[1:2]
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
        import ast
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
def convert_m_i(a):
    for i in range(len(a)):
        a[i] = int(a[i])
    return a[i]
def write_down(filename, arg):
    print(arg)
    f = open ('salida.txt', 'a')
    f.write(arg)
    f.close()
def main():
    """
    Comentario de la función
    
    print("Hola Mundo")
    """
    addi("x2","x0","0x02")
    addi("x4","x0","-1")
    print(decimal_a_binario(1))
    
    
    #print(len(decimal_a_binario(2)))
if __name__ == "__main__":
    main()

