import json
import os
from ficheros import Articulo
import random
import smtplib  
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

def aumentar_stock(usuario):
    cod = input("Código: ")
    art = Articulo()
    if art.leer(cod):
        print(f"{'Cod':<10}{'Nombre':<20}{'Stock':>5}{'Precio':>15}")
        print("----------------------------------------------------------------------------------------------")
        print(f"{art.cod:<10}{art.nombre:<20}{art.cantidad:>5}{art.precio:>15}{art.cantidad} ")
        print("----------------------------------------------------------------------------------------------")
        cantidad = int(input("Cantidad a aumentar:"))
        art.cantidad += cantidad
        Articulo.modificar(cod, usuario, nueva_cant=art.cantidad)
        print("----------------------------------------------------------------------------------------------")
        print("Articulo actualizado correctamente")
        print("----------------------------------------------------------------------------------------------")
    else:
        print("No existe.")
        print("Volviendo al menu principal...")
        os.system("pause")
        from principal import menu_principal
        menu_principal(usuario)


def dar_baja_articulo(usuario):
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
        Articulo.modificar(cod, usuario, nueva_cant=art.cantidad)
        print("----------------------------------------------------------------------------------------------")
        print("Stock actualizado correctamente")
        print("----------------------------------------------------------------------------------------------")
    else:
        print("Articulo no encontrado")
        print("Volviendo al menu principal...")
        os.system("pause")
        from principal import menu_principal
        menu_principal(usuario)

def modificar_articulo(usuario):
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
            usuario=usuario,  
            nuevo_cod=nuevo_cod,  
            nuevo_nombre=nombre,
            nueva_cant=int(cant),
            nuevo_precio=float(precio)
        )
    else:
        print("No existe.")
        input("ENTER para continuar...")
        from principal import menu_principal
        menu_principal(usuario)

def listar_articulos(usuario):
    Articulo.listar(usuario)
    input("ENTER para continuar...")

def registrar_articulo(usuario):
    os.system("cls")
    cod = input('Ingrese el codigo del nuevo articulo: ')
    art= Articulo()
    if art.leer(cod):
        print("El código ya existe.")
    else:
        nombre = input("Nombre: ")
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: "))
        Articulo(cod, nombre, cantidad, precio).guardar(usuario)
        from principal import menu_principal
        menu_principal(usuario)

def eliminar_articulo(usuario):
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
            Articulo.eliminar(cod, usuario)
        else:
            print("Eliminacion cancelada")
            print("Enter para volver al menu principal")
            os.system("pause")
            from principal import menu_principal
            menu_principal(usuario)
    else:
        print("Articulo no encontrado")
        input("ENTER para Volver al menu principal")
        os.system("pause")
        from principal import menu_principal
        menu_principal(usuario)
    

def vender(usuario):
    import os
    from ficheros import cargar_inventario, guardar_venta
    os.system("cls")
    print("************* VENTA DE ARTÍCULOS **************\n")

    inventario = cargar_inventario()
    if inventario is None:
        print("No hay inventario registrado.")
        os.system("pause")
        from principal import menu_principal
        menu_principal(usuario)
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
                break
            else:
                    from datetime import datetime
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
                    print("-----------------------------------------------------------------------")
                    print(f"✅ Agregado: {cantidad} x {articulo['nombre']} (Subtotal: {subtotal})")
                    print("-----------------------------------------------------------------------")           
                    print(f"*" *27," Lista de Articulos ","*" *27)
                    print("-" * 70)
                    print(f"{'Cod':<10}{'Nombre':<20}{'Cant':>5}{'Precio':>15}{'Subtotal':>15}")
                    print("-" * 70)
                    for art in lista_venta:
                      print(f"{art['cod']:<10}{art['nombre']:<20}{art['cantidad']:>5}{art['precio']:>15.2f}{art['subtotal']:>15.2f}")
                    print("-" * 70)
                    print(f"{'Subtotal:':>55} {total_venta:>10.2f}")
                    print("-" * 70)
                    print("Presione ENTER para continuar...")
                    break
                    

    if not lista_venta:
        print("\nNo se realizó ninguna venta.")
        os.system("pause")
        from principal import menu_principal
        menu_principal(usuario)
        return
        
    if lista_venta:
        while True:
            os.system("cls")
            print("*************** Artículos en la venta ***************")
            for i, art in enumerate(lista_venta, start=1):
                print(f"{i}. {art['nombre']} - {art['cantidad']} x {art['precio']:.2f} = {art['subtotal']:.2f}")
            print("Total actual:", total_venta)
            print("*****************************************************")
            opcion = input("Ingresa el numero si quieres eliminar un articulo o ENTER para continuar): ")

            if opcion == "":
                break
            if opcion.isdigit():
                i = int(opcion) - 1
                if 0 <= i < len(lista_venta):
                    articulo_devuelto = lista_venta.pop(i)
                    total_venta -= articulo_devuelto["subtotal"]
                    
                    for art in inventario:
                        if art["cod"] == articulo_devuelto["cod"]:
                            art["cantidad"] += articulo_devuelto["cantidad"]
                    print(f"✅ Artículo '{articulo_devuelto['nombre']}' eliminado de la venta.")
                else:
                    print("Número inválido.")
            else:
                print("Entrada inválida. Escribe un número o ENTER.")
            os.system("pause")


    os.system("cls")
    from datetime import datetime
    iva = round(total_venta * 0.15, 2)
    total_con_iva = round(total_venta + iva, 2)
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

    
    import json
    numero_factura = 1
    try:
        with open("Facturas.json", "r", encoding="utf-8") as f:
            facturas = json.load(f)
            if facturas:
                numero_factura = facturas[-1]["numero"] + 1
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        numero_factura = 1

    print(f"*" *27," Factura de venta ","*" *27)
    print(f"Factura N°: {numero_factura}") 
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

    
    guardar_venta(lista_venta, inventario, total_venta, cliente, usuario)
    print(f"Venta registrada correctamente. Factura N°: {numero_factura}")


