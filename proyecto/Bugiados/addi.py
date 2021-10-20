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
    #rt = rt[1:1]
    #if rt == 'x': 
    rs = rs[1:2]
    a = decimal_a_binario(int(rs))
    if len(a) == 1: 
        a.insert(0,0)
        a.insert(0,0)
    if len(a) == 2: 
        a.insert(0,0)
    print("0001",a[0],a[1],a[2])
    arg = "0001" + str(a[0]) + str(a[1]) + str(a[2]) + "\n"
    print(arg)
    f = open ('salida.txt', 'a')
    f.write(arg)
    f.close()

def decimal_a_binario(num_dec):
    modulos = []
    num_bin = 0
    multiplicador = 1
    while num_dec != 0:
       # num_bin = num_bin + num_dec % 2 * multiplicador
        #num_dec //= 2
        #multiplicador *= 10
        modulos.insert(0,num_dec % 2)
        num_dec //= 2
    return modulos

def convert_m_i(a):
    for i in range(len(a)):
        a[i] = int(a[i])
    return a[i]

def main():
    """
    Comentario de la función
    
    print("Hola Mundo")
    """
    addi("x5","x3",0)
    addi("x0","x1",0)
    print(decimal_a_binario(1))
    
    #print(len(decimal_a_binario(2)))
if __name__ == "__main__":
    main()

