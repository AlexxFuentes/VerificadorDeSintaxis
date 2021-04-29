"""
Implemetacion de estructura para tokenizar codigos en C
y almacenarlos en una cola.

@autor: Alex Fuentes
fecha: 24/04/2021
"""
#importacion de clases y funciones requeridas
from clases.admonArchivos import Archivos      
from clases.deque import Deque
from funciones.validador import validador
import re

cola = Deque()
file = Archivos()
f = '(){<>}#:;=,.%'

documento = 'programa.c'
doc = file.openFile(documento)
#Palabras_Cadenas = r'(?P<CADENAS>([a-zA-Z_][a-zA-Z.]*)|(["/a-zA-Z_]["/a-zA-Z_0-9"/*:%\s]*))'
Palabras_Cadenas = r'(?P<CADENAS>([a-zA-Z_][a-zA-Z.*/]*)|(["/a-zA-Z_]["/a-zA-Z_0-9"/*:%\s]*))'
numero = r'(?P<NUMEROS>[0-9][.]*[0-9]*)'
simbolos = r'(?P<SIMBOLOS>[(){<>}#:,;=%])'
division = r'(?P<DIVISION>\/)'
espacio = r'(?P<ESPACIO>[\s+])'
operadoresLogicos = r'(?P<OPERADORESlOGIVOS>[\&\|\+\-\<\>\+\-\*]+)'

patron = re.compile('|'.join([operadoresLogicos, Palabras_Cadenas, simbolos, division, numero, espacio]))

for linea in doc:
    grupos = patron.scanner(linea)
    for i in range(0, len(linea)):
        try:
            token = grupos.match()
            #print(token.lastgroup, token.group())
            token1 = token.group()
            if token1 != " ":
                if token1[-1].__eq__('\n') and token1[:-1].__ne__(''):                    
                    cola.add_front(token1[:-1])
                    cola.add_front('\n')                       
                else:
                    cola.add_front(token.group())                    
                    
        except:
            break
     
#print("Elementos de la Cola: ", cola.__dict__)
validador(cola)