import json
import os
from ficheros import Articulo

def aumentar_stock():
    cod = input("Código: ")
    art = Articulo()
    if art.leer(cod):
         print(f"{'Cod':<10}{'Nombre':<20}{'Stock':>5}{'Precio':>15}")
         print("----------------------------------------------------------------------------------------------")
         print(f"{art.cod:<10}{art.nombre:<20}{art.cantidad:>5}{art.precio:>15}{art.cantidad} ")
         print("----------------------------------------------------------------------------------------------")
         cantidad = int(input("Cantidad a aumentar:"))
         art.cantidad += cantidad
         Articulo.modificar(cod, nueva_cant=art.cantidad).guardar()
         print("----------------------------------------------------------------------------------------------")
         print("Articulo actualizado correctamente")
         print("----------------------------------------------------------------------------------------------")
    else:
        print("No existe.")
        print("Volviendo al menu principal...")
        os.system("pause")
        from principal import menu_principal
        menu_principal()


def dar_baja_articulo():
   os.system("cls")
   cod = input("Código: ")
   art = Articulo()
   os.system("cls")
   if art.leer(cod):
         print(f"{'Cod':<10}{'Nombre':<20}{'Cant':>5}{'Precio':>15}")
         print("----------------------------------------------------------------------------------------------")
         print(f"{art.cod:<10}{art.nombre:<20}{art.cantidad:>5}{art.precio:>15}{art.cantidad}")
         print("----------------------------------------------------------------------------------------------")
         cantidad = int(input("cantidad a dar de baja: "))
         art.cantidad -= cantidad
         Articulo.modificar(cod, nueva_cant=art.cantidad)
         nombre = input("Nombre: ")
         cantidad = int(input("Cantidad: "))
         precio = float(input("Precio: "))
         Articulo(cod, nombre, cantidad, precio).guardar()
   else:
        print("Articulo no encontrado")
        print("Volviendo al menu principal...")
        os.system("pause")
        from principal import menu_principal
        menu_principal

def modificar_articulo():
    cod = input("Código a modificar: ")
    art = Articulo()
    if art.leer(cod):
        os.system("cls")
        print("********************************MODIFICAR ARTICULO***********************************")
        print("----------------------------------------------------------------------------------------------")
        print(f"{'Cod':<10}{'Nombre':<20}{'Stock':>5}{'Precio':>15}")
        print("----------------------------------------------------------------------------------------------")
        print(f"{art.cod:<10}{art.nombre:<20}{art.cantidad:>5}{art.precio:>15}{art.cantidad}")
        print("----------------------------------------------------------------------------------------------")
        nuevo_cod = input("Nuevo codigo: (enter = sin cambios) ") or art.cod
        nombre = input("Nuevo nombre (enter = sin cambio): ") or art.nombre
        cant = input("Nueva cantidad:(enter = sin cambios) ") or art.cantidad
        precio = input("Nuevo precio: (enter = sin cambios) ") or art.precio
        Articulo.modificar(
            cod=cod,  
            nuevo_cod=nuevo_cod,  
            nuevo_nombre=nombre,
            nueva_cant=int(cant),
            nuevo_precio=float(precio)
        )
    else:
        print("No existe.")
        input("ENTER para continuar...")
        from principal import menu_principal
        menu_principal()


def listar_articulos():
    Articulo.listar()
    input("ENTER para continuar...")


def registrar_articulo():
   os.system("cls")
   cod = input('Ingrese el codigo del nuevo articulo: ')
   art= Articulo()
   if art.leer(cod):
       print("El código ya existe.")
   else:
       nombre = input("Nombre: ")
       cantidad = int(input("Cantidad: "))
       precio = float(input("Precio: "))
       Articulo(cod, nombre, cantidad, precio).guardar()
       from principal import menu_principal
       menu_principal()

def eliminar_articulo():
   os.system("cls")
   cod = input("Ingrese el codigo del articulo que desea eliminar: ")
   art = Articulo()
   os.system("cls")
   if art.leer(cod):
       print(f"{'Cod':<10}{'Nombre':<20}{'Stock':>5}{'Precio':>15}")
       print("----------------------------------------------------------------------------------------------")
       print(f"{art.cod:<10}{art.nombre:<20}{art.cantidad:>5}{art.precio:>15}{art.cantidad}")
       print("----------------------------------------------------------------------------------------------")
       print("(s) para confirmar la eliminacion del articulo")
       print("(n) para cancelar la eliminacion")
       confirmacion = input("Ingrese su respuesta:")
       print("----------------------------------------------------------------------------------------------")
       if confirmacion == "s":
           print("Articulo eliminado correctamente")
           print("----------------------------------------------------------------------------------------------")
           print("Enter para volver al menu principal")
           os.system("pause")
           Articulo.eliminar(cod)
           from principal import menu_principal
           menu_principal()
       else:
           print("Eliminacion cancelada")
           print("Enter para volver al menu principal")
           os.system("pause")
           from principal import menu_principal
           menu_principal()
   else:
       print("Articulo no encontrado")
       input("ENTER para Volver al menu principal")
       os.system("pause")
       from principal import menu_principal
       menu_principal()
    

