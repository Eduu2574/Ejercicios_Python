# ventas.py
from datetime import datetime

ventas = []

def registrar_venta(cliente, carrito, total):
    venta = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cliente": cliente,
        "productos": carrito,
        "total": total,
    }
    ventas.append(venta)
    print(f"Venta registrada por un total de {total}€.")