def imprimir_factura(usuario):
    while True:
        num = input("Ingrese el número de factura a imprimir: ").strip()
        if not num.isdigit():
            print("Debe ingresar un número válido.")
            continue
        num = int(num)
        break
    from ficheros import mostrar_factura
    mostrar_factura(num, usuario)  
    input("Presione ENTER para volver al menú principal...")
    from principal import menu_principal
    menu_principal(usuario)

def anular_factura(usuario):
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
        anular_factura_fichero(num, usuario)  # Pasa usuario si lo requiere
        from principal import menu_principal
        menu_principal(usuario)
    elif confirmacion == 'n':
        print("Anulacion cancelada volviendo al menu principal...")
        os.system("pause")
        from principal import menu_principal
        menu_principal(usuario)
    else: 
        print('Opcion invalida, volviendo al menu principal...')
        os.system("pause")
        from principal import menu_principal
        menu_principal(usuario)

def olvide_contrasena():
    os.system("cls")
    print("=== RECUPERAR CONTRASEÑA ===")
    username = input("Ingrese su nombre de usuario: ").strip()
    encontrado = False
    try:
        with open("usuarios.dat", "r") as f:
            for linea in f:
                partes = linea.strip().split()
                if len(partes) >= 2 and partes[0] == username:
                    encontrado = True
                    break
    except FileNotFoundError:
        print("No hay usuarios registrados.")
        os.system("pause")
        return

    if not encontrado:
        print("Usuario no encontrado.")
        os.system("pause")
        return

    correo = input("Ingrese el correo donde desea recibir el código: ").strip()
    codigo = str(random.randint(100000, 999999))

    
    EMAIL_EMISOR = "kenethzamora223@gmail.com"
    EMAIL_PASSWORD = "ooet wxtl pbem tnoa"

    mensaje = f"Sistema  recuperación de contraseña\n\nTu código de verificación es: {codigo}"
    msg = MIMEText(mensaje, "plain", "utf-8")
    msg["Subject"] = Header("Código de recuperación", "utf-8")
    msg["From"] = formataddr(("Soporte", EMAIL_EMISOR))
    msg["To"] = correo

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_EMISOR, EMAIL_PASSWORD)
            smtp.sendmail(EMAIL_EMISOR, correo, msg.as_string())
        print(f"Código enviado al correo {correo}.")
    except Exception as e:
        print("No se pudo enviar el correo. Verifica los datos y tu conexión a internet.")
        print("Error:", e)
        os.system("pause")
        return

    codigo_ingresado = input("Ingrese el código recibido en su correo: ").strip()
    if codigo_ingresado != codigo:
        print("Código incorrecto.")
        os.system("pause")
        return
    print("-------------------------------------------------")
    print("Codigo verificado correctamente")
    print("-------------------------------------------------")
    nueva_contra = input("Ingrese la nueva contraseña: ").strip()
    nuevas_lineas = []
    with open("usuarios.dat", "r") as f:
        for linea in f:
            partes = linea.strip().split()
            if len(partes) >= 2 and partes[0] == username:
                partes[1] = nueva_contra
                nuevas_lineas.append(" ".join(partes) + "\n")
            else:
                nuevas_lineas.append(linea)
    with open("usuarios.dat", "w") as f:
        f.writelines(nuevas_lineas)
    print("----------------------------------------------------------------")
    print("Contraseña actualizada correctamente.")
    print("----------------------------------------------------------------")
    os.system("pause")
    print("Enter para volver al menu principal")
    from InicioSesion import iniciar_sesion
    iniciar_sesion()
    print("----------------------------------------------------------------")
