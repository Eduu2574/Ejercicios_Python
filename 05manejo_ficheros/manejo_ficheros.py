import os

# Ruta del archivo (se creará en la raíz del proyecto o donde indiques)
# Ruta absoluta para guardar el archivo
ruta_archivo = r"C:\Users\eduar\Documents\Ejercicios_Python-2\datos.txt"

# Crear el archivo
with open(ruta_archivo, "w") as archivo:
    archivo.write("Nombre: Juan Pérez\n")
    archivo.write("Edad: 30\n")
    archivo.write("Lenguaje de programación usado: Python\n")

print(f"Archivo creado en: {ruta_archivo}")


# Crear el archivo y escribir información
with open(ruta_archivo, "w") as archivo:
    archivo.write("Nombre: Juan Pérez\n")
    archivo.write("Edad: 30\n")
    archivo.write("Lenguaje de programación usado: Python\n")

print(f"Archivo '{ruta_archivo}' creado y datos escritos.\n")

# Leer e imprimir el contenido del archivo
with open(ruta_archivo, "r") as archivo:
    contenido = archivo.read()

print("Contenido del archivo:")
print(contenido)

# Eliminar el archivo
'''
os.remove(ruta_archivo)
print(f"\nArchivo '{ruta_archivo}' eliminado.")
'''

