import json  # Importa la librería json para trabajar con datos en formato JSON
import os

# --- Información sobre JSON ---
# JSON (JavaScript Object Notation) es un formato ligero para el intercambio de datos.
# Se basa en una estructura de pares clave-valor y listas ordenadas.
# 
# **Elementos principales:**
# - Objetos: Representados por llaves {}, contienen pares clave-valor.
# - Listas: Representadas por corchetes [], contienen una secuencia ordenada de valores.
# - Valores: Pueden ser cadenas, números, booleanos, listas, objetos o nulos.
#
# **Características:**
# - Legible por humanos y fácil de interpretar por máquinas.
# - Independiente de lenguaje: JSON es usado ampliamente en programación.
# - Utilizado en APIs, almacenamiento de configuraciones y transmisión de datos.
#
# **Usos principales:**
# - Comunicación entre cliente-servidor en aplicaciones web.
# - Almacenamiento de configuraciones y datos estructurados.
# - Intercambio de datos en sistemas distribuidos.

# --- Programa para crear, mostrar y borrar un archivo JSON ---

# Definimos los datos que queremos almacenar en el archivo JSON.
# Se estructuran como un diccionario de Python, con claves (ej. "Nombre") y valores (ej. "Juan Pérez").
datos = {
    "Nombre": "Eduardo",  # Nombre del usuario como cadena de caracteres.
    "Edad": 18,              # Edad del usuario como entero.
    "FechaNacimiento": "2000-05-15",  # Fecha de nacimiento como cadena de caracteres.
    "Modulos": ["Desarrollo de aplicaciones moviles", "Bases de Datos"]  # Lista de módulos que el usuario estudia.
}

# Especificamos el nombre del archivo JSON donde guardaremos los datos.
archivo_json = "datos.json"

# Abrimos el archivo en modo escritura ("w") para crear o sobrescribir el archivo existente.
# Usamos el bloque "with" para asegurarnos de que el archivo se cierre automáticamente después de escribir.
with open(archivo_json, "w") as archivo:
    # Usamos json.dump() para escribir los datos en el archivo.
    # El parámetro "indent=4" agrega una indentación de 4 espacios para formatear el JSON de forma legible.
    json.dump(datos, archivo, indent=2)

# Imprimimos un mensaje para informar que los datos se guardaron correctamente.
print(f"Archivo '{archivo_json}' creado y datos guardados.")

# Ahora queremos mostrar el contenido del archivo JSON en la terminal.
print("\nContenido del archivo JSON:")

# Abrimos el archivo en modo lectura ("r") para leer su contenido.
with open(archivo_json, "r") as archivo:
    # Usamos json.load() para cargar los datos desde el archivo y convertirlos a un diccionario de Python.
    contenido = json.load(archivo)
    
    # Usamos json.dumps() para convertir el diccionario de Python a una cadena JSON formateada.
    # El parámetro "indent=4" agrega una indentación para hacer el JSON más fácil de leer.
    print(json.dumps(contenido, indent=2))
# Borrar el archivo JSON
"""
if os.path.exists(archivo_json):
    os.remove(archivo_json)
    print(f"\nArchivo '{archivo_json}' eliminado correctamente.")
else:
    print(f"\nNo se pudo encontrar el archivo '{archivo_json}' para eliminarlo.")
"""
