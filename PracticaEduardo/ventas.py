def calcular_total():
    total = 0
    for item in carrito.values():
        total += item["cantidad"] * item["precio"]
    return total

def registrar_venta(cliente, carrito, total):
    with open("ventas.txt", "a") as archivo_ventas:
        archivo_ventas.write(f"Cliente: {cliente}\n")
        for item in carrito.values():
            archivo_ventas.write(f"{item['nombre']} - Cantidad: {item['cantidad']} - Total: {item['cantidad'] * item['precio']}€\n")
        archivo_ventas.write(f"Total de la venta: {total}€\n\n")
    print(f"Venta registrada para {cliente}.")
