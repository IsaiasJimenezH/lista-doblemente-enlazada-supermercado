from colaCompras import ColaCompras
from producto import Producto
from listaDoble import ListaDoble


def main():
    print("Iniciando prueba...")

    lista = ListaDoble()

    lista.ingresar_producto(
        Producto(1, "Arroz", 1500, "Costa Rica", 10)
    )

    lista.ingresar_producto(
        Producto(2, "Atún", 1200, "Ecuador", 0)
    )

    print("\n LISTA ORIGINAL ")
    lista.mostrar_productos()

    print("\nBUSCAR PRODUCTO 2 ")
    producto = lista.buscar_producto(2)

    if producto is not None:
        print("Encontrado:", producto)
    else:
        print("Producto no encontrado.")

    print("\n=== ELIMINAR PRODUCTO 1 ===")

    if lista.eliminar_producto(1):
        print("Producto eliminado correctamente.")
    else:
        print("Producto no encontrado.")

    print("\n LISTA ACTUALIZADA ")
    lista.mostrar_productos()

    print("\n LISTA ACTUALIZADA RECURSIVA ")
    lista.mostrar_productos_recursivo(lista.cabeza)


    print("Prueba de la cola :")

    cola = ColaCompras()
    cola.encolar(Producto(3, "Leche", 800, "Costa Rica", 5))
    cola.encolar(Producto(4, "Pan", 500, "Costa Rica",  20))
    print("\nCola después de encolar productos:")
    cola.mostrar_cola() 

if __name__ == "__main__":
    main()