# TareasPython
Repositorio Personal - Gustavo Alejandro Solorio Ramos

Los commits se realizaron a mi repositorio personal, al cual se le invito a ser
colaborador:
https://github.com/GusSolorio/TareasPython

#Algoritmo que simula un compilador de ensamblador a codigo maquina

El algoritmo comienza leyendo el nombre del archivo .txt con las instrucciones
en ensamblador, debe estar en el mismo directorio que el algoritmo.

Enseguida separa las instrucciones en ensamblador de la siguiente manera:
	instrucciones_txt = [linea 1 del .txt, ... , linea n del .txt]

Si el archivo de instrucciones .txt contiene etiquetas, las separa y guarda en
un diccionario, dejando un vector "temp_etiquetas" solo con las instrucciones
	Ejemplo:
	Arrego instrucciones_txt	      Arreglo temp_etiquetas
	[MAIN:addi,x0,x1,0x05] se guarda como [addi,x0,x1,0x05]
	
	La etiqueta y su valor (numero de instruccion o linea del .txt) se
	guardan en un diccionario}
	
	etiquetas = {'MAIN':'1, ...}

Se divide el arreglo temp_etiquetas cada que encuentra ',', generando una matriz
llamada instrucciones donde se guardan todas las del archivo .txt
	
	instrucciones = [addi,x0,x1,0x05]
			[    ,  ,  ,    ]

Se guardan los valores inmediatos gracias a la funcion "eval" en un 
arreglo "inmediato = []" para despues hacerles el complemento a 2

Finalmente se remplazan los elementos de la matriz resultado = [[],...] con la
interpretacion a codigo máquina, se guardan la interpretacion en la variable
"salida" y se genera el archivo "resultado.txt" donde se muestra el codigo
maquina.

NOTA: el archivo resultado esta en el mismo directorio que el algoritmo.
