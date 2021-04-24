"""
@autor Alex Fuentes
Fecha: 28/03/2021
"""

from clases.stack import Stack
from clases.deque import Deque

def seleccionSimbolos(_cola: Deque):
    'selecciona los simbolos que extrajo de la cola'
    simbolos = '{()}'
    CadenaSimbolos = ""
    for _item in range(0, _cola.size()):
        caracter = _cola.remove_front()
        if caracter in simbolos:
            CadenaSimbolos += caracter 
    return CadenaSimbolos

def VerificadorSimbolos(cadena):
    'Funcion que verifica si los simbolos son pares'
    p = Stack()
    balanceados = True
    indice = 0
    
    while indice < len(cadena) and balanceados:
        simbolo = cadena[indice]
        
        if simbolo in "([{":
            p.push(simbolo)                             # Agrega un elemento
        else:
            if p.is_empty():                            # Comprueba si la pila está vacía
                balanceados = False
            else:
                tope = p.pop()                          # Extrae (elimina) un elemento
                if not parejas(tope,simbolo):
                    balanceados = False             
        indice = indice + 1

    if balanceados and p.is_empty():
        return True
    else:
        return False


def parejas(simboloApertura, simboloCierre):
    aperturas = "([{"
    cierres = ")]}"
    return aperturas.index(simboloApertura) == cierres.index(simboloCierre)