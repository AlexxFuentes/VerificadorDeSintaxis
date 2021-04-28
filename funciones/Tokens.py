# Esta funcion tiene como proposito validar si la palabra recibida, es una palaba reservada
# En el escenario de que sea reservada retornara un True, caso contrario False 

def tokensTipoVariable(_token):
    dictTiposVariables ={
        'int':"Tipo entero",
        'float':"Tipo flotante",
        'double':"tipo de dato para valores decimales",
        'short':"Modificador de rango numerico",
        'long':"modificador de tamaño",
        'signed':"define si una variable puede ser positiva o negativo",
        'list':'Biblioteca',
        'char':"un solo caracter de tipo char",
        'const':"Define una variable constante",
        'unsigned':"indica a la variable que no llevara signo",
    }
    if _token in dictTiposVariables.keys():
        return True
    else:
        return False

def tokensCondicionales(_token):
    dictCondicionales = {
        'if': "Condicional if",
        'else': "parte de la estructura de control if, caso default",
        'do':"instruccion de hacer - mientras",
        'while':"Bucle while",
        'for':"ciclo for",
        'switch':"condicional switch",
        'case':"Define los casos de switch",
        'default':"Define el caso default del switch",
    }
    if _token in dictCondicionales.keys():
        return True
    else:
        return False

def tokensBibliotecas(_token):
    dictBibliotecas ={
        'stdio.h':'Biblioteca',
        'fstream':'Biblioteca',
        'iosfwd':'Biblioteca',
        'iostream':'Biblioteca',
        'math':'Biblioteca',
        'math.h':'Biblioteca',
        'memory':'Biblioteca',
        'numeric':'Biblioteca',
        'ostream':'Biblioteca',
        'queue':'Biblioteca',
        'stdlib':'Biblioteca',
        'string':'Biblioteca',
        'typeinfo':'Biblioteca',
        'vector':'Biblioteca',
        'forward_list':'Biblioteca',
        'list':'Biblioteca',
        'iterator':'Biblioteca',
        'time':'Biblioteca',
        'thread':'Biblioteca',
    }
    if _token in dictBibliotecas.keys():
        return True
    else:
        return False
  
def tokensReservadas(palabra):
    dict1 = { 
        'main': "Inicio de funcion principal",
        'printf': "funcion que da un mensaje en cosola",
        'scanf': "Almacena Valores por el Usuario",
        'include':"Incluye las declaraciones de otroa fichero",
        'auto':" tipos automática",
        'break':"instruccion de salto",                                                
        'continue':"instruccion de salto",                                                              
        'enum':"enumeraciones",
        'extern':"modificador",                
        'goto':"funciona para transferir el control a un punto determinado del código",                            
        'register':"trata a la variable como un registro",
        'return':"instruccion de salto volver",                                
        'sizeof':"es un operador de tiempo de compilacion",
        'static':"almacena la variable en la memoria de manera estatica",
        'struct':"indica que los elementos entre llaves son una estructura tipo struct",            
        'typedef':"asigna un nombre alternativo a tipos existentes",
        'union':"indica que los elementos entre llaves son una estructura tipo union",                
        'void':"no existencia o no atribución de un tipo en una variable o sentencia",
        'volatile':"variable que modifica el programa",
        'new': "crear objeto",
        'delete': "destruir objeto",
        'sizeof': "tamaño de objeto o tipo",
        'typeid': "nombre de tipo",
        'const_cast': "conversion de tipos constante",
        'dynamic_cast': "conversion de tipos dinamica",
        'reinterpret_cast': "conversion de tipos reinterpretada",
        'static_cast': "conversion de tipos estatica", 
        'throw' : "expresion throw",
    }
    if palabra in dict1.keys():
        return True
    else:
        return False

def tokensOperadores(operadores):
    dict2 = { '::': "resolucion de ambito",
              '.' : "seleccion de miembro",
              '->': "otra forma de seleccion de miembro",
              '[]': "subindice de matriz",
              '()': "llamada a funcion",
              '++': "incremento de postfijo",
              '--': "decremento de postfijo",                     
              '~': "complemento de uno",
              '!': "not logico",
              '-': "negacion unaria",
              '+': "suma unaria",
              '&': "direccion de o AND bit a bit",
              '*': "direccionamiento indirecto o multiplicacion", 
              '=': "Asignacion",           
              '.*': "puntero a miembro",
              '->*': "otra forma de puntero a miembro",
              '/' : "division",
              '%' : "modulo",
              '<<': "desplazamiento a la izquierda",
              '>>': "desplazamiento a la derecha",
              '<' : "menor que",
              '>' : "mayor que",
              '<=': "menor o igual que",
              '>=': "mayor o igual que",
              '==': "igualdad",
              '!=': "desigualdad",
              '^' : "Or exclusivo bit a bit",
              '|' : "otro tipo de Or exclusivo",
              '&&': "Y logico",
              '||': "O logico",
              '?:': "condicional",
              '=': "asignacion",
              '*=': "asignacion y multiplicacion",
              '/=': "asignacion y division",
              '%=': "asignacion y modulo",
              '+=': "asignacion y suma",
              '-=': "asignacion y resta",
              '<<=': "asignacion y desplazamiento a la izquierda",
              '>>=': "asignacion y desplazamiento a la derecha",
              '&=' : "asignacion AND bit a bit",
              '|=' : "asignacion y OR inclusivo",
              '^=' : "otro tipo de asignacion y OR inclusivo",              
              ',' : "coma",
              ';': "punto y coma",
              '#': "ayuda a incluir libreria",
              '(': "Apertura de parentesis",
              ')': "Cierre de parentesis",
              '{': "Apertura de parentesis",
              '}': "Cierre de parentesis",
              '[': "Apertura de parentesis",
              ']': "Cierre de parentesis",

    }
    if operadores in dict2.keys():
        return True
    else:
        return False
        