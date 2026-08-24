from nodoCola import NodoCola

class ColaCompras:
    def __init__(self):
        self.frente = None  
        self.final = None   
        self.cantidad = 0

    def esta_vacia(self):
        return self.frente is None

    def encolar(self, producto):
        nuevo_nodo = NodoCola(producto)

        if self.esta_vacia():
            self.frente = nuevo_nodo
            self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo

        self.cantidad += 1

    def desencolar(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")

        nodo_saliente = self.frente
        self.frente = self.frente.siguiente

        if self.frente is None:
            self.final = None

        self.cantidad -= 1
        return nodo_saliente.producto

    def ver_frente(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self.frente.producto

    def tamano(self):
        return self.cantidad

    def mostrar_cola(self):
        if self.esta_vacia():
            print("La cola está vacía")
            return

        actual = self.frente
        while actual is not None:
            print("-", actual.producto)
            actual = actual.siguiente