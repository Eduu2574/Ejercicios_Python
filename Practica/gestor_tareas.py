import json
from peticiones_http import obtener_cita
import datetime

# Diccionario para almacenar las tareas
tareas = []

# Crear una nueva tarea
def crear_tarea(descripcion, prioridad, fecha_vencimiento):
    tarea = {
        "id": len(tareas) + 1,
        "descripcion": descripcion,
        "fecha_creacion": datetime.date.today().strftime("%Y-%m-%d"),
        "fecha_vencimiento": fecha_vencimiento,
        "prioridad": prioridad,
        "completada": False
    }
    tareas.append(tarea)
    print(f"Tarea '{descripcion}' creada correctamente.\n")

# Mostrar todas las tareas
def mostrar_tareas():
    if tareas:
        for tarea in tareas:
            print(f"Tarea {tarea['id']}: {tarea['descripcion']}, prioridad {tarea['prioridad']}, completada: {tarea['completada']}")
    else:
        print("No hay tareas.\n")

# Marcar tarea como completada
def completar_tarea(id_tarea):
    for tarea in tareas:
        if tarea["id"] == id_tarea:
            tarea["completada"] = True
            print(f"Tarea {id_tarea} completada.\n")
            return
    print(f"Tarea con ID {id_tarea} no encontrada.\n")

# Filtrar tareas por estado (completadas o no completadas)
def filtrar_tareas_completadas(completadas=True):
    filtradas = [tarea for tarea in tareas if tarea["completada"] == completadas]
    if filtradas:
        for tarea in filtradas:
            print(f"Tarea {tarea['id']}: {tarea['descripcion']}, completada: {tarea['completada']}")
    else:
        print(f"No hay tareas {'completadas' if completadas else 'pendientes'}.\n")

# Ordenar tareas por prioridad usando función lambda
def ordenar_por_prioridad():
    tareas.sort(key=lambda tarea: tarea["prioridad"])
    print("Tareas ordenadas por prioridad.\n")

# Programa principal para gestionar el menú de opciones
def menu():
    while True:
        print("\nGestor de Tareas:")
        print("1. Crear tarea")
        print("2. Mostrar todas las tareas")
        print("3. Completar tarea")
        print("4. Filtrar tareas completadas")
        print("5. Ordenar tareas por prioridad")
        print("6. Obtener cita motivacional")  # NUEVA OPCIÓN
        print("7. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            descripcion = input("Descripción de la tarea: ")
            prioridad = int(input("Prioridad (1-5): "))
            fecha_vencimiento = input("Fecha de vencimiento (YYYY-MM-DD): ")
            crear_tarea(descripcion, prioridad, fecha_vencimiento)
        elif opcion == "2":
            mostrar_tareas()
        elif opcion == "3":
            id_tarea = int(input("ID de la tarea a completar: "))
            completar_tarea(id_tarea)
        elif opcion == "4":
            filtrar_tareas_completadas(completadas=True)
        elif opcion == "5":
            ordenar_por_prioridad()
        elif opcion == "6":
            obtener_cita()  # LLAMA A LA FUNCIÓN PARA OBTENER LA CITA
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor elige una opción correcta.\n")

if __name__ == "__main__":
    menu()
