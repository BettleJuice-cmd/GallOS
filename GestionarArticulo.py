import os

def gestionar ():
    os.system("cls")
    from funciones import registrar_articulo, modificar_articulo, eliminar_articulo
    print("*********GESTIONAR ARTICULO**********")
    print("********Selecciona una opcion********")
    print("1..................Registrar Articulo")
    print("2..................Modificar Articulo")
    print("3...................Eliminar articulo")
    print("4............Volver al menu principal")

    opcion = 0
    while opcion != 4:
        opcion = int(input("selecciona una opcion:"))
        if opcion == 1:
            registrar_articulo()
        elif opcion == 2:
            modificar_articulo()
        elif opcion == 3:
            eliminar_articulo()
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")
