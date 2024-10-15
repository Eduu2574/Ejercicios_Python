# Estructura if
numero = int(input("Introduce un número: "))

if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")

# Estructura match
dia_semana = int(input("Introduce un número del 1 al 3 para el día de la semana: "))

match dia_semana:
    case 1:
        print("Hoy es lunes")
    case 2:
        print("Hoy es martes")
    case 3:
        print("Hoy es miércoles")
    case _:
        print("Número fuera de rango")
