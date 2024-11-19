import os

# Ruta del archivo donde se almacenarán los productos
ARCHIVO_VENTAS = "ventas.txt"

# Función para añadir un producto
def añadir_producto():
    nombre = input("Nombre del producto: ").strip()
    cantidad = int(input("Cantidad del producto: "))
    precio = float(input("Precio del producto: "))
    
    with open(ARCHIVO_VENTAS, "a") as archivo:
        archivo.write(f"{nombre},{cantidad},{precio}\n")
    print(f"Producto '{nombre}' añadido correctamente.")

# Función para consultar un producto
def consultar_producto():
    nombre = input("Nombre del producto a consultar: ").strip()
    encontrado = False

    if os.path.exists(ARCHIVO_VENTAS):
        with open(ARCHIVO_VENTAS, "r") as archivo:
            for linea in archivo:
                prod_nombre, prod_cantidad, prod_precio = linea.strip().split(",")
                if prod_nombre.lower() == nombre.lower():
                    print(f"Producto encontrado: Nombre: {prod_nombre}, Cantidad: {prod_cantidad}, Precio: {prod_precio}")
                    encontrado = True
                    break

    if not encontrado:
        print(f"Producto '{nombre}' no encontrado.")

# Función para actualizar un producto
def actualizar_producto():
    nombre = input("Nombre del producto a actualizar: ").strip()
    encontrado = False
    productos = []

    if os.path.exists(ARCHIVO_VENTAS):
        with open(ARCHIVO_VENTAS, "r") as archivo:
            for linea in archivo:
                prod_nombre, prod_cantidad, prod_precio = linea.strip().split(",")
                if prod_nombre.lower() == nombre.lower():
                    nuevo_nombre = input("Nuevo nombre del producto: ").strip()
                    nueva_cantidad = int(input("Nueva cantidad del producto: "))
                    nuevo_precio = float(input("Nuevo precio del producto: "))
                    productos.append(f"{nuevo_nombre},{nueva_cantidad},{nuevo_precio}\n")
                    encontrado = True
                else:
                    productos.append(linea)

        with open(ARCHIVO_VENTAS, "w") as archivo:
            archivo.writelines(productos)

    if encontrado:
        print(f"Producto '{nombre}' actualizado correctamente.")
    else:
        print(f"Producto '{nombre}' no encontrado.")

# Función para borrar un producto
def borrar_producto():
    nombre = input("Nombre del producto a borrar: ").strip()
    encontrado = False
    productos = []

    if os.path.exists(ARCHIVO_VENTAS):
        with open(ARCHIVO_VENTAS, "r") as archivo:
            for linea in archivo:
                prod_nombre, prod_cantidad, prod_precio = linea.strip().split(",")
                if prod_nombre.lower() == nombre.lower():
                    encontrado = True
                else:
                    productos.append(linea)

        with open(ARCHIVO_VENTAS, "w") as archivo:
            archivo.writelines(productos)

    if encontrado:
        print(f"Producto '{nombre}' borrado correctamente.")
    else:
        print(f"Producto '{nombre}' no encontrado.")

# Función para mostrar todos los productos
def mostrar_todos():
    if os.path.exists(ARCHIVO_VENTAS):
        print("\nLista de productos:")
        with open(ARCHIVO_VENTAS, "r") as archivo:
            for linea in archivo:
                prod_nombre, prod_cantidad, prod_precio = linea.strip().split(",")
                print(f"Nombre: {prod_nombre}, Cantidad: {prod_cantidad}, Precio: {prod_precio}")
    else:
        print("No hay productos registrados.")

# Función para calcular la venta total
def calcular_venta_total():
    total = 0.0
    if os.path.exists(ARCHIVO_VENTAS):
        with open(ARCHIVO_VENTAS, "r") as archivo:
            for linea in archivo:
                _, cantidad, precio = linea.strip().split(",")
                total += int(cantidad) * float(precio)
    print(f"Venta total: {total:.2f}")

# Función para calcular venta por producto
def calcular_venta_producto():
    nombre = input("Nombre del producto: ").strip()
    venta = 0.0
    encontrado = False

    if os.path.exists(ARCHIVO_VENTAS):
        with open(ARCHIVO_VENTAS, "r") as archivo:
            for linea in archivo:
                prod_nombre, prod_cantidad, prod_precio = linea.strip().split(",")
                if prod_nombre.lower() == nombre.lower():
                    venta = int(prod_cantidad) * float(prod_precio)
                    encontrado = True
                    break

    if encontrado:
        print(f"Venta total del producto '{nombre}': {venta:.2f}")
    else:
        print(f"Producto '{nombre}' no encontrado.")

# Función para borrar el archivo y salir
def salir():
    if os.path.exists(ARCHIVO_VENTAS):
        os.remove(ARCHIVO_VENTAS)
        print("Archivo de ventas eliminado.")
    print("Saliendo del programa. ¡Hasta luego!")
    exit()

# Función principal para mostrar el menú
def menu():
    while True:
        print("\n--- MENÚ DE VENTAS ---")
        print("1. Añadir producto")
        print("2. Consultar producto")
        print("3. Actualizar producto")
        print("4. Borrar producto")
        print("5. Mostrar todos los productos")
        print("6. Calcular venta total")
        print("7. Calcular venta por producto")
        print("8. Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            añadir_producto()
        elif opcion == "2":
            consultar_producto()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            borrar_producto()
        elif opcion == "5":
            mostrar_todos()
        elif opcion == "6":
            calcular_venta_total()
        elif opcion == "7":
            calcular_venta_producto()
        elif opcion == "8":
            salir()
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el menú principal
if __name__ == "__main__":
    menu()
