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
        """Eliminar un artículo de la pila"""
        return self._items.pop()

    def peek(self):
        """Obtenga el valor del elemento superior de la pila"""
        return self._items[-1]

    def size(self):
        """Obtenga la cantidad de elementos en la pila"""
        return len(self._items)
