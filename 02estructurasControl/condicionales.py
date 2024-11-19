# Estructura if
edad = int(input("Introduce tu edad"))

# Estructura if

if edad < 18:
    print("Eres menor de edad.")
elif edad == 18:
    print("Tienes 18 años.")
else:
    print("Eres mayor de edad.")


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
