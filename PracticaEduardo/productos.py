# productos.py

productos = {
    1: {"nombre": "Balón de fútbol", "cantidad": 50, "precio": 20.99},
    2: {"nombre": "Raqueta de tenis", "cantidad": 30, "precio": 35.50},
    3: {"nombre": "Zapatillas deportivas", "cantidad": 100, "precio": 60.00},
}

def mostrar_productos():
    print("Productos disponibles:")
    for id_producto, producto in productos.items():
        print(f"{id_producto}. {producto['nombre']} - Precio: {producto['precio']}€ - Stock: {producto['cantidad']}")

def agregar_producto(nombre, cantidad, precio):
    id_producto = len(productos) + 1  # Genera un nuevo ID
    productos[id_producto] = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
    print(f"Producto {nombre} añadido exitosamente.")

def eliminar_producto(id_producto):
    if id_producto in productos:
        del productos[id_producto]
        print(f"Producto con ID {id_producto} eliminado.")
    else:
        print("Producto no encontrado.")

def actualizar_producto(id_producto, nombre=None, cantidad=None, precio=None):
    if id_producto in productos:
        if nombre:
            productos[id_producto]["nombre"] = nombre
        if cantidad:
            productos[id_producto]["cantidad"] = cantidad
        if precio:
            productos[id_producto]["precio"] = precio
        print(f"Producto con ID {id_producto} actualizado.")
    else:
        print("Producto no encontrado.")
