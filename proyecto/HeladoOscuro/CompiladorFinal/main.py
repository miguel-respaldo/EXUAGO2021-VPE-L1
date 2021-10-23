# Converts MIPS instructions into binary and hex
import os
import sys

from mnemonicos import instr_decode # converts the instruction part of a line of MIPS code
from registerlist import reg_decode # converts the register and immediate parts of the MIPS code

#Function that opens and reads a file
def readFile(fileName):
    fileObj = open(fileName, "r") #opens file with read permission
    words = fileObj.read().split("\n") #splits input after line jump
    fileObj.close() #closes the opened file
    return words 



# the main conversion function

def convert(code):
    code = code.replace(" ", "")
    code = code.replace(",", " ") #replaces comma with space
    code = code.replace("  ", " ") #replaces double space with single space
    code = code.replace("	", "") #replaces tab with an empty character
    code = code.replace(":", " ") #replaces : with a single space
    args = code.split(" ") #splits the arguments after every espace
    instruction = args[0] #instrucion code is stored in pos 0 
   
   #pulls the values of the mnemonics and registers   
    codes = instr_decode(instruction) #Assigns the value of  the opcode
    func_type = codes[0]   #Assigns a function type to be printed according to cases
    reg_values = reg_decode(func_type, instruction, args[1:]) #get the numeric values of the registers
    
    
    if reg_values == None:
        #print("Not a valid MIPS statement")
        print(":( Me declaro incompetente para este caso")
        return
     
    #execution for r-type functions
    if func_type == "r":            
        opcode = '{0:04b}'.format(codes[1])
        rs = '{0:03b}'.format(reg_values[0])
        rt = '{0:03b}'.format(reg_values[1])
        rd = '{0:03b}'.format(reg_values[2])
        filler = '{0:05b}'.format(reg_values[3])
        binary = opcode+rs+rt+rd+filler
        print(binary)
        
    #execution for b-type functions
    elif func_type == "b":
        opcode = '{0:04b}'.format(codes[1])
        rs = '{0:03b}'.format(reg_values[0])
        rt = '{0:03b}'.format(reg_values[1])
        label = '{0:08b}'.format(reg_values[2])
        binary = opcode+rs+rt+label
        print(binary)

    #execution for i-type functions    
    elif func_type == "i":
        opcode = '{0:04b}'.format(codes[1])
        rs = '{0:03b}'.format(reg_values[0])
        rt = '{0:03b}'.format(reg_values[1])
        if reg_values[2] < 0:
            imm = (bin(((1 << 8) -1) & reg_values[2])[2:]).zfill(8)
        else:
            imm = '{0:08b}'.format(reg_values[2]) 
        binary = opcode+rs+rt+imm
        print(binary)
    
    #execution for j-type functions    
    elif func_type == "j":
        opcode = '{0:04b}'.format(codes[1])
        imm = '{0:014b}'.format(reg_values[0])
        binary = opcode+imm
        print(binary)
        
    else:
        print("Its impossible to enter to this print")
        print("If you read this you broke our program")
        return 
           
    return

# main
os.system("clear")
print("Ingresar nombre del archivo y su extension")
print("Ejemplo: codigo1.txt") #Provides an example
filename = input("Archivo:   ") #requests file name input
file1 = readFile(filename)

arguments = []

##########################################################################################
auxiliary = []  #stores 
auxiliary2 = [] #va a guardar num de linea donde va un tag
val_tag = []
tags = {}

for j in range(len(file1)):
	if(":" in file1[j]):
		val_tag.append(j+1)
		auxiliary.extend(file1[j].split(":"))
		auxiliary2.append(auxiliary[j])
		del auxiliary[j]
	else:
		auxiliary.extend(file1[j].split(":"))
	#print(auxiliar[j])

for j in range (len(auxiliary2)):
	tags[auxiliary2[j]] = val_tag[j]	

#print(valor_etiqueta) #contiene pos de las etiquetas 
#print(tags) #contiene las etiquetas

###########################################################################################



#print (type(file1))
#print (type(auxiliar))
#textfile = open("output.txt","w")
print("La salida será un archivo llamado output.txt")

orig_stdout = sys.stdout #guarda console original

file_path = 'output.txt'
sys.stdout = open(file_path, "w") #imprime a archivo

for x in range(len(auxiliary)-1):
    
    file1[x] = convert(auxiliary[x])
    #if (auxiliary[x] != None):
    #	print (auxiliary[x])
    #print("-------------------------------------")

sys.stdout.close()
sys.stdout = orig_stdout #revierte a imprimir en consola

#for i in range(len(file1)-1):
#	print(file1[i])



	



    
    
    
   
