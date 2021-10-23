
#Proyecto final Ensamblador del equipo "Proyecto_abstracto" con Alba Castro y
#Jesus Apodaca.
#Este programa lee como entrada un archivo .txt que contiene las instrucciones
#de nmemonicos y registros a interpretar en el archivo que se genera en lenguaje
#maquina .bin

#from io import open     


#Funcion para identificar y abrir el archivo a codificar, con extension .txt
def leer_archivo ():
    
    #try:
    f = open("codigo1.txt",'r')
    archivo = f.read() 
    #except:
     #   print ("error 404 not fount") 
    #print("El archivo que se va a codificar es" , nombre)
    f.close()
    return archivo

#Funcion que realiza el objetivo de programa
def codifica(archivo):
    mensaje_final=''
   # lineas=0
   # contenido = archivo.read
   # coli = contenido.split("\n")
   # for d in coli:
    #    if d:
     #       counter +=1

    lineas=archivo.count("\n")
    lineas+=1
    archivo = archivo.replace(' ','')
    archivo = archivo.lower()
   # file=open(
#matrices para identificar y escribir  los opcodes
    codigos_operaciones = ['add','addi','and','andi','beq','bne','j','jal','jr','lb','or','sb','sll','srl']
    codigos_binarios=['0000','0001','0010','0011','0100','0101','0110','0111','1010','1011','1100','1101','1110','1111']
    
    archivox = open("codigo1.txt",'r')
    memoria=[] 
    for i in range (lineas):
        vista_aux= archivox.readline()
        etiquetax = vista_aux.find(':')
        if etiquetax != 0:
            etiqueta=vista_aux.split(':')
            memoria[i]=etiqueta[0]

               
    for j in range (lineas):
        vista_aux=archivox.readline()
        ensamblar=vista_aux
        x1=vista_aux.find(':')
        if x1!=0:
           cuerpo_texto=vista_aux.split(':')
           ensamblar=cuerpo_texto[1]
           salida_texto=ensamblar.split(',')    
           for a in range(14):
               if (salida_texto[0]==codigos_operaciones[a-1]):
                  co_ope=codigos_binarios[a-1]
        rt=registros(salida_texto[2])
        rd=registros(salida_texto[1])
        imm=rutina_etiqueta(salida_texto[3],memoria)    
        if salida_texto[0]=='j' or salida_texto[0] =='jal':
           imm=rutina_etiqueta(salida_texto[1],memoria)
           rt='000'
           rd='000'
              
        if salida_texto[0]=='jr':
           imm='00000111'
           rt='000'
           rd='000'
       
        mensaje_final+=co_ope        
        mensaje_final+=' '
        mensaje_final+=rt
        mensaje_final+=' '
        mensaje_final+=rd
        mensaje_final+=' ' 
        mensaje_final+=imm
        mensaje_final+='\n'                                
    return mensaje_final


def registros(salida_text):
        register=int(salida_tex,16)
        register=int(bin(imm)[2:])
        register=str(imm)
        return imm           

#Funcion para escribir numeros negativos que puedan estar como registros    
def rutina_etiqueta (salida_tex ,memory):               
        valor_negativo = salida_tex.find('-1')
        if valor_negativo!=0:
           valor_etiqueta ='11111111'
           return valor_etiqueta
#Se identifican registros en formato hexadecimal para escribirlos en binario de 16 bits                    
        hexa=salida_text.find('x')
        if hexa==0:
           imm=int(salida_tex,16)
           imm=int(bin(imm)[2:])
           imm=str(imm)
           return imm
        #ultimo registro, imm            
        for c in range(lineas):
            if salida_tex==memory[c]:
               salida=int(bin(c)[2:])
               imm=str(salida)
               break
                        
        return imm

#Funcion para crear y escribir el archivo a mostrar como implementacion del programa
def escribe_archivo(mensaje_final):
    
    f = open("codigo1.bin",'w')
    f.write(mensaje_final)
    f.close()
    return

archivo1=[]
mensaje_final1=[]
archivo1 = leer_archivo()
mensaje_final1 = codifica(archivo1)
escribe_archivo(mensaje_final1)
print("Archivo generado")


if __name__ == "__main__":
    main()
