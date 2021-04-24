"""
w --> Modo escritura. Abre un fichero para escribir contenido posicionándose al principio del fichero, 
    en el caso de no existir el archivo lo crea

r --> Abre un fichero para su lectura. Es el valor predeterminado, el puntero del archivo se pone al 
    principio y nos devuelve un error si el fichero no existe.

a--> Modo añadir. Abre un fichero para añadir contenido posicionándose al final, en el caso de no 
    existir el archivo lo crea.

@Alex Fuentes
fecha: 28/03/2021
"""

class Archivos:
    
    def file_manipulation(self, _nombreArchivo, _modo):
        '''Abrir un archivo en el modo indicado'''
        try:
            with open (_nombreArchivo, _modo) as file:
                return file
        except OSError as err:
            print("Error: {0}".format(err))
            return

    def file_write(self, _nombreArchivo, _texto):
        '''Agrega texto al final del archivo y si no existe lo crea'''
        with open(_nombreArchivo,"w") as file:
            file.write(_texto)

    def add_text(self, _nombreArchivo, _texto):
        '''Agrega texto al final del archivo y si no existe lo crea'''
        with open(_nombreArchivo,"a") as file:
            file.write(_texto)
    
    def read_file(self, _nombreArchivo):
        '''abre un archivo en modo lectura'''
        with open (_nombreArchivo, "r") as file:
            cont = 0
            for linea in file:
                cont += 1
                print(cont,linea)
    
    def openFile(self, _nombreArchivo):
        return open(_nombreArchivo, "r")  