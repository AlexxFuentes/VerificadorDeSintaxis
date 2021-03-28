from clases.stack import Stack

def verificarSimbolos(cadenaSimbolos):
    p = Stack()
    balanceados = True
    indice = 0
    while indice < len(cadenaSimbolos) and balanceados:
        simbolo = cadenaSimbolos[indice]
        if simbolo in "([{":
            p.push(simbolo)                             # Agrega un elemento
        else:
            if p.is_empty():
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

"""
print(verificarSimbolos('{{(([][]))}()}'))
print(verificarSimbolos('[{()]'))
"""