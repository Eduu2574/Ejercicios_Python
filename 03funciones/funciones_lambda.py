# funciones_lambda.py

# Ejemplo 1: Función lambda que suma dos números
suma = lambda x, y: x + y
resultado = suma(5, 10)
print(f"Suma de 5 y 10: {resultado}")

# Ejemplo 2: Función lambda que verifica si un número es par
es_par = lambda num: num % 2 == 0
print(f"¿Es 8 par?: {es_par(8)}")
print(f"¿Es 7 par?: {es_par(7)}")

# Ejemplo 3: Función lambda dentro de la función map() para elevar al cuadrado una lista de números
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print(f"Números elevados al cuadrado: {cuadrados}")

# Ejemplo 4: Función lambda dentro de la función filter() para filtrar números pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Números pares filtrados: {pares}")

# Ejemplo 5: Función lambda con sorted() para ordenar una lista de tuplas por el segundo valor
tuplas = [(1, 'uno'), (2, 'dos'), (3, 'tres')]
tuplas_ordenadas = sorted(tuplas, key=lambda x: x[1])
print(f"Tuplas ordenadas por segundo valor: {tuplas_ordenadas}")