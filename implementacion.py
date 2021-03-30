from clases.stack import Stack
from clases.verificaSimbolos import verificarSimbolos, parejas, verifica_Caracteres



# Prueba de una pila 
f = Stack()
f.push(4)
f.push(True)
print(f.__dict__)


#prueba de funcion de verificacion de simbolos
print(verificarSimbolos('{{(([][]))}()}'))
print(verificarSimbolos('[{()]'))

print(verifica_Caracteres("(hola)"))
print(verifica_Caracteres('{{(([hola][]))}(hola)}'))
