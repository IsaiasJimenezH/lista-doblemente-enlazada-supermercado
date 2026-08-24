from nodo import Nodo
from colaCompras import ColaCompras

class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def ingresar_producto(self, producto):
        if self.buscar_producto(producto.id_producto) is not None:
            return False

        nuevo_nodo = Nodo(producto)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo

        return True


    def eliminar_producto(self, id_producto):
        actual = self.cabeza

        while actual is not None:
            if actual.producto.id_producto == id_producto:

                if actual.anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    actual.anterior.siguiente = actual.siguiente

                if actual.siguiente is None:
                    self.cola = actual.anterior
                else:
                    actual.siguiente.anterior = actual.anterior

                return True
            actual = actual.siguiente

        return False

    def buscar_producto(self, id_producto):
        actual = self.cabeza

        while actual is not None:
            if actual.producto.id_producto == id_producto:
                return actual.producto

            actual = actual.siguiente

        return None

    def mostrar_productos(self):
        if self.cabeza is None:
            print("No hay productos en la lista")
            return

        actual = self.cabeza

        while actual is not None:
            print("-", actual.producto)
            actual = actual.siguiente

    def mostrar_productos_recursivo(self, nodo):
        if nodo is None:
            return
        print("-", nodo.producto)
        self.mostrar_productos_recursivo(nodo.siguiente)

    def productos_agotados_a_cola(self):
        cola_compras = ColaCompras()
        actual = self.cabeza
        while actual is not None:
            if actual.producto.existencias == 0:
                cola_compras.encolar(actual.producto)
            actual = actual.siguiente
        return cola_compras
