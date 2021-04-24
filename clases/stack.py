"""
@autor: Alex Fuentes
fecha: 24/04/2021
"""
class Stack:
    """Implementación de pila como una lista"""

    def __init__(self):
        """Crear nueva pila """
        self._items = []

    def is_empty(self):
        """Comprueba si la pila está vacía """
        return not bool(self._items)

    def push(self, item):
        """Agregar un elemento a la pila"""
        self._items.append(item)

    def pop(self):
        """ Devuelve el elemento tope y lo elimina de la pila.
        Si la pila está vacía levanta una excepción. """
        try:
            return self._items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")

    def peek(self):
        """Obtenga el valor del elemento superior de la pila"""
        return self._items[-1]

    def size(self):
        """Obtenga la cantidad de elementos en la pila"""
        return len(self._items)