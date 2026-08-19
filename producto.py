class Producto:
    def __init__(self, id_producto, nombre, precio, pais_origen, existencias):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.pais_origen = pais_origen
        self.existencias = existencias

    def __str__(self):
        return (
            f"ID: {self.id_producto} | "
            f"Nombre: {self.nombre} | "
            f"Precio: ₡{self.precio} | "
            f"País: {self.pais_origen} | "
            f"Existencias: {self.existencias}"
        )