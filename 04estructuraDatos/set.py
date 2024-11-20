''' Un set es una colección desordenada de elementos únicos. No admite elementos duplicados. '''

# Crear un set
mi_set = {10, 20, 30, 40}

# Inserción
mi_set.add(50)  # Añadir un elemento

print("Set después de insertar 50:", mi_set)

# Actualización (no hay una actualización directa de elementos en un set, porque no hay índices)
# Pero se pueden añadir o eliminar elementos

# Borrado
mi_set.remove(30)  # Elimina el elemento 30
print("Set después de eliminar 30:", mi_set)

# Ordenación (los sets no tienen orden, pero se pueden convertir en una lista y ordenar)
mi_lista_ordenada = sorted(mi_set)  # Ordenamos los elementos
print("Set ordenado (como lista):", mi_lista_ordenada)
