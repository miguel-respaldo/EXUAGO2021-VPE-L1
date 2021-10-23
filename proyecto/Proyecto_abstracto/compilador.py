from io import open     



def leer_archivo():
    ##nombre= eval(input("escriba el nombre del archivo "))
    try:
         archivo= open("codigo1.txt","r")
    except:
        print ("error 404 not fount")        
    return archivo
        
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
    texto= archivo.replace(' ','')
    texto=texto.lower()
            
    codigos_operaciones = ['add','addi','and','andi','beq','bne','j','jal','jr','lb','or','sb','sll','srl']
    codigos_binarios=['0000','0001','0010','0011','0100','0101','0110','0111','1010','1011','1100','1101','1110','1111']
                     
    for i in range (lineas):
        vista_aux= texto.readline()
        etiqueta=vista_aux.split(':')
        memoria[linea]=etiqueta[0]
               
    for j in range (lineas):
        vista_aux=texto.readline()
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
                                
    def rutina_etiqueta (salida_tex ,memory):               
        valor_negativo = salida_tex.find('-1')
        if valor_negativo!=0:
           valor_etiqueta ='11111111'
           return valor_etiqueta
                    
        hexa=salida_text.find('x')
        if hexa==0:
           imm=int(salida_tex,16)
           imm=int(bin(imm)[2:])
           imm=str(imm)
           return imm
                    
        for c in range(lineas):
            if salida_tex==memory[c]:
               salida=int(bin(c)[2:])
               imm=str(salida)
               break
                        
        return imm              
def escribe_archivo(mensaje_end):
    name = input("ingrese el nombre final que quiere que tenga su archivo binario")
    name+=".bin"
    arch = open(name,"w")
    arch.write(mensaje_end)
    arch.close()
    return
archivo1=[]
mensaje_final1=[]
archivo1 = leer_archivo()
mensaje_final1 = codifica(archivo1)
escribe_archivo(mensaje_final1)
print("archivo generadoro")
            
