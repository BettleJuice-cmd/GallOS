
from ficheros import Articulo
from funciones import aumentar_stock, dar_baja_articulo, listar_articulos
import os

def inventario():
    
    os.system("cls")
    print("╔" + "═"*36 + "╗")
    print("║" + "     GESTIÓN DE INVENTARIO          ║")
    print("╠" + "═"*36 + "╣")
    print("║   1) Aumentar Stock                ║")
    print("║   2) Dar de baja Artículo          ║")
    print("║   3) Listar Artículos              ║")
    print("║   4) Regresar al menú principal    ║")
    print("╚" + "═"*36 + "╝")
    a=0
    while a!=1:
     opcion = int(input("Selecciona una opción: "))
     if opcion == 1:
         aumentar_stock() 
     elif opcion == 2:
         dar_baja_articulo()
     elif opcion == 3:
         listar_articulos()
     elif opcion == 4:
         from principal import menu_principal
         menu_principal()
     else:
        print("Opción inválida. Por favor, selecciona una opción válida.") 
    else:
       print("Hasta la proxima...")
       menu_principal()



