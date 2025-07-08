import os

def facturacion(usuario):
    os.system("cls")
    print("*************FACTURACION**************")
    print("1............................Vender")
    print("2..................Imprimir Factura")
    print("3....................Anular Factura")
    print("4..........Volver al menu principal")
    opcion = input("Selecciona una opción: ")

    from funciones import vender, imprimir_factura, anular_factura

    if opcion == "1":
        vender(usuario)
    elif opcion == "2":
        imprimir_factura(usuario)
    elif opcion == "3":
        anular_factura(usuario)
    elif opcion == "4":
        from principal import menu_principal
        menu_principal(usuario)
    else:
        print("Opción inválida.")
        input("Presiona ENTER para continuar...")
        facturacion(usuario)






