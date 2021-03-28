from clases.stack import Stack
from clases.verificaSimbolos import verificarSimbolos, parejas


# Prueba de una pila 
f = Stack()
f.push(4)
f.push(True)
print(f.__dict__)


#prueba de funcion de verificacion de simbolos
print(verificarSimbolos('{{(([][]))}()}'))
print(verificarSimbolos('[{()]'))
