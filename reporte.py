from datetime import date

def generar_reporte(lista, nombre_archivo="reportes.txt"):
    total_inventario = 0
    actual = lista.cabeza

    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("REPORTE DE INVENTARIO DEL SUPERMERCADO\n")
        archivo.write(f"Fecha: {date.today().strftime('%d/%m/%Y')}\n")
        archivo.write("=" * 70 + "\n")

        if actual is None:
            archivo.write("No hay productos registrados.\n")

        while actual is not None:
            producto = actual.producto
            subtotal = producto.precio * producto.existencias
            total_inventario += subtotal
            archivo.write(
                f"{producto.nombre} | {producto.existencias} x "
                f"₡{producto.precio:.2f} = ₡{subtotal:.2f}\n"
            )
            actual = actual.siguiente

        archivo.write("=" * 70 + "\n")
        archivo.write(f"TOTAL POR RECUPERAR: ₡{total_inventario:.2f}\n")

    return total_inventario
