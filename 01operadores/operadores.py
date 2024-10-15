'''
F-Strings (f"..."): Las f-strings son una forma de interpolación de cadenas de texto en Python, es decir, permiten insertar expresiones (como operaciones matemáticas o variables) dentro de un texto de manera sencilla.

En este caso, dentro de las llaves {}, se evalúa la expresión 8 + 14, que da como resultado 22. Así que el código mostrará:

Suma: 8 + 14 = 22
'''
# Este código realiza una suma y la imprime usando f-strings
print(f"Suma: 8 + 14 = {8 + 14}")

# Pedir al usuario que ingrese su nombre
nombre = input("Escribe tu nombre: ")

# 2 Formas de mostrar el nombre en pantalla
print(f"Hola, {nombre}!")
print("Hola, "+nombre+"!")

# Realizar un pequeño programa llamado calculadora.py que pida por teclado 2 números y 
# muestre por pantalla estas operaciones aritméticas: suma, resta, multiplicación, división, resto.
numero1=float(input("Introduce el numero 1:"))
numero2=float(input("Introduce el numero 2:"))

suma=numero1+numero2
resta=numero1-numero2
multiplicacion=numero1*numero2
division=numero1/numero2
resto=numero1%numero2
print(suma)