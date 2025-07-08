import os
from Facturar import facturacion
from FicheroUsuario import Usuario
from GestionarArticulo import gestionar
from GestionarInventario import inventario
from FicheroUsuario import registrar_admin

#Nombre del proyecto: Gestion de Inventario para tienda de sacos 
#autor: Kenneth Zamora, Adolfo Arauz, Joshua nosexd, Andy tampoco sexd
#verion: 1.0 
#fecha: sin fecha aun 


def menu_principal(usuario):
    while True:
        os.system("cls")
        print("="*45)
        print("        BIENVENIDO AL SISTEMA")
        print("="*45)
        print("             MENÚ PRINCIPAL")
        print("-"*45)
        if usuario.es_admin:
            print("1) Gestionar Artículos")
            print("2) Gestionar Inventario")
            print("3) Facturación")
            print("4) Gestionar usuarios")
            print("5) Salir")
        else:
            print("1) Facturación")
            print("2) Salir")
        print("-"*45)
        try:
            opcion = int(input("Selecciona una opción: "))
        except ValueError:
            print("Debes ingresar un número.")
            os.system("pause")
            continue

        if usuario.es_admin:
            if opcion == 1:
                gestionar(usuario)
            elif opcion == 2:
                inventario(usuario)
            elif opcion == 3:
                facturacion(usuario)
            elif opcion == 4:
                from GestionarUsuarios import gestionar_usuarios
                gestionar_usuarios()
            elif opcion == 5:
                print("Hasta la próxima...")
                os.system("pause")
                exit()
            else:
                print("Opción inválida. Por favor, selecciona una opción válida.")
                os.system("pause")
        else:
            if opcion == 1:
                facturacion(usuario)
            elif opcion == 2:
                print("Hasta la próxima...")
                os.system("pause")
                exit()
            else:
                print("Opción inválida. Por favor, selecciona una opción válida.")
                os.system("pause")

