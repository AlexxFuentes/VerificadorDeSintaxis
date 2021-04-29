"""
@autor: Alex Fuentes
fecha: 24/04/2021
"""
from clases.stack import Stack

class Deque:
    """Implementación de la cola como una lista"""

    def __init__(self):
        """crea una nueva cola"""
        self._items = []

    def is_empty(self):
        """verifica si la cola está vacía."""
        return not bool(self._items)

    def add_front(self, item):
        """Agregar un elemento al frente de la cola"""
        self._items.append(item)

    def add_rear(self, item):
        """Agrega un elemento al final de la cola."""
        self._items.insert(-1, item)

    def remove_front(self):
        """ Elimina el primer elemento de la cola y devuelve su
        valor. Si la cola está vacía, levanta ValueError. """
        try:
            return self._items.pop(0)
        except:
            raise ValueError("La cola está vacía")         
        
    def remove_rear(self):
        """Quitar un elemento de la parte trasera de la cola."""
        return self._items.pop(-1)

    def size(self):
        """Obtener la cantidad de elementos en la etiqueta"""
        return len(self._items)
