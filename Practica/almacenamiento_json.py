import json

# Diccionario que se usará para las tareas en gestor_tareas.py
tareas = []

# Guardar las tareas en un archivo JSON
def guardar_tareas_en_json():
    with open("tareas.json", "w") as archivo:
        json.dump(tareas, archivo, indent=4)
    print("Tareas guardadas correctamente en JSON.\n")

# Cargar las tareas desde un archivo JSON
def cargar_tareas_desde_json():
    global tareas
    try:
        with open("tareas.json", "r") as archivo:
            tareas = json.load(archivo)
        print("Tareas cargadas desde el archivo JSON.\n")
    except FileNotFoundError:
        print("No se encontró el archivo JSON. No se ha cargado ninguna tarea.\n")
