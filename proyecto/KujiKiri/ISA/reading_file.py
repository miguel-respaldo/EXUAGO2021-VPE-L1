#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
    This program reads a file that the user want to transform (codigo1.txt,
    codigo2.txt, codigo3.txt, codigo4.txt) and returns a tupple with the
    content of  the file read.
"""

#Function that read the file and return a list with the lines
def readfile(nombre):
    #Opens the file with the name nombre and stores it in valores
    valores = open(nombre)
    #Reads the lines and stores them in lineas
    lineas = valores.readlines()
    #Eliminates the jump line character from the end of each line.
    lineas = list(map(lambda l: l.rstrip('\n'), lineas))
    #Return the list with the code.
    return lineas

#Test block of code
if __name__ == "__main__":
    print(readfile("codigo1.txt"))
