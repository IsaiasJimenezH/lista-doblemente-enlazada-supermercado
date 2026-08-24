from producto import Producto
from listaDoble import ListaDoble
from frecuenciaPaises import mostrar_frecuencia_paises
from reporte import generar_reporte


def leer_entero(mensaje, minimo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Digite un número entero válido.")


def leer_decimal(mensaje, minimo=None):
    while True:
        try:
            valor = float(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Digite un número válido.")


def mostrar_menu():
    print("\n--- SUPERMERCADO ---")
    print("1. Ingresar producto")
    print("2. Eliminar producto")
    print("3. Buscar producto")
    print("4. Mostrar lista")
    print("5. Mostrar lista recursivamente")
    print("6. Generar cola de productos agotados")
    print("7. Mostrar frecuencia de países")
    print("8. Generar reporte")
    print("0. Salir")


def main():
    lista = ListaDoble()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            producto = Producto(
                leer_entero("ID: ", 1),
                input("Nombre: ").strip(),
                leer_decimal("Precio: ", 0),
                input("País de origen: ").strip(),
                leer_entero("Existencias: ", 0),
            )
            if lista.ingresar_producto(producto):
                print("Producto ingresado correctamente.")
            else:
                print("Ya existe un producto con ese ID.")

        elif opcion == "2":
            identificador = leer_entero("ID que desea eliminar: ", 1)
            print("Producto eliminado." if lista.eliminar_producto(identificador)
                  else "Producto no encontrado.")

        elif opcion == "3":
            identificador = leer_entero("ID que desea buscar: ", 1)
            producto = lista.buscar_producto(identificador)
            print(producto if producto is not None else "Producto no encontrado.")

        elif opcion == "4":
            lista.mostrar_productos()

        elif opcion == "5":
            lista.mostrar_productos_recursivo()

        elif opcion == "6":
            print("\nLista de compras (productos con existencias en cero):")
            lista.productos_agotados_a_cola().mostrar_cola()

        elif opcion == "7":
            mostrar_frecuencia_paises(lista)

        elif opcion == "8":
            total = generar_reporte(lista)
            print(f"Reporte generado. Total por recuperar: ₡{total:.2f}")

        elif opcion == "0":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
