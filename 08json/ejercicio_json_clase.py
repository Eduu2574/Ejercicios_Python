import json  # Importa la librería json para trabajar con datos en formato JSON
import os


    



# Especificamos el nombre del archivo JSON donde guardaremos los datos.

def generarJson(nombreArchivo):
    datos = {
        "Nombre": "Eduardo",  # Nombre del usuario como cadena de caracteres.
        "Edad": 18,              # Edad del usuario como entero.
        "FechaNacimiento": "2000-05-15",  # Fecha de nacimiento como cadena de caracteres.
        "Modulos": ["Desarrollo de aplicaciones moviles", "Bases de Datos"]  # Lista de módulos que el usuario estudia.
    }
    
    with open(archivo_json, "w") as archivo:
        json.dump(datos, archivo)
    print(f"Archivo '{nombreArchivo}' creado y datos guardados.")

class Person:
    def __init__(self, nombre, edad, fecha_nacimiento, modulos):
        # Almacenar los atributos en variables de instancia
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.modulos = modulos

    def mostrar_informacion(self):
        # Método para mostrar los atributos de la persona
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Fecha de Nacimiento: {self.fecha_nacimiento}")
        print(f"Módulos: {', '.join(self.modulos)}")
    
archivo_json = "datosPersona.json"

# Generar el fichero JSON con los datos iniciales
generarJson(archivo_json)

# Leer el fichero JSON y convertir los datos en un objeto de la clase Person
if os.path.exists(archivo_json):
    with open(archivo_json, "r") as archivo:
        datos = json.load(archivo)  # Cargar los datos del archivo JSON

    # Crear una instancia de la clase Person usando los datos leídos
    persona = Person(
        nombre=datos["Nombre"],
        edad=datos["Edad"],
        fecha_nacimiento=datos["FechaNacimiento"],
        modulos=datos["Modulos"]
    )

    # Mostrar la información de la instancia de la clase
    print("\nInformación de la persona creada desde el archivo JSON:")
    persona.mostrar_informacion()

    # Eliminar el archivo JSON
    os.remove(archivo_json)
    print(f"\nArchivo '{archivo_json}' eliminado correctamente.")
else:
    print(f"El archivo '{archivo_json}' no existe.")