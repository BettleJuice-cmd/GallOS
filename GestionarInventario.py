from ficheros import Articulo
from funciones import aumentar_stock, dar_baja_articulo, listar_articulos
import os

def inventario(usuario):
    os.system("cls")
    print("╔" + "═"*36 + "╗")
    print("║" + "     GESTIÓN DE INVENTARIO          ║")
    print("╠" + "═"*36 + "╣")
    print("║   1) Aumentar Stock                ║")
    print("║   2) Dar de baja Artículo          ║")
    print("║   3) Regresar al menú principal    ║")
    print("╚" + "═"*36 + "╝")
    while True:
        try:
            opcion = int(input("Selecciona una opción: "))
        except ValueError:
            print("Debes ingresar un número.")
            continue
        if opcion == 1:
            aumentar_stock(usuario)
        elif opcion == 2:
            dar_baja_articulo(usuario)
        elif opcion == 3:
            from principal import menu_principal
            menu_principal(usuario)
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")



