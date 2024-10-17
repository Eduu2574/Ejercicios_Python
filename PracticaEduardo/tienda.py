# tienda.py
from productos import *
from carrito import *
from ventas import *

def menu():
    while True:
        print("\nBienvenido a la tienda de deportes")
        print("1. Mostrar productos")
        print("2. Agregar producto al carrito")
        print("3. Ver carrito")
        print("4. Realizar compra")
        print("5. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            id_producto = int(input("Introduce el ID del producto a añadir al carrito: "))
            cantidad = int(input("Introduce la cantidad: "))
            agregar_al_carrito(id_producto, cantidad)
        elif opcion == "3":
            mostrar_carrito()
        elif opcion == "4":
            total = calcular_total()
            print(f"Total de la compra: {total}€")
            cliente = input("Introduce el nombre del cliente: ")
            registrar_venta(cliente, carrito, total)
            carrito.clear()  # Vaciar carrito después de la compra
        elif opcion == "5":
            print("Saliendo de la tienda...")
            break
        else:
            print("Opción no válida.")

# Llamar a la función menu cuando se ejecuta el script directamente
if __name__ == "__main__":
    menu()