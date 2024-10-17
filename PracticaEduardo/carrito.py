# carrito.py

carrito = {}

def agregar_al_carrito(id_producto, cantidad):
    if id_producto in carrito:
        carrito[id_producto]["cantidad"] += cantidad
    else:
        carrito[id_producto] = {"cantidad": cantidad}
    print(f"{cantidad} unidades del producto {id_producto} añadidas al carrito.")

def mostrar_carrito():
    print("Carrito de compras:")
    for id_producto, info in carrito.items():
        print(f"Producto ID: {id_producto} - Cantidad: {info['cantidad']}")

def calcular_total():
    total = 0
    for id_producto, info in carrito.items():
        producto = productos.get(id_producto)
        if producto:
            total += producto["precio"] * info["cantidad"]
    return total
