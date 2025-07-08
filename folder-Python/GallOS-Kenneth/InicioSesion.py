import os
from FicheroUsuario import login
from principal import menu_principal
from funciones import olvide_contrasena
def iniciar_sesion():
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
            usuario = login()
            if usuario:
                menu_principal(usuario)
                break
        elif opcion == "2":
            olvide_contrasena()
            os.system("pause")
        elif opcion == "3":
            print("Adiós.")
            os.system("pause")
            break
        else:
            print("Opción inválida.")
            os.system("pause")

iniciar_sesion()
