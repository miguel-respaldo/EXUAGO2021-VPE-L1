#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Mnemonicos de el ensamblador
"""

MNEMONICOS = tuple(("add","addi","and","andi","beq","bne","j","jal","jr","lb","or","sb","sll","srl"))

OPCODE = tuple((0,1,2,3,4,5,6,7,10,11,12,13,14,15))

REGISTROS = tuple(("x0","x1","x2","x3","x4","x5","x6","x7"))

def get_opcode(mnemonico):
    ret = -1
    for x in range(len(MNEMONICOS)):
        if MNEMONICOS[x] == mnemonico.strip().lower():
            ret = OPCODE[x]
            break
    return ret

def get_registro(reg):
    ret = -1
    for x in range(len(REGISTROS)):
        if REGISTROS[x] == reg.strip().lower():
            ret = x
            break
    return ret
