'''Una lista es una estructura de datos mutable en Python que puede contener elementos de diferentes tipos. '''

# Crear una lista con algunos elementos
mi_lista = [10, 20, 30, 40, 50]

# Inserción
mi_lista.append(60)  # Añadir un elemento al final de la lista
mi_lista.insert(2, 25)  # Insertar el valor 25 en la posición 2
print("Lista después de inserciones:", mi_lista)

# Actualización
mi_lista[1] = 15  # Actualizamos el valor en la posición 1 (de 20 a 15)
print("Lista después de actualización:", mi_lista)

# Borrado
mi_lista.remove(40)  # Eliminamos el valor 40 de la lista
print("Lista después de eliminar 40:", mi_lista)
elemento_eliminado = mi_lista.pop(3)  # Eliminamos el valor en la posición 3
print("Elemento eliminado:", elemento_eliminado)

# Ordenación
mi_lista.sort()  # Ordenamos la lista en orden ascendente
print("Lista ordenada:", mi_lista)
