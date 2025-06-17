import os
from Facturar import facturacion
from GestionarArticulo import gestionar
from GestionarInventario import inventario
#Nombre del proyecto: Gestion de Inventario para tienda de sacos 
#autor: Kenneth Zamora, Adolfo Arauz, Joshua nosexd, Andy tampoco sexd
#verion: 1.0 
#fecha: sin fecha aun 


def menu_principal():
    os.system("cls")
    print("*********MENU PRINCIPAL**********")
    print("1............Gestionar Artículos")
    print("2............Gestionar Inventario")
    print("3............Facturación")
    print("4............Salir")

    a=0
    while a!=1:
        os.system("pause")
        opcion = int(input("Selecciona una opción: "))
        if opcion == 1:
            gestionar()
        elif opcion == 2:
            inventario()
        elif opcion == 3:
            facturacion()
        elif opcion == 4:
            exit()
        else:
         print("Opción inválida. Por favor, selecciona una opción válida.")
     
    else:
       print("Hasta la proxima...")
menu_principal()
