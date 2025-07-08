import os

def gestionar(usuario):
    os.system("cls")
    from funciones import registrar_articulo, modificar_articulo, eliminar_articulo,listar_articulos
    print("╔════════════════════════════════════╗")
    print("║  GESTIONAR ARTÍCULO                ║")
    print("╠════════════════════════════════════╣")
    print("║  1) Registrar Artículo             ║")
    print("║  2) Modificar Artículo             ║")
    print("║  3) Eliminar Artículo              ║")
    print("║  4) Listar Articulos               ║")
    print("║  5) Volver al Menú Principal       ║")
    print("╚════════════════════════════════════╝")

    while True:
        try:
            opcion = int(input("selecciona una opcion:"))
        except ValueError:
            print("Debes ingresar un número.")
            continue
        if opcion == 1:
            registrar_articulo(usuario)
        elif opcion == 2:
            modificar_articulo(usuario)
        elif opcion == 3:
            eliminar_articulo(usuario)
        elif opcion == 4:
            listar_articulos(usuario)
        elif opcion == 5:
            from principal import menu_principal
            menu_principal(usuario)
            return
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")
