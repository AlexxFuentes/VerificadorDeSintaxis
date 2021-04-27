from clases.stack import Stack
from clases.deque import Deque
from .Tokens import tokensCD


def validator( cola: Deque ):
    '''Metodo para sacar los items de la cola'''
    simbolos = ['::','.','->','[]','()','++','--','~','!','-','+','&','*','#','<','>','.*','->*','/','%','<<','>>','<','>','<=','>=',
              '==','!=','^','|','&&','||','?:','=','*=','/=','%=','+=','-=','<<=','>>=','&=','|=','^=','throw',','
              ]
    colaSize = cola.size()

    for itemCola in range( 0 , colaSize ):
        data = cola.remove_front()
        print(data)
        if ( data in simbolos ):
            print('Simbolo')
        elif (data == '\n'):
            print('salto de linea')   
        elif(tokensCD(data)):
            print('Palabra Reservada')      

