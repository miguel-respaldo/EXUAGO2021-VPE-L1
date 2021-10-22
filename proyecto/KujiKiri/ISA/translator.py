#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
This is the module that contains a function that translate the code obtained
from the file and saves it into a new list.
"""

#Here are defined some dictionaries that will have the mnemonics and
#registers with their respective value.

#Mnemonics dictionary with their respective value in decimal.
MNEMOS = {"add": 0, "addi": 1, "and": 2, "andi": 3, "beq": 4, "bne": 5,
          "j": 6, "jal": 7, "jr": 10, "lb": 11, "or": 12, "sb": 13,
          "sll": 14, "srl": 15}
#Registers dictionary with their respective value in decimal.
REGS = {"x0": 0, "x1": 1, "x2": 2, "x3": 3, "x4": 4, "x5": 5, "x6": 6,
        "x7": 7, "C2": 0, "zero": 0}
#Dictionary that contains lists with the order in how args gonna be appended.
ORDER_APPEND = {"std1" : [2, 3, 1, 4], "std2" : [3, 2, 1, 4],
                "off1" : [1, 2, 3], "off2" : [3, 1, 2], "imm0" : [2, 1, 3]}
#Dictionary that holds the wordlenght of each argument
BINFORMAT = {"type1" : [4, 3, 3, 3, 5], "type2" : [4, 3, 3, 8]}

def translate(code: list):
    """
    This function contains the algorithm needed to translate the code.
    Receives a list that contains the code and returns a translated list
    of that code into 18 bits.
    """
    #Dictionary that will contain the labels of the code, if there's any
    labels = {}
    #List that will save the lines of the translated code
    ensa = []
    #In this for cycle the program will identify all the labels with their
    #respective memory address
    prog_counter = 0
    for line in code:
        prog_counter += 1
        islabel = line.split(":")
        if len(islabel) == 2:
            labels[islabel[0].strip()] = prog_counter

    #In this cycle, the program will iterate the lines of code
    prog_counter = 0
    for line in code:
        #This part of the code will split the line into arguments.
        #Eliminating the labels
        codet = []
        prog_counter += 1
        if ":" in line:
            aux = line.split(":")
            instr = aux[1]
            instr = instr.split(",")
        else:
            instr = line.split(",")
        #This part eliminates the whitespaces around the arguments
        i = 0
        while i < len(instr):
            instr[i] = instr[i].strip()
            i += 1
        #The list instr now have the instruction arguments individualy

        #We make sure that the first argument is a valid mnemonic.
        if instr[0] in MNEMOS:
            codet.append(MNEMOS[instr[0]])
        else:
            print(f"Error en la linea: {prog_counter}, no se reconoce la operacion")
            return 0

        #We make sure that the line of code have the correct number of arguments
        if len(instr) == 2:

            #Validate if the mnemonic is a Jump type, these 3 only receive
            #two arguments.
            if codet[0] in [6, 7]:
                codet.append(0)
                codet.append(0)
                codet.append(labels.get(instr[1]))
            elif codet[0] == 10:
                codet.append(REGS.get(instr[1]))
                codet.append(0)
                codet.append(0)
            else:
                print(f"Faltan argumentos en la linea {prog_counter}")
                return 0

        #We make sure that the line of code has 4 arguments.
        elif len(instr) == 4:
            #If equal to an add, and or or instruction, std1 pattern is added
            if codet[0] in [0, 2, 12]:
                corris = ORDER_APPEND["std1"]
                instr.append("zero")
            #If equal to sll or srl instruction, std2 pattern is added.
            elif codet[0] in [14, 15]:
                corris = ORDER_APPEND["std2"]
                instr.append("zero")
            #If equal to beq or bne instruction, off1 pattern is added.
            elif codet[0] in [4, 5]:
                corris = ORDER_APPEND["off1"]
                REGS["C2"] = (labels.get(instr[3]) - prog_counter) & (2**8-1)
                instr[3] = "C2"
            #If equal to lb or sb instruction, off2 pattern is added.
            elif codet[0] in [11, 13]:
                corris = ORDER_APPEND["off2"]
                REGS["C2"] = eval(instr[2])
                if REGS["C2"] < 0:
                    REGS["C2"] = REGS["C2"] & (2**8-1)
                instr[2] = "C2"
            #If equal to addi or andi instruction, imm0 pattern is added.
            elif codet[0] in [1, 3]:
                corris = ORDER_APPEND["imm0"]
                REGS["C2"] = eval(instr[3])
                if REGS["C2"] < 0:
                    REGS["C2"] = REGS["C2"] & (2**8-1)
                instr[3] = "C2"
            else:
                print(f"Se ha cometido un error en la linea {prog_counter}")
                return 0

            for index in corris:
                codet.append(REGS.get(instr[index]))

        #If instr don't have the enough arguments, then display an error
        else:
            print(f"Error: Revise la linea de codigo {prog_counter}")
            return 0

        #At this point we have a decoded list with the opcodes and
        #values of registers, labels and constants in decimal base.
        #Now the next part is to transform them into binary code strings.
        if codet[0] in [0, 2, 12, 14, 15]:
            patt = BINFORMAT["type1"]
        elif codet[0] in [1, 3, 4, 5, 6, 7, 10, 11, 13]:
            patt = BINFORMAT["type2"]
        else:
            print("No se encuentra el codigo de operacion")

        #In this part, we use a string format to transform decimals into
        #binary words, the lenght of the word is commanded by patt.
        binarytext = ""
        i = 0
        while i < len(patt):
            binf = "{:0" + str(patt[i]) + "b}"
            binarytext += binf.format(codet[i])
            i += 1

        #After the format to binary, is ready to append it to the ensa list
        #Then the cycle is repeated until the lines of code are fully processed
        ensa.append(binarytext)
    #At the end, we return the ensa list, that contains the binary code in
    #string format
    return ensa

#Test code when module is executed as a main project
if __name__ == "__main__":
    #Emulated in lists of the code.
    #These lists have the simulates the returned list by the module that
    #reads files and returns a list with the lines of code of the file.
    CODE_1 = ["addi,x1,x0,1",
              "addi,x2,x0,0x02",
              "addi,x3,x0,0xA0",
              "addi,x4,x0,-1",
              "add,x6,x2,x1",
              "and,x7,x4,x3",
              "or,x5,x3,x4",
              "sll,x3,x3,x1",
              "srl,x3,x3,x1"]
    CODE_2 = ["MAIN:   addi,	x2,	x0,	0x05",
              "        addi,	x3,	x0,	0x01",
              "        addi,	x1,	x0,	0x00",
              "INC:    addi,	x1,	x1,	0x01",
              "        add,	x0,	x0,	x0",
              "        add,	x0,	x0,	x0",
              "        add,	x0,	x0,	x0",
              "        bne,     x1,	x2,	INC",
              "DEC:    addi,	x2,	x2,	-1",
              "        addi,	x0,	x0,	0x00",
              "        addi,	x0,	x0,	0x00",
              "        addi,	x0,	x0,	0x00",
              "        beq,     x2,     x0,	EXIT",
              "        j,	DEC",
              "EXIT:   add, 	x0,	x0,	x0",
              "        add, 	x0,	x0,	x0"]
    CODE_3 = ["MAIN:    addi,	x2,	x0,	0x05",
              "         addi,	x3,	x0,	0x01",
              "         jal,	FUNC",
              "INC:     add, 	x0,	x0,	x0",
              "         add, 	x0,	x0,	x0",
              "         add, 	x0,	x0,	x0",
              "         j,	MAIN",
              "FUNC:    add, 	x0,	x0,	x0",
              "         add, 	x0,	x0,	x0",
              "         add, 	x0,	x0,	x0",
              "         add,	x4,	x3,	x2",
              "         jr,	x7",]

    #The function is called, and then the content of the returned list
    #is printed in the screen.
    EXP = translate(CODE_1)
    print("Codigo1-bin.txt".center(18, "-"))
    for w in EXP:
        print(w)

    EXP = translate(CODE_2)
    print("\n" + "Codigo2-bin.txt".center(18, "-"))
    for w in EXP:
        print(w)

    EXP = translate(CODE_3)
    print("\n" + "Codigo3-bin.txt".center(18, "-"))
    for w in EXP:
        print(w)
