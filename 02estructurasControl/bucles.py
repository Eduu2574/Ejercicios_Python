# Bucle for
nombres = ["Juan", "Ana", "Luis"]

for nombre in nombres:
    print(f"Hola, {nombre}!")
    
palabra = "Python"

for letra in palabra:
    print(letra)


# Bucle while
numero = int(input("Introduce un número (0 para salir): "))

while numero != 0:
    print(f"Has introducido el número {numero}")
    numero = int(input("Introduce otro número (0 para salir): "))

print("Has salido del bucle")