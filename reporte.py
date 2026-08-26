from datetime import date

def generar_reporte(lista, nombre_archivo="archivo.txt"):
    total_inventario = 0
    actual = lista.cabeza

    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("REPORTE DE VALOR DEL INVENTARIO DEL SUPERMERCADO\n")
        archivo.write(f"Fecha: {date.today().strftime('%d/%m/%Y')}\n")
        archivo.write("=" * 105 + "\n")
        archivo.write(
            f"{'ID':<8}{'PRODUCTO':<25}{'PAÍS DE ORIGEN':<22}"
            f"{'EXISTENCIAS':>12}{'PRECIO':>18}{'SUBTOTAL':>20}\n"
        )
        archivo.write("-" * 105 + "\n")

        if actual is None:
            archivo.write("No hay productos registrados.\n")

        while actual is not None:
            producto = actual.producto
            subtotal = producto.precio * producto.existencias
            total_inventario += subtotal
            archivo.write(
                f"{producto.id_producto:<8}{producto.nombre:<25.25}"
                f"{producto.pais_origen:<22.22}{producto.existencias:>12}"
                f"{f'₡{producto.precio:,.2f}':>18}"
                f"{f'₡{subtotal:,.2f}':>20}\n"
            )
            actual = actual.siguiente

        archivo.write("=" * 105 + "\n")
        archivo.write(f"TOTAL POR RECUPERAR: ₡{total_inventario:,.2f}\n")

    return total_inventario
