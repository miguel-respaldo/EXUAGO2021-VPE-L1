#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
import sys


r_inst = { #inst $d,$s,$t
    "add" : "0000",
    "sub" : "000001",
    "slt" : "000101",
    "and" : "0010",
    "or" : "1100",
    "nor" : "001001",
    "xor" : "001010"
}

r_inst_mult = { #inst $s,$t
    "mult" : "000011",
    "div" : "000100"
}

r_inst_move = {
    "mfhi" : "001110",
    "mflo" : "001111"
}

r_inst_shift = { #inst $d
    "sll" : "1110",
    "srl" : "1111",
    "slr" : "1111",
    "sra" : "010011"
}

r_inst_jr = { #inst $s
    "jr" : "1010"
}

i_inst_signed = { #inst $t,$s,C
    "addi" : "0001",
    "slti" : "000110",
}

i_inst_unsigned = { #inst $t,$s,C
    "andi" : "001011",
    "ori" : "001100",
    "xori" : "001101"
}


i_inst_mem = { #inst $t,C($s)
    "lw" : "010100",
    "lb" : "1011",
    "sw" : "010110",
    "sb" : "1101"
}

i_inst_branch = { #inst $s,$t,C
    "beq" : "0100",
    "bne" : "0101"
}

i_inst_lui = { #inst $t,C
    "lui" : "010000"
}

j_inst = { #inst C
    "j" : "0110",
    "jal" : "0111"
}

reg = {
    "x0" : "000",
    "x1" : "001",
    "x2" : "010",
    "x3" : "011",
    "x4" : "100",
    "x5" : "101",
    "x6" : "110",
    "x7" : "111",
    "x8" : "1000",
    "x9" : "1001",
    "$14" : "01110",
    "$15" : "01111",
    "$16" : "10000",
    "$17" : "10001",
    "$18" : "10010",
    "$19" : "10011",
    "$20" : "10100",
    "$21" : "10101",
    "$22" : "10110",
    "$23" : "10111",
    "$24" : "11000",
    "$25" : "11001",
    "$26" : "11010",
    "$27" : "11011",
    "$28" : "11100",
    "$29" : "11101",
    "$30" : "11110",
    "$31" : "11111",
}

def regOrConst(valor):
        machine_lin = ""
        if valor  in reg.keys():
            machine_lin += reg[valor].zfill(8)  # zeros a la izq
        elif valor not in reg.keys():
            if valor.isdecimal():
                bina = "{:8b}".format(int((valor),10)).strip().zfill(8)
                machine_lin += (bina)
            else:  #si  no es registro (reg) ni numero ,sera dato hexadecimal y convertiremos a bin
                if int((valor),16) >= 0:
                    bina = "{:8b}".format(int((valor),16)).strip().zfill(8) # zeros a la izq
                    machine_lin += (bina)
                else:
                    bina = bin((eval("0b"+str(int(bin(int(valor))[3:].zfill(8).replace("0","2").replace("1","0").replace("2","1"))))+eval("0b1")))[2:].zfill(8)
                    machine_lin += bina
        return  machine_lin

f = 0
w = 0

if len(sys.argv) == 3:
    f = open(sys.argv[1], 'r')
    w = open(sys.argv[2], 'w')
else:
    f = open(".\ASSEM4.txt", "r")
    w = open(".\Fib.txt", 'w')
#comentario de prueba de git


labels = {}
count = 0
machines_lines = []
offsets = {}
i=1
lineapos=0
brand= []
for lin in f:
       
        linea = lin.lower()
        linea = linea.replace(',', ' ')
        linea = linea.replace(':', ' ')
        linea = linea.split()
        if(len(linea)==5):
            offsets[linea[-5]]= i
        i = i+1
print(offsets)  
f.seek(0)

for line in f:
    lineapos= lineapos+1
    line = line.lower()
    #end = line.find('#')
    #line = line[:end]
    line = line.replace(',', ' ')
    line = line.replace(':', ' ')
    line = line.split()

    
    if not line:
        continue
    if(len(line)>=4):
        pos=-4

    elif (len(line)==2):
        pos=-len(line)
    

    if line[pos] not in r_inst.keys() \
            and line[pos] not in r_inst_mult.keys() \
            and line[pos] not in r_inst_move.keys() and line[pos] not in r_inst_shift.keys() \
            and line[pos] not in r_inst_jr.keys() and line[pos] not in i_inst_signed.keys() \
            and line[pos] not in i_inst_unsigned.keys() and line[pos] not in i_inst_lui.keys() \
            and line[pos] not in i_inst_mem.keys() and line[pos] not in i_inst_branch.keys() \
            and line[pos] not in j_inst.keys(): print(line[pos],"Nmonicon no Encontrado")       
    machine_line = ""

    if line[pos] in r_inst.keys():
        machine_line += r_inst[line[pos]] #opcode
        machine_line += reg[line[-2]] #rs
        machine_line += reg[line[-1]] #rt
        machine_line += reg[line[-3]].ljust(8,"0") #rd   0 a la derecha
        print(machine_line)

    elif line[pos] in i_inst_signed.keys(): 
        machine_line += i_inst_signed[line[pos]] 
        machine_line += reg[line[-2]]
        machine_line += reg[line[-3]]
        machine_line += regOrConst(line[-1])      
        print(machine_line)

    elif line[pos] in r_inst_shift.keys():
        machine_line += r_inst_shift[line[pos]]
        machine_line += reg[line[-1]]
        machine_line += reg[line[-2]]
        machine_line += reg[line[-3]].ljust(8,"0")
        print(machine_line)
    elif line[pos] in i_inst_mem.keys():
        machine_line += i_inst_mem[line[pos]] 
        machine_line += reg[line[-1]] #rs
        machine_line += reg[line[-3]] #rt
        machine_line += regOrConst(line[-2]) #offset 
        print(machine_line)
    elif line[pos] in i_inst_branch.keys():
        machine_line += i_inst_branch[line[pos]] 
        machine_line += reg[line[-3]] #rs
        machine_line += reg[line[-2]] #rt
        if line[-1] in offsets.keys():
            BranAddr = offsets[line[-1]] -lineapos
            brand.append(BranAddr)
            if (BranAddr >0):
                bina = bin(BranAddr)[2:]
                machine_line += bina.strip().zfill(8) 
            else:
                BranAddr &= (2 << 8-1)-1
                formatStr = '{:0'+str(8)+'b}'
                bina = formatStr.format(int(BranAddr))
                machine_line += str(bina) 
        print(machine_line)
