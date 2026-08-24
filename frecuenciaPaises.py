def calcular_frecuencia_paises(lista):
    frecuencias = {} # Diccionario vacio
    actual = lista.cabeza
    while actual is not None:
        pais = actual.producto.pais_origen
        frecuencias[pais] = frecuencias.get(pais, 0) + 1
        actual = actual.siguiente
    return frecuencias


def mostrar_frecuencia_paises(lista):
    frecuencias = calcular_frecuencia_paises(lista)
    if not frecuencias:
        print("No hay productos para calcular frecuencias.")
        return

    print("\nFrecuencia de productos por país:")
    for pais, cantidad in sorted(
        frecuencias.items(), key=lambda elemento: elemento[1], reverse=True
    ):
        print(f"- {pais}: {cantidad} producto(s)")

    mayor = max(frecuencias.values())
    paises_mayor = [pais for pais, cantidad in frecuencias.items() if cantidad == mayor]
    print("País(es) del que se importan más productos:", ", ".join(paises_mayor))
