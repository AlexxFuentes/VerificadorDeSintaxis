# Esta funcion tiene como proposito validar si la palabra recibida, es una palaba reservada
# En el escenario de que sea reservada retornara un True, caso contrario False 
def tokensC(palabra):
    tokens = ["auto","break","case","char","const","continue","default","do","double","else","enum","extern","float","for","goto","if","int","long","register","return","short","signed","sizeof","static","struct","switch","typedef","union","unsigned","void","volatile","while"]
    if palabra in tokens:
        return True
    else:
        return False
  
def tokensCD(palabra):
    dict1 = { 'auto':" tipos automática",
                'break':"instruccion de salto",
                'case':"sentencia",
                'char':"un solo caracter de tipo char",
                'const':"tipo de correctitud",
                'continue':"instruccion de salto",
                'default':"condicional default",
                'do':"instruccion de hacer - mientras",
                'double':"tipo de dato para valores decimales",
                'else':"parte de la estructura de control if para tomar decisiones",
                'enum':"enumeraciones",
                'extern':"modificador",
                'float':"tipo de dato punto flotante",
                'for':"ciclo for",
                'goto':"funciona para transferir el control a un punto determinado del código",
                'if':"Condicional if",
                'int':"Tipo de dato entero",
                'long':"modificador de tamaño",
                'register':"trata a la variable como un registro",
                'return':"instruccion de salto volver",
                'short':"modificador de tamano2",
                'signed':"define si una variable puede ser positiva o negativo",
                'sizeof':"es un operador de tiempo de compilacion",
                'static':"almacena la variable en la memoria de manera estatica",
                'struct':"indica que los elementos entre llaves son una estructura tipo struct",
                'switch':"condicional switch",
                'typedef':"asigna un nombre alternativo a tipos existentes",
                'union':"indica que los elementos entre llaves son una estructura tipo union",
                'unsigned':"indica a la variable que no llevara signo",
                'void':"no existencia o no atribución de un tipo en una variable o sentencia",
                'volatile':"variable que modifica el programa",
                'while':"Bucle while"
    }
    if palabra in dict1.keys():
        return True
    else:
        return False


print(tokensC('whi'))
print(tokensCD('whil'))