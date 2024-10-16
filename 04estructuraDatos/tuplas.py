''' Una tupla es similar a una lista, pero es inmutable, lo que significa que no se puede modificar después de su creación. '''

# Crear una tupla
mi_tupla = (10, 20, 30, 40)

# No se puede insertar, actualizar o borrar elementos porque las tuplas son inmutables
# Sin embargo, puedes acceder a sus elementos o convertir la tupla en lista si necesitas modificarla.

# Acceso a elementos
print("Elemento en la posición 1:", mi_tupla[1])

# Ordenar una tupla (convertimos la tupla en una lista para ordenarla)
tupla_ordenada = sorted(mi_tupla)  # Devuelve una lista ordenada
print("Tupla ordenada (como lista):", tupla_ordenada)

# Conversión de tupla a lista
mi_lista = list(mi_tupla)
mi_lista.append(50)  # Ahora podemos modificarla
print("Tupla convertida en lista y modificada:", mi_lista)
