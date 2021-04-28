from clases.deque import Deque
from funciones.verificadorSimbolos import VerificadorSimbolos
from funciones.Tokens import tokensTipoVariable, tokensOperadores, tokensReservadas, tokensCondicionales, tokensBibliotecas

def validador( _cola: Deque):
    contador = 1
    cadenaSimbolos = ''
    print("Linea ", contador)
    while not _cola.is_empty():
        _item = _cola.remove_front()
        
        if _item != '\n':
            if tokensOperadores(_item) :
                print("Es un operador: ", _item)

                if _item in '{([])}':
                    cadenaSimbolos += _item
            elif _item[0] == "/" and _item[1] == "/":
                 print("Comentario: ", _item)    
            elif tokensReservadas(_item):
                print("Palabra reservada: ", _item)
            elif tokensCondicionales(_item):
                print("Inicio de bucle o condicional: ", _item)
            elif tokensTipoVariable(_item):
                print("Declaraciond de tipo de variable: ", _item)
            elif tokensBibliotecas(_item):
                print("Incluye la libreria: ", _item)
            elif _item[0] == '"' and _item[-1] == '"':
                print("Cadena: ", _item)
                """
            elif _item[0] == "/" and _item[1] == "*":
                cadena = _item
                _item = _cola.remove_front()
                while _item[-1] != "/" and _item[-2] != "*":
                    cadena += _item
                print("Comentario de bloque: ", cadena)
            """
        else:
            contador +=1
            print("\nLinea ", contador)            
    

    print("simbolos equilibrados", VerificadorSimbolos(cadenaSimbolos))