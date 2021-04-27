"""
Implemetacion de estructura para tokenizar codigos en C
y almacenarlos en una cola.

@autor: Alex Fuentes
fecha: 24/04/2021
"""

#importacion de clases y funciones requeridas
from clases.admonArchivos import Archivos      
from clases.deque import Deque
from funciones.verificadorFinal import seleccionSimbolos, VerificadorSimbolos
from funciones import Validador
import re

cola = Deque()
file = Archivos()
arrLine = []
arrChar = []

documento = 'programa.c'
doc = file.openFile(documento)
palabras = r'(?P<PALABRAS>[a-zA-Z_][a-zA-Z_0-9]*)'
numero = r'(?P<NUMEROS>\d+)'
simbolos = r'(?P<SIMBOLOS>[(){<>""}#:.;,%&=])'
suma = r'(?P<OPERADORES>\+)'
espacio = r'(?P<ESPACIO>[\s+])'
saltoLinea = r'(?P<SALTOLINEA>\n)'
multiplicacion = r'(?P<OPERADORESMUL>\*)'
division = r'(?P<OPERADORESDIV>\/)'
resta = r'(?P<OPERADORESRES>\-)'
patron = re.compile('|'.join([palabras, simbolos, suma, numero, espacio, saltoLinea, resta, multiplicacion, division]))

for linea in doc:
    grupos = patron.scanner(linea)
    for i in range(0, len(linea)):
        try:
            token = grupos.match()
            if token.group() != " ":
                cola.add_front(token.group())
        except:
            break


#print(cola.__dict__)
x = Validador.validator(cola)        

f = seleccionSimbolos(cola)
print("Imprime los simbolos")
print("simbolos: ",f)
print('Verificador de simbolos')
print(VerificadorSimbolos(f))
