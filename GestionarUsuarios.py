import os

usuario_valido = "admin"
contrasena_valida = "1234"

def iniciar_sesion():
    global contrasena_valida
    while True:
        os.system("cls")
        print("="*40)
        print("      BIENVENIDO AL SISTEMA ")
        print("="*40)
        print("           INICIO DE SESIÓN")
        print("-"*40)
        print("1) Iniciar sesión")
        print("2) Olvidé la contraseña")
        print("3) Salir")
        print("-"*40)
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            usuario = input("Usuario: ")
            contrasena = input("Contraseña: ")
            if usuario == usuario_valido and contrasena == contrasena_valida:
                print("\n✅ ¡Inicio de sesión exitoso! Bienvenido,", usuario)
                os.system("pause")
                from principal import menu_principal
                menu_principal()
                break
            else:
                print("\n❌ Usuario o contraseña incorrectos.")
                os.system("pause")

        elif opcion == "2":
            nueva = input("Nueva contraseña: ")
            confirm = input("Confirma contraseña: ")
            if nueva == confirm and nueva != "":
                contrasena_valida = nueva
                print("✔ Contraseña restablecida.")
            else:
                print("❌ Las contraseñas no coinciden o están vacías.")
            os.system("pause")

        elif opcion == "3":
            print("Adiós.")
            os.system("pause")
            break
        else:
            print("Opción inválida.")
            os.system("pause")
iniciar_sesion()

