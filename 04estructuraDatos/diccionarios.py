''' Un diccionario es una colección desordenada de pares clave-valor. Es mutable, y las claves deben ser únicas. '''

# Crear un diccionario
mi_diccionario = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Madrid'}

# Inserción
mi_diccionario['teléfono'] = '123456789'  # Añadir una nueva clave-valor
print("Diccionario después de la inserción:", mi_diccionario)

# Actualización
mi_diccionario['edad'] = 26  # Actualizamos el valor de 'edad'
print("Diccionario después de la actualización:", mi_diccionario)

# Borrado
del mi_diccionario['ciudad']  # Elimina la clave 'ciudad'
print("Diccionario después de borrar 'ciudad':", mi_diccionario)

# Ordenación (no tiene sentido ordenar un diccionario, pero podemos mostrar las claves en orden)
claves_ordenadas = sorted(mi_diccionario.keys())
print("Claves ordenadas del diccionario:", claves_ordenadas)
