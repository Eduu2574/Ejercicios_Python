import requests  # Importamos la librería requests para hacer peticiones HTTP

# --- Conceptos importantes sobre HTTP y servicios web ---

# **Servicio web:**
# Un servicio web es una aplicación que ofrece funcionalidad a través de Internet o una red local.
# Permite la comunicación entre diferentes sistemas, por lo general, mediante peticiones y respuestas.
# Los servicios web son fundamentales para el intercambio de información entre aplicaciones distribuidas.

# **RESTful API:**
# Una API (Interfaz de Programación de Aplicaciones) RESTful es un conjunto de reglas que permiten que dos sistemas se comuniquen utilizando HTTP.
# REST (Representational State Transfer) es un estilo de arquitectura que se basa en los principios de HTTP, como el uso de métodos GET, POST, PUT y DELETE.
# Las API RESTful son ampliamente utilizadas en servicios web debido a su simplicidad y flexibilidad.

# **Protocolo HTTP:**
# HTTP (HyperText Transfer Protocol) es un protocolo de comunicación utilizado para la transmisión de información en la web.
# Funciona bajo el modelo cliente-servidor, donde el cliente hace peticiones y el servidor responde con los datos solicitados.
# HTTP es la base para la comunicación en la web, utilizado para acceder a páginas web, realizar envíos de formularios, etc.

# **Peticiones HTTP:**
# Las peticiones HTTP son las solicitudes que hace el cliente (generalmente un navegador o aplicación) al servidor para acceder a un recurso.
# Los métodos más comunes de las peticiones HTTP son:
# - GET: Solicitar datos de un recurso.
# - POST: Enviar datos al servidor, por ejemplo, un formulario.
# - PUT: Actualizar un recurso existente.
# - DELETE: Eliminar un recurso.

# **Respuestas HTTP:**
# Las respuestas HTTP indican el resultado de una petición realizada al servidor. Algunos códigos comunes son:
# - 200 OK: La petición fue exitosa y el servidor ha respondido con los datos solicitados.
# - 404 Not Found: El recurso solicitado no se encuentra en el servidor.
# - 500 Internal Server Error: Hubo un error en el servidor al procesar la petición.

# --- Librería de Python para hacer peticiones HTTP ---

# La librería de Python más comúnmente utilizada para hacer peticiones HTTP es "requests".
# Requests es sencilla de usar y permite realizar todo tipo de peticiones HTTP como GET, POST, PUT, DELETE, etc.

# --- Realizando una petición HTTP GET a una página web ---

# URL de la página web a la que haremos la solicitud
url = "https://www.example.com"
urlError = "https://www.example.com/pagina_inexistente"
urlErrorServidorInterno="https://httpstat.us/500"

# Realizamos la petición GET al servidor para obtener la página web
respuesta = requests.get(url)

# Verificamos si la petición fue exitosa (código de estado 200)
if respuesta.status_code == 200:
    print("Petición exitosa! Mostrando el contenido de la página:\n")
    print(respuesta.text)  # Mostramos el contenido de la página web (código HTML)
else:
    # Si la petición no fue exitosa, mostramos el código de error
    print(f"Error al realizar la petición. Código de error: {respuesta.status_code}")
