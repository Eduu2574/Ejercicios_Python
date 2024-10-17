carrito = {}

def agregar_al_carrito(id_producto, cantidad, nombre, precio):
    if id_producto in carrito:
        carrito[id_producto]["cantidad"] += cantidad
    else:
        carrito[id_producto] = {
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio
        }
    print(f"Se han añadido {cantidad} unidades de {nombre} al carrito.")

def mostrar_carrito():
    if not carrito:
        print("El carrito está vacío.")
    else:
        print("\nContenido del carrito:\n")
        for item in carrito.values():
            print(f"{item['nombre']} - Cantidad: {item['cantidad']} - Precio unitario: {item['precio']}€")
