
from ficheros import Articulo
from funciones import aumentar_stock, dar_baja_articulo, modificar_articulo, listar_articulos


def inventario():
    from principal import menu_principal
    import os
    os.system("cls")
    print("*********GESTIONAR INVENTARIO********")
    print("********SELECCIONA UNA OPCION**********")
    print("1. Aumentar Stock")
    print("2. Dar de baja Artículo")
    print("3. Modificar Artículo")
    print("4. Listar Artículos")
    print("5. regresar al menu principal")
    a=0
    while a!=1:
     opcion = int(input("Selecciona una opción: "))
     if opcion == 1:
        aumentar_stock() 
     elif opcion == 2:
        dar_baja_articulo()
     elif opcion == 3:
        modificar_articulo()
     elif opcion == 4:
        listar_articulos()
     elif opcion == 5:
        return menu_principal()
     else:
        print("Opción inválida. Por favor, selecciona una opción válida.") 
    else:
       print("Hasta la proxima...")
       return menu_principal()

