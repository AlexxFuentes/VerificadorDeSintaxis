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
                'break':"Descrip",
                'case':"Descrip",
                'char':"Descrip",
                'conts':"Descrip",
                'continue':"Descrip",
                'default':"Descrip",
                'do':"Descrip",
                'double':"Descrip",
                'else':"Descrip",
                'enum':"Descrip",
                'extern':"Descrip",
                'float':"Descrip",
                'for':"Descrip",
                'goto':"Descrip",
                'if':"Condicional if",
                'int':"Tipo de dato entero",
                'long':"Descrip",
                'register':"Descrip",
                'return':"Descrip",
                'short':"Descrip",
                'signed':"Descrip",
                'sizeof':"Descrip",
                'static':"Descrip",
                'struct':"Descrip",
                'switch':"Descrip",
                'typedef':"Descrip",
                'union':"Descrip",
                'unsigned':"Descrip",
                'void':"Descrip",
                'volatile':"Descrip",
                'while':"Bucle while"
    }
    if palabra in dict1.keys():
        return True
    else:
        return False


print(tokensC('whi'))
print(tokensCD('whil'))