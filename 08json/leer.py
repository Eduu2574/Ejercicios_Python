import json
import os

ruta="datos.json"

with open(ruta, "r") as archivo:
    contenido=json.load(archivo)
    print(json.dumps(contenido))