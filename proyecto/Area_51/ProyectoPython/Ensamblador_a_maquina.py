#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#

"""
Proyecto Python
PROGRAMA PARA SIMULAR COMPILADOR DE ENSAMBLADOR Y MOSTRAR EN LENGUAJE MAQUINA
Elaboro: Gustavo Alejandro Solorio Ramos
Correo: gustavo.solorio@iteso.mx
22 de Octubre 2021
"""
resultado = []          #Se convierte en un arreglo donde se guardan los valores de
                        #salida, posteriormente se imprimen en la variable salida 
instrucciones_txt = []  #Arreglo donde se guardaran las instrucciones del txt
instrucciones = []      #Matriz que guarda las instrucciones 1x1 del txt
temp_etiquetas = []     #Arreglo que divide las etiquetas en las instrucciones
valor_etiqueta= []      #Arreglo donde se guarda el valor de la etiqueta
temp_etiquetas2 = []    #Arreglo donde se guarda el nombre de la etiqueta
inmediato = []          #Arreglo donde se guardan los valores inmediatos, en
                        #complemento a 2
relleno = "00000"       #Se define el relleno para los casos que aplique
rellenojr="00000000000" #Se define el relleno para la instruccion jr
salida=""               #Se declara la variable donde se imprimen las
                        #instrucciones codigo maquina como str

######## Definicion de diccionarios ############
etiquetas= {} #se define un diccionario donde se guardaran las etiquetas y su valor
oppcode = {'add':'0000','addi':'0001','and':'0010','andi':'0011','beq':'0100',\
        'bne':'0101','j':'0110', 'jal':'0111','jr':'1010','lb':'1011','or':'1100',\
        'sb':'1101','sll':'1110','srl':'1111' } #Diccionario de oppcode
Rx={'x0':'000','x1':'001','x2':'010','x3':'011','x4':'100','x5':'101','x6':'110',\
'x7':'111','X0':'000','X1':'001','X2':'010','X3':'011','X4':'100','X5':'101',\
'X6':'110','X7':'111'} #Diccionario de registros
###########################################

############## APERTURA DE ARCHIVOS ###################
""" Guarda el valor de la ruta, solo agregar el nombre del archivo ######
 tiene que estar en el mismo directorio                            """
print("\nPROGRAMA PARA SIMULAR LA COMPILACION DE INSTRUCCIONES EN ENSAMBLADOR")
print("A LENGUAJE MAQUINA\n")
print("Asegurate que los codigos.txt están en el mismo directorio")
ruta = str(input("Escribe el nombre del archivo .txt\n./"))
ruta="./"+ruta

""" Abre el archivo y guarda los datos en un array
instrucciones_txt = [Linea 1 del txt, Linea 2 del txt, ...]"""
archivo= open(ruta,"r")
############# APERTURA DE ARCHIVOS ####################

##### Guarda las instrucciones del .txt, separado por salto de linea #####
instrucciones_txt= archivo.read().strip().replace("\t","").replace(" ","").split("\n")
archivo.close()
##### Guarda las instrucciones del .txt, separado por salto de linea ####


"""
***Busca etiquetas en caso de que existan, las guarda en un diccionario con su
***valor
"""
for j in range (len(instrucciones_txt)): #Recorre el arreglo de instrucciones
    if(":" in instrucciones_txt[j]): #Si detecta un ':' es que hay etiqueta
        valor_etiqueta.append(j+1)   #Guarda el valor donde esta la etiqueta
     #Divide el arreglo en posicion 'j' separando la etiqueta de la instruccion
        temp_etiquetas.extend(instrucciones_txt[j].split(":"))
        temp_etiquetas2.append(temp_etiquetas[j]) #Guarda el nombre de la etiqueta
        del temp_etiquetas[j]
        #La elimina la etiqueta del arreglo, se quedan unicamente#las intruccioens
    else:
        temp_etiquetas.extend(instrucciones_txt[j].split(":"))
"""
*********** Diccionario de etiquetas *********************
"""
for j in range (len(temp_etiquetas2)):
    etiquetas[temp_etiquetas2[j]]=valor_etiqueta[j]
    #Guarda en el diccionario el "Nombre_de_etiqueta":"Valor"
"""
**********************************************************
"""
"""
************* MATRIZ DE INSTRUCCIONES ***************
"""
for j in range (len(instrucciones_txt)):
    instrucciones.append([]) #Agrega una fila al arreglo, se convierte en matriz
    resultado.append([])    #Agrega una fila al arreglo, se convierte en matriz
    instrucciones[j].extend(temp_etiquetas[j].split(","))
    #Guarda cada una de las instrucciones en un elemento de la matriz, usando ','
    #para dividir las instrucciones
    resultado[j].extend(temp_etiquetas[j].split(","))
    #se conservaron ambas matrices, instrucciones y resultado para comparar
    #al final del algoritmo
"""
*******************************************************
"""

"""
***************** Arreglo con los valores inmediatos *******************
"""
for j in range(len(instrucciones_txt)): #Recorre la matriz de instrucciones
    inmediato.append(None)   #Agrega un elemento al arreglo de inmediatos
    if (instrucciones[j][0] == "j") or (instrucciones[j][0]=="jal") or (instrucciones[j][0]== "jr"):
        inmediato[j]= None   #Si detecta una instrucciones de salto, guarda None
    elif (instrucciones[j][3] == "x0")or(instrucciones[j][3] == "x1")or(instrucciones[j][3] =="x2")\
            or (instrucciones[j][3] == "x3") or (instrucciones[j][3] == "x4")or\
            (instrucciones[j][3] =="x5")or(instrucciones[j][3] == "x6")or(instrucciones[j][3] == "x7"):
        inmediato[j]= None #Si detecta un registro, guarda None
    elif (instrucciones[j][0]=="beq")or(instrucciones[j][0]=="bne"):
        inmediato[j] = None  # Si detecta un beq o bne, guarda none
    else:
        inmediato[j]= eval(instrucciones[j][3])
    #Al final, sabemos que el valor sera un nuemero entero, con signo o hexadec.
"""
******************************************************************************
"""
for l in range (len(inmediato)): #Se realiza el complemento a 2 del inmediato
    if (inmediato[l] != None):
        inmediato[l] = (bin(((1 << 8) -1) & inmediato[l])[2:]).zfill(8)

"""              i
instrucciones =[ ,  ,  , ] j
               [ ,  ,  , ]
               [ ,  ,  , ]
"""

"""
**********  Reemplazar elementos de matriz instrucciones por su valor
            correspondiente
"""
for j in range (len(instrucciones_txt)):
    for i in range(len(instrucciones[j])):
        if i == 0:
            resultado[j][i] = oppcode[instrucciones[j][i]]
        elif i==1:
            if (instrucciones[j][0] == "j")or(instrucciones[j][0] == "jal"):
                if instrucciones[j][i] in etiquetas.keys():
                    tag = etiquetas[instrucciones[j][i]]
                else:
                    tag = eval(instrucciones[j][i])
                resultado[j][i] = (bin(((1<<14)-1)& tag)[2:]).zfill(14)
            elif (instrucciones[j][0] == "jr"):
                resultado[j][i] = Rx[instrucciones[j][i]] + rellenojr
            elif (instrucciones[j][0] == "bne") or (instrucciones[j][0] == "beq"):
                resultado[j][i] = Rx[instrucciones[j][i]]
            elif (instrucciones[j][0] == "sll")or (instrucciones[j][0] == "srl"):
                resultado[j][i] = Rx[instrucciones[j][i+2]]
            elif (instrucciones[j][0] == "sb") or (instrucciones[j][0] == "lb"):
                resultado[j][i] = Rx[instrucciones[j][i+2]]
            elif (instrucciones[j][0] == "addi")or(instrucciones[j][0]=="andi"):
                resultado[j][i] = Rx[instrucciones[j][i+1]]
            else:
                resultado[j][i] = Rx[instrucciones[j][i+1]]
        elif i==2:
            if (instrucciones[j][0] == "j")or(instrucciones[j][0] == "jal"):
                x="no hace nada"
            elif (instrucciones[j][0] == "jr"):
                x="no hace nada"
            elif (instrucciones[j][0] == "bne") or (instrucciones[j][0] == "beq"):
                resultado[j][i] = Rx[instrucciones[j][i]]
            elif (instrucciones[j][0] == "sll"):
                resultado[j][i] = Rx[instrucciones[j][i]]
            elif (instrucciones[j][0] == "srl"):
                resultado[j][i] = Rx[instrucciones[j][i-1]]
            elif (instrucciones[j][0] == "sb") or (instrucciones[j][0] == "lb"):
                resultado[j][i] = Rx[instrucciones[j][i-1]]
            elif (instrucciones[j][0] == "addi")or(instrucciones[j][0]=="andi"):
                resultado[j][i] = Rx[instrucciones[j][i-1]]
            else:
                resultado[j][i] = Rx[instrucciones[j][i+1]]
        elif i==3:
            if (instrucciones[j][0] == "j")or(instrucciones[j][0] == "jal"):
                x="no hace nada"
            elif (instrucciones[j][0] == "jr"):
                x="no hace nada"
            elif (instrucciones[j][0] == "bne"):
                if ( j > etiquetas[instrucciones[j][i]]):
                    tag = -1*etiquetas[instrucciones[j][i]]
                else:
                    tag = etiquetas[instrucciones[j][i]]
                resultado[j][i] = (bin(((1<<8)-1)& tag)[2:]).zfill(8)
            elif (instrucciones[j][0] == "beq"):
                tag = etiquetas[instrucciones[j][i]]-(j+1)
                resultado[j][i] = (bin(((1<<8)-1)& tag)[2:]).zfill(8)
            elif (instrucciones[j][0] == "sll"):
                resultado[j][i] = Rx[instrucciones[j][i-2]]+relleno
            elif (instrucciones[j][0] == "srl"):
                resultado[j][i] = Rx[instrucciones[j][i-1]]+relleno
            elif (instrucciones[j][0] == "sb") or (instrucciones[j][0] == "lb"):
                tag = eval(instrucciones[j][i-1])
                resultado[j][i] = (bin(((1<<8)-1)& tag)[2:]).zfill(8)
            elif (instrucciones[j][0] =="addi") or (instrucciones[j][0] =="andi"):
                resultado[j][i] = inmediato[j]
            else:
                resultado[j][i] = Rx[instrucciones[j][i-2]]+relleno
"""
*******************************************************************************
"""

#Borrar las """ para que te muestre el resultado en la terminal
"""
print("****instrucciones***")
for j in range(len(instrucciones_txt)):
    print(instrucciones[j])

print("\n****resultado*****\n")
for j in range(len(instrucciones_txt)):
    print(resultado[j])
"""
for j in range(len(instrucciones_txt)):
    for i in range(len(resultado[j])):
       salida=salida+resultado[j][i]    #Guarda el resultado en una variable
    salida=salida+"\n"                  #de salida
"""
**********Genera el archivo de salida .txt***********
"""
archivo_salida=open('resultado.txt',"w")
archivo_salida.write(salida)
archivo_salida.close()
"""
****************************************************
"""
print("*************************************************************")
print("El resultado se encuentra en resultado.txt en este directorio")
print("*************************************************************")
