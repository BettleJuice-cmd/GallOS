import os
from FicheroUsuario import Usuario

def gestionar_usuarios():
    while True:
        os.system("cls")
        print("="*45)
        print("        GESTIONAR USUARIOS")
        print("="*45)
        print("1) Agregar usuario")
        print("2) Eliminar usuario")
        print("3) Modificar rol de usuario")
        print("4) Listar Usuarios")
        print("5) Volver al menú principal")
        print("-"*45)
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_usuario()
        elif opcion == "2":
            eliminar_usuario()
        elif opcion == "3":
            modificar_rol_usuario()
        elif opcion == "4":
            listar_usuarios()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")
            os.system("pause")

def agregar_usuario():
    os.system("cls")
    print("=== AGREGAR USUARIO ===")
    username = input("Nuevo usuario: ")
    password = input("Contraseña: ")
    usuario = Usuario(username, password, False)
    usuario.guardar()
    print("Usuario registrado exitosamente.")
    os.system("pause")

def eliminar_usuario():
    os.system("cls")
    print("=== ELIMINAR USUARIO ===")
    username = input("Usuario a eliminar: ")
    usuarios = []
    encontrado = False
    try:
        with open("usuarios.dat", "r") as f:
            for linea in f:
                partes = linea.strip().split()
                if partes and partes[0] != username:
                    usuarios.append(linea)
                else:
                    encontrado = True
        with open("usuarios.dat", "w") as f:
            f.writelines(usuarios)
        if encontrado:
            print("Usuario eliminado exitosamente.")
        else:
            print("Usuario no encontrado.")
    except FileNotFoundError:
        print("No hay usuarios registrados.")
    os.system("pause")

def modificar_rol_usuario():
    os.system("cls")
    print("=== MODIFICAR ROL DE USUARIO ===")
    username = input("Usuario a modificar: ")
    usuarios = []
    encontrado = False
    try:
        with open("usuarios.dat", "r") as f:
            for linea in f:
                partes = linea.strip().split()
                if partes and partes[0] == username:
                    nuevo_rol = input("¿Hacer admin? (s/n): ").lower() == "s"
                    usuarios.append(f"{partes[0]} {partes[1]} {nuevo_rol}\n")
                    encontrado = True
                else:
                    usuarios.append(linea)
        with open("usuarios.dat", "w") as f:
            f.writelines(usuarios)
        if encontrado:
            print("Rol modificado exitosamente.")
        else:
            print("Usuario no encontrado.")
    except FileNotFoundError:
        print("No hay usuarios registrados.")
    os.system("pause")

def listar_usuarios():
    try:
        with open("usuarios.dat", "r") as archivo:
            print("\n{:<15} {:<15} {:<10}".format("Usuario", "Contraseña", "Rol"))
            print("-" * 40)
            for linea in archivo:
                partes = linea.strip().split()
                if len(partes) == 3:
                    usuario, contrasena, rol = partes
                    rol_legible = "Admin" if rol == "True" else "Vendedor"
                    print("{:<15} {:<15} {:<10}".format(usuario, contrasena, rol_legible))
                else:
                    print("Línea malformada:", linea)
    except FileNotFoundError:
        print("El archivo 'usuarios.dat' no existe.")
    input("\nPresiona Enter para continuar...")


