opcion=-1
agenda={}
def inserta_contacto(nombre, telefono):
    agenda[telefono]=nombre
    
while opcion!=0:
    opcion=int(input("1. Buscar contacto, 2. Insertar contacto, 3. Actualizar contacto, 4. Eliminar contacto, 5.Mostrar todos los contactos en orden ascendente, 0. Salir"))

    
    match opcion:
        case 1:
            print("Buscar contacto")
        # Buscar contacto
            nombre = input("Introduce el nombre del contacto: ")
            if nombre in agenda:
                    print(f"{nombre}: {agenda[nombre]}")
            else:
                    print("Contacto no encontrado.")
        case 2:
            print("Insertar contacto")
            nombre=input("Introduce un nombre: ")
            telefono=input("Introduce un telefono: ")
            if telefono.isdigit() and len(telefono) == 9:
                inserta_contacto(nombre,telefono)
                print("Contacto añadido correctamente.")
            else:
                print("El teléfono debe contener solo números y tener 9 dígitos.")
            
        case 3:
            print("Actualizar contacto")
            nombre = input("Introduce el nombre del contacto a actualizar: ")
            if nombre in agenda:
                telefono=input("Introduce el nuevo numero de telefono")
                agenda[nombre]=telefono
                print(f"{nombre}: {agenda[nombre]}")
            else:
                    print("Contacto no encontrado.")
        case 4:
            print("Eliminar contacto")
            nombre = input("Introduce el nombre del contacto a eliminar: ")
            if nombre in agenda:
                del agenda[nombre]
            else:
                    print("Contacto no encontrado.")
        case 5:
            print("Mostrar todos los contactos en orden ascendente")
            claves_ordenadas = sorted(agenda.keys())
            print("Claves ordenadas de la agenda:", claves_ordenadas)
        case 6:
            for telefono, nombre in agenda.items():
                print(nombre+":"+telefono)
        case _:
            print("Has introducido una opción incorrecta")
print("Has salido del bucle")