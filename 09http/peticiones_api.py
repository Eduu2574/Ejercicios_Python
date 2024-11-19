import requests

# --- Definición de conceptos importantes ---

# **API (Interfaz de Programación de Aplicaciones):**
# Una API (Interfaz de Programación de Aplicaciones) es un conjunto de reglas y herramientas que permiten que diferentes programas se comuniquen entre sí.
# Las APIs permiten que un software acceda a las funciones o datos de otro software sin necesidad de conocer los detalles internos de su implementación.

# **API RESTful:**
# REST (Representational State Transfer) es un estilo de arquitectura de software que utiliza los principios y métodos del protocolo HTTP.
# Una API RESTful es aquella que sigue los principios de REST, utilizando los métodos HTTP como GET, POST, PUT y DELETE, y se basa en recursos accesibles mediante URLs (endpoints).

# **Endpoint:**
# Un endpoint es una URL que se utiliza para acceder a un recurso específico de una API.
# Cada endpoint está asociado a un recurso o conjunto de datos que la API maneja. En el caso de la PokeAPI, un endpoint podría ser el que nos devuelve información sobre un Pokémon específico.
# Por ejemplo, el endpoint `https://pokeapi.co/api/v2/pokemon/35/` nos devuelve información sobre el Pokémon con el ID 35.

# --- Programa para obtener información sobre un Pokémon desde PokeAPI ---

def obtener_informacion_pokemon(nombre_o_id):
    # Aseguramos que el nombre del Pokémon esté en minúsculas
    nombre_o_id = nombre_o_id.lower()

    # Construimos la URL del endpoint para obtener la información del Pokémon
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_o_id}/"

    try:
        # Realizamos la petición GET a la API
        respuesta = requests.get(url)
        
        # Verificamos si la respuesta fue exitosa
        if respuesta.status_code == 200:
            # Convertimos la respuesta JSON en un diccionario de Python
            pokemon = respuesta.json()

            # Mostramos la información del Pokémon
            print(f"Nombre: {pokemon['name'].capitalize()}")
            print(f"ID: {pokemon['id']}")
            print(f"Peso: {pokemon['weight']} hectogramos")
            print(f"Altura: {pokemon['height']} decímetros")
            print(f"Tipos: {', '.join(tipo['type']['name'] for tipo in pokemon['types'])}")
        else:
            # Si la respuesta no fue exitosa, mostramos el código de error
            print(f"Error al obtener los datos del Pokémon. Código de error: {respuesta.status_code}")
    except requests.exceptions.RequestException as e:
        # Si hubo un error en la solicitud, lo mostramos
        print(f"Error al realizar la solicitud: {e}")

# --- Solicitar al usuario el nombre o ID del Pokémon ---

pokemon = input("Introduce el nombre o ID del Pokémon: ").strip()

# Obtener y mostrar la información del Pokémon
obtener_informacion_pokemon(pokemon)
