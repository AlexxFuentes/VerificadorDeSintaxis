from clases.deque import Deque
from funciones.verificadorSimbolos import VerificadorSimbolos
from funciones.Tokens import dictTiposVariables, dictCondicionales, dictOperadores, dictReservadas, dictBibliotecas,validadorDict
import re

def validador( _cola: Deque):
    contador = 1
    cadenaSimbolos = ''
    print("Linea ", contador)
    while not _cola.is_empty():
        _item = _cola.remove_front()        
        if _item.__ne__('\n'):
            if validadorDict(_item, dictOperadores) :
                print("Es un operador: ", _item, ": ", dictOperadores.get(_item))

                if _item in '{([])}':
                    cadenaSimbolos += _item
            
            elif _item[0].__eq__("/") and _item[1].__eq__("/"):
                print("Comentario: ", _item)                                
            #elif re.match(r'[/*a-zA-Z*/][/*a-zA-Z*/]', _item):
                #print("Bloque de comentario: ", _item)
            elif validadorDict(_item, dictReservadas):
                print("Palabra reservada: ", _item, ": ", dictReservadas.get(_item))            
            elif validadorDict(_item, dictCondicionales):
                print("Inicio de bucle o condicional: ", _item, ": ", dictCondicionales.get(_item))
            elif validadorDict(_item, dictTiposVariables):
                print("Declaraciond de tipo de variable: ", _item, ": ", dictTiposVariables.get(_item))
            elif validadorDict(_item, dictBibliotecas):
                print("Incluye la libreria: ", _item, ": ", dictBibliotecas.get(_item))
            elif _item[0].__eq__('"') and _item[-1].__eq__('"'):
                print("Cadena: ", _item)   
            elif re.match(r'^\d*[.,]?\d*$', _item):                 
                print("Es una numero: ", _item)
            elif re.match(r'[a-z][a-zA-Z\d_]*$', _item):
                print("Es una variable: ", _item)
            else:
                print("Bloque de comentario: ", _item)
                
        else:
            contador +=1
            print("\nLinea ", contador)            
    
    print("Simbolos: ", cadenaSimbolos)
    print("simbolos equilibrados", VerificadorSimbolos(cadenaSimbolos))