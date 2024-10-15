'''
F-Strings (f"..."): Las f-strings son una forma de interpolación de cadenas de texto en Python, es decir, permiten insertar expresiones (como operaciones matemáticas o variables) dentro de un texto de manera sencilla.

En este caso, dentro de las llaves {}, se evalúa la expresión 8 + 14, que da como resultado 22. Así que el código mostrará:

Suma: 8 + 14 = 22
'''
# 1. Probar la línea de código:
print(f"Suma: 8 + 14 = {8 + 14}")

# 2. Obtener texto del teclado:
nombre = input("Escribe tu nombre: ")
print(f"Hola, {nombre}!")

# 3. Operadores de comparación:
print(5 == 5)  # True
print(3 != 4)  # True
print(10 > 5)  # True

# 4. Operadores lógicos:
print(True and False)  # False
print(True or False)   # True
print(not True)        # False

# 5. Operadores de asignación:
x = 10
x += 5  # x ahora es 15
print(x)

#________________________________________________________________________________________________
# Realizar un pequeño programa llamado calculadora.py que pida por teclado 2 números y 
# muestre por pantalla estas operaciones aritméticas: suma, resta, multiplicación, división, resto:

# Pedimos al usuario dos números
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Realizamos las operaciones aritméticas
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
resto = num1 % num2

# Mostramos los resultados
print(f"Suma: {num1} + {num2} = {suma}")
print(f"Resta: {num1} - {num2} = {resta}")
print(f"Multiplicación: {num1} * {num2} = {multiplicacion}")
print(f"División: {num1} / {num2} = {division}")
print(f"Resto: {num1} % {num2} = {resto}")
