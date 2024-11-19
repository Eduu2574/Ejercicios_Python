# LIBRERIA INTERNA
import math

numero = 16
raiz_cuadrada = math.sqrt(numero)
print(f"La raíz cuadrada de {numero} es {raiz_cuadrada}")

# LIBRERIA EXTERNA
# Asegúrate de instalar la librería antes de usarla con:
# pip install requests

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
respuesta = requests.get(url)

if respuesta.status_code == 200:
    print("Datos obtenidos exitosamente:")
    print(respuesta.json())
else:
    print(f"Error al obtener datos. Código: {respuesta.status_code}")
