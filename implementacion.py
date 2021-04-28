"""
Implemetacion de estructura para tokenizar codigos en C
y almacenarlos en una cola.

@autor: Alex Fuentes
fecha: 24/04/2021
"""

#importacion de clases y funciones requeridas
from clases.admonArchivos import Archivos      
from clases.deque import Deque, copiaCola
from funciones.verificadorSimbolos import seleccionSimbolos, VerificadorSimbolos
from funciones.validador import validador
import re

cola = Deque()
file = Archivos()

documento = 'programa.c'
doc = file.openFile(documento)
#palabras = r'(?P<PALABRAS>[a-zA-Z_][a-zA-Z_0-9]*)' *.,:%\s
Cadenas = r'(?P<PALABRAS>["/a-zA-Z_"]["/a-zA-Z_0-9"*.:%\s]*)'
numero = r'(?P<NUMEROS>\d+)'
simbolos = r'(?P<SIMBOLOS>[(){<>}#:;=,.%&/])'
suma = r'(?P<OPERADORES>\++)'
resta = r'(?P<RESTA>\-+)'
multiplicacion = r'(?P<MULTIPLICACION>\*)'
division = r'(?P<DIVISION>\/+)'
espacio = r'(?P<ESPACIO>[\s+])'
#saltoLinea = r'(?P<SALTOLINEA>\n)'
Logico =  r'(?P<LOGIVO>\&+)'


patron = re.compile('|'.join([Logico, Cadenas, simbolos, suma, resta, multiplicacion, division, numero, espacio]))

for linea in doc:
    grupos = patron.scanner(linea)
    for i in range(0, len(linea)):
        try:
            token = grupos.match()
            #print(token.lastgroup, token.group())
            """
            print(s[-1])
            print(s[:-1])
            """
            token1 = token.group()
            if token1 != " ":
                if token1[-1] == '\n' and token1[:-1] != '':                    
                    cola.add_front(token1[:-1])
                    cola.add_front('\n')
                else:
                    cola.add_front(token.group())
        except:
            break

      
print("Elementos de la Cola: ", cola.__dict__)
validador(cola)