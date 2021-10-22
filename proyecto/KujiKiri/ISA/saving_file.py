#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
"""
    This module is going to write a file with the content of the module 2 and
    save it with the name given on the command line when running the executable
    main program.
"""
def write_to(nombre: str, code_list: list, ftype: str):

    #First checks the extension of the file to decide wich mode use, txt or bin
    if '.txt' in ftype:
        #Open the file with the name stored in nombre in write mode
        f_out = open(nombre, "w")

        #Iterates in the lines of code_list, and writes them in the new file
        for line in code_list:
            f_out.write(line + '\n')

        #Close of the file
        f_out.close()
    #If the extension is .bin, executes this block of code
    else:
        #Open the file in binary mode
        f_out = open(nombre, "wb")
        #Creates a empty list to store the values that are going to be writen
        #into the file
        values = []

        #Iterates the lines of the list code_list
        for line in code_list:

            #Reverses the string line
            l_back = line[::-1]
            #Sets the position to zero
            ch_pos = 0
            #Sets the byte value to zero
            w_byte = 0

            #Iterates the characters from the string, this to get the value of
            #each byte of code.
            for char in l_back:
                #Inside this block, the algorithm processes 8 bits each cicle
                #and append the byte value into values list
                if char == '1':
                    w_byte += 2**ch_pos

                #If it has got 8 bits, appends the value, and resets ch_pos and
                #w_byte
                if (ch_pos + 1) % 8 == 0:
                    values.append(w_byte)
                    ch_pos = 0
                    w_byte = 0
                else:
                    ch_pos += 1

            #Appends the value of the two last bits to the list.
            if ch_pos > 0:
                values.append(w_byte)
        #When it finished processing the whole list, it converts the list
        #values into a bytearray, to be able to write it into the file.
        values = bytearray(values)

        #Writes the bytearray values into the file and later it closes it.
        f_out.write(values)
        f_out.close()

#Block of code that executes a test of the module.
if __name__ == "__main__":
    CODIGO = 'codigo1pru.txt'
    LISTA = ["000010101011110100", "000101100001001101", "110101011100000011"]
    write_to(CODIGO, LISTA, '.txt')

    CODIGO2 = 'codigo1pru.bin'
    LISTA = ["000010101011110100", "000101100001001101", "110101011100000011"]
    write_to(CODIGO2, LISTA, '.bin')