def vender():
    import os
    from ficheros import cargar_inventario, guardar_venta
    os.system("cls")
    print("************* VENTA DE ARTÍCULOS **************\n")

    inventario = cargar_inventario()
    if inventario is None:
        print("No hay inventario registrado.")
        os.system("pause")
        from principal import menu_principal
        menu_principal()
        return

    cliente = input("Ingrese el nombre del cliente: ")
   
    lista_venta = []
    total_venta = 0.0

    while True:
        print("\n--- Nuevo artículo a vender ---")
        codigo = input("Ingrese el CÓDIGO del artículo (ENTER para terminar): ")

        if codigo == "":
            break

        articulo = None
        for a in inventario:
            if a["cod"] == codigo:
                articulo = a
                break

        if articulo is None:
            print("❌ Artículo no encontrado. Intente de nuevo.")
            continue
        os.system("cls")
        print("********************Detalles del artículo************************")
        print(f"Nombre: {articulo['nombre']}")
        print(f"Stock disponible: {articulo['cantidad']}")
        print(f"Precio unitario: {articulo['precio']}")
        print("*****************************************************************")

        while True:
            cantidad = int(input("Cantidad a vender: "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor que cero.")
            elif cantidad > articulo["cantidad"]:
                print("No hay suficiente stock. Stock disponible:", articulo["cantidad"])
                os.system("pause")
                print("Enter para volver al menu principal")
                from principal import menu_principal
                menu_principal()
            else:
                break

        subtotal = cantidad * articulo["precio"]
        lista_venta.append({
            "cod": articulo["cod"],
            "nombre": articulo["nombre"],
            "cantidad": cantidad,
            "precio": articulo["precio"],
            "subtotal": subtotal
        })
        articulo["cantidad"] -= cantidad
        total_venta += subtotal
        print(f"✅ Agregado: {cantidad} x {articulo['nombre']} (Subtotal: {subtotal})")

    if not lista_venta:
        print("\nNo se realizó ninguna venta.")
        os.system("pause")
        from principal import menu_principal
        menu_principal()
        return

    
    os.system("cls")
    from datetime import datetime
    iva = round(total_venta * 0.15, 2)
    total_con_iva = round(total_venta + iva, 2)
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

    print(f"*" *27," Factura de venta ","*" *27)
    print(f"Cliente: {cliente}")
    print(f"Fecha: {fecha}")
    print("-" * 70)
    print(f"{'Cod':<10}{'Nombre':<20}{'Cant':>5}{'Precio':>15}{'Subtotal':>15}")
    print("-" * 70)
    for art in lista_venta:
        print(f"{art['cod']:<10}{art['nombre']:<20}{art['cantidad']:>5}{art['precio']:>15.2f}{art['subtotal']:>15.2f}")
    print("-" * 70)
    print(f"{'Subtotal:':>55} {total_venta:>10.2f}")
    print(f"{'IVA (15%):':>55} {iva:>10.2f}")
    print(f"{'TOTAL:':>55} {total_con_iva:>10.2f}")
    print("-" * 70)
    input("Presione ENTER para guardar la factura...")

    guardar_venta(lista_venta, inventario, total_venta, cliente)
    print("Venta registrada correctamente.")


def imprimir_factura():
     while True:
        num = input("Ingrese el número de factura a imprimir: ").strip()
        if not num.isdigit():
            print("Debe ingresar un número válido.")
            continue
        num = int(num)
        break
     from ficheros import mostrar_factura
     mostrar_factura(num)

def anular_factura():
    while True:
        numero_factura = input("Ingrese el número de factura a anular: ").strip()
        if not numero_factura.isdigit():
            print("Debe ingresar un número válido.")
            continue
        num = int(numero_factura)
        break
    os.system("cls")
    print("***************ANULAR FACTURA*******************")
    print(f"Esta seguro que desea anular la factura #{num}")
    print("-------------------------------------------------")
    print("Ingrese (s) para confirmar o (n) para cancelar")
    print("-------------------------------------------------")
    confirmacion = input("ingrese su respuesta:")
    if confirmacion == "s":
        print("Anulando factura...")
        os.system("pause")
        from ficheros import anular_factura_fichero
        anular_factura_fichero(num)
    elif confirmacion == 'n':
        print("Anulacion cancelada volviendo al menu principal...")
        os.system("pause")
        from principal import menu_principal
        menu_principal()
    else: 
        print('Opcion invalida, volviendo al menu principal...')
        os.system("pause")
        from principal import menu_principal
        menu_principal()
