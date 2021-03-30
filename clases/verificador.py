from clases.stack import Stack
from clases.admonArchivos import Archivos

def verifica_Caracteres(cadena):
    'Funcion que elimina las palabras que estan entre simbolos y retorna una cadena solo con los simbolos'
    caracteres = 'abcdefghijklmnopqrstu'
    simbolo = '({""})'
    CadenaSimbolos = ""
    tamCadena = len(cadena)
    for i in range(0,tamCadena):
        if cadena[i] in caracteres:
            pass
        elif cadena[i] in simbolo:
            CadenaSimbolos += cadena[i]

    return CadenaSimbolos

def Verificador(cadena):
    'Funcion que verifica si los simbolos son pares'
    p = Stack()
    balanceados = True
    indice = 0
    
    while indice < len(cadena) and balanceados:
        simbolo = cadena[indice]
        
        if simbolo in cadena:
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
