#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Mnemonicos de el ensamblador
"""

MNEMONICOS = tuple(("add", "addi", "and", "andi", "beq", "bne", "j", "jal",
                   "jr", "lb", "or", "sb", "sll", "srl"))

OPCODE = tuple((0,1,2,3,4,5,6,7,10,11,12,13,14,15))

