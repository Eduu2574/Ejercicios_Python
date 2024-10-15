def contar_caracteres(cadena1, cadena2):
    # Sumamos las longitudes de las dos cadenas
    longitud_total = len(cadena1) + len(cadena2)
    return longitud_total

def fizz_buzz(cadena1, cadena2):
    contador_numeros = 0  # Inicializamos un contador para los números impresos

    # Iteramos del 1 al 100
    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(cadena1 + cadena2)
        elif numero % 3 == 0:
            print(cadena1)
        elif numero % 5 == 0:
            print(cadena2)
        else:
            print(numero)
            contador_numeros += 1  # Aumentamos el contador si imprimimos un número

    return contador_numeros  # Devolvemos el número de veces que imprimimos un número

# Ejecución de la función fizz_buzz con las cadenas de texto
cadena1 = "Fizz"
cadena2 = "Buzz"
resultado = fizz_buzz(cadena1, cadena2)

# Imprimir cuántas veces se imprimieron números en lugar de texto
print(f"Se han impreso números en lugar de cadenas {resultado} veces.")