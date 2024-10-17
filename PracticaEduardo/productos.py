import requests

# URL base de la API de Decathlon (simulada para el ejemplo)
BASE_URL = "https://pokeapi.co/api/v2/pokemon/ditto"

def obtener_productos():
    url = f"{BASE_URL}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()  # Retorna los datos como un diccionario
        else:
            print(f"Error: {response.status_code}")
    except Exception as e:
        print(f"Error al realizar la petición HTTP: {e}")
        return []

def mostrar_productos():
    productos = obtener_productos()
    print("\nProductos disponibles en la tienda:\n")
    for producto in productos:
        print(f"ID: {producto['id']} - {producto['name']} - Precio: {producto['price']}€")
