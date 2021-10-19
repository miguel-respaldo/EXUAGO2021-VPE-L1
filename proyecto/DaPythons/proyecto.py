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

f = 0
w = 0

if len(sys.argv) == 3:
    f = open(sys.argv[1], 'r')
    w = open(sys.argv[2], 'w')
else:
    f = open(".\ASSEM4.txt", "r")
    w = open(".\Fib.txt", 'w')

#comentario de prueba
