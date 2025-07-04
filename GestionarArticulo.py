import os

def gestionar ():
    os.system("cls")
    from funciones import registrar_articulo, modificar_articulo, eliminar_articulo
    print("╔════════════════════════════════════╗")
    print("║  GESTIONAR ARTÍCULO                ║")
    print("╠════════════════════════════════════╣")
    print("║  1) Registrar Artículo             ║")
    print("║  2) Modificar Artículo             ║")
    print("║  3) Eliminar Artículo              ║")
    print("║  4) Volver al Menú Principal       ║")
    print("╚════════════════════════════════════╝")

    opcion = 0
    while opcion != 5:
        opcion = int(input("selecciona una opcion:"))
        if opcion == 1:
            registrar_articulo()
        elif opcion == 2:
            modificar_articulo()
        elif opcion == 3:
            eliminar_articulo()
        elif opcion == 4:
            from principal import menu_principal
            menu_principal
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")
            return gestionar()
