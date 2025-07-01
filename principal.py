import os
from Facturar import facturacion
from GestionarArticulo import gestionar
from GestionarInventario import inventario
#Nombre del proyecto: Gestion de Inventario para tienda de sacos 
#autor: Kenneth Zamora, Adolfo Arauz, Joshua nosexd, Andy tampoco sexd
#verion: 1.0 
#fecha: sin fecha aun 


def menu_principal():
    while True:
        os.system("cls")
        print("="*45)
        print("        BIENVENIDO A SACOS WILLY")
        print("="*45)
        print("             MENÚ PRINCIPAL")
        print("-"*45)
        print("1) Gestionar Artículos")
        print("2) Gestionar Inventario")
        print("3) Facturación")
        print("4) Salir")
        print("-"*45)
        try:
            opcion = int(input("Selecciona una opción: "))
        except ValueError:
            print("Debes ingresar un número.")
            os.system("pause")
            continue

        if opcion == 1:
            gestionar()
        elif opcion == 2:
            inventario()
        elif opcion == 3:
            facturacion()
        elif opcion == 4:
            print("Hasta la próxima...")
            os.system("pause")
            exit()
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")
            os.system("pause")