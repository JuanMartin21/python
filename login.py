

def gestionar_usuarios():
    usuarios = {}

    while True:
        print("Opciones:")
        print("1. Guardar usuario")
        print("2. Iniciar sesión")
        print("3. Imprimir diccionario de usuarios")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre de usuario: ")
            contraseña = input("Ingrese la contraseña: ")
            usuarios[nombre] = contraseña
            print("Usuario guardado exitosamente.")

        elif opcion == "2":
            nombre = input("Ingrese el nombre de usuario: ")
            contraseña = input("Ingrese la contraseña: ")
            if nombre in usuarios and usuarios[nombre] == contraseña:
                print("Inicio de sesión exitoso.")
            else:
                print("Nombre de usuario o contraseña incorrectos.")

        elif opcion == "3":
            print("Diccionario de usuarios:")
            for nombre, contraseña in usuarios.items():
                print("Usuario:", nombre, "Contraseña:", contraseña)

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intenta nuevamente.")


gestionar_usuarios()
