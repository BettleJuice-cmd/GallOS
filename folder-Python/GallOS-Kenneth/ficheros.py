import json
import os
from datetime import datetime
class Articulo:
    def __init__(self, cod="", nombre="", cantidad=0, precio=0.0):
        self.cod = cod
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def guardar(self, usuario):
        articulos = []
        if os.path.exists("Inventario.json"):
            with open("Inventario.json", "r", encoding="utf-8") as f:
                articulos = json.load(f)
        articulos.append({
            "cod": self.cod,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        })
        with open("Inventario.json", "w", encoding="utf-8") as f:
            json.dump(articulos, f, ensure_ascii=False, indent=2)
        from principal import menu_principal
        menu_principal(usuario)

    def leer(self, cod_buscado):
        if not os.path.exists("Inventario.json"):
            return False
        with open("Inventario.json", "r", encoding="utf-8") as f:
            articulos = json.load(f)
            for art in articulos:
                if art["cod"] == cod_buscado:
                    self.cod = art["cod"]
                    self.nombre = art["nombre"]
                    self.cantidad = art["cantidad"]
                    self.precio = art["precio"]
                    return True
        return False

    @staticmethod
    def modificar(cod, usuario, nuevo_cod=None, nuevo_nombre=None, nueva_cant=None, nuevo_precio=None):
        if not os.path.exists("Inventario.json"):
            return False
        with open("Inventario.json", "r", encoding="utf-8") as f:
            articulos = json.load(f)
        encontrado = False
        for art in articulos:
            if art["cod"] == cod:
                if nuevo_cod is not None:
                    art["cod"] = nuevo_cod
                if nuevo_nombre is not None:
                    art["nombre"] = nuevo_nombre
                if nueva_cant is not None:
                    art["cantidad"] = nueva_cant
                if nuevo_precio is not None:
                    art["precio"] = nuevo_precio
                encontrado = True
                break
        if encontrado:
            with open("Inventario.json", "w", encoding="utf-8") as f:
                json.dump(articulos, f, ensure_ascii=False, indent=2)
        print("----------------------------------------------------------------------------------------------")
        print("Articulo modificado Correctamente")
        print("----------------------------------------------------------------------------------------------")
        print("Enter para volver al menu principal")
        print("----------------------------------------------------------------------------------------------")
        os.system("pause")
        from principal import menu_principal
        menu_principal(usuario)

    @staticmethod
    def eliminar(cod, usuario):
        if not os.path.exists("Inventario.json"):
            return False
        with open("Inventario.json", "r", encoding="utf-8") as f:
            articulos = json.load(f)
        nuevos = [art for art in articulos if art["cod"] != cod]
        eliminado = len(nuevos) != len(articulos)
        if eliminado:
            with open("Inventario.json", "w", encoding="utf-8") as f:
                json.dump(nuevos, f, ensure_ascii=False, indent=2)
        print("Articulo eliminado correctamente")
        print("----------------------------------------------------------------------------------------------")
        print("Enter para volver al menu principal")
        from principal import menu_principal
        os.system("pause")
        menu_principal(usuario)
        return eliminado

    @staticmethod
    def listar(usuario):
        os.system("cls")
        if not os.path.exists("Inventario.json"):
            print("No hay articulos registrados.")
            return
        with open("Inventario.json", "r", encoding="utf-8") as f:
            articulos = json.load(f)
            if not articulos:
                print("No hay articulos registrados.")
                print("Enter para volver al menu principal")
                os.system('pause')
                from principal import menu_principal
                menu_principal(usuario)
            print("-" * 90)
            print(f"{'Codigo':<10}{'Nombre':<25}{'Stock':>13}{'Precio':>15}")
            print("-" * 90)
            for art in articulos:
                print(f"{art['cod']:<10}{art['nombre']:<25}{str(art['cantidad']):>10}{str(art['precio']):>15}")
            print("-" * 90)
            print("Enter para volver al menu principal")
            print("-" * 90)
            os.system("pause")
            from principal import menu_principal
            menu_principal(usuario)

def cargar_inventario():
    if not os.path.exists("Inventario.json"):
        return None
    with open("Inventario.json", "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_venta(lista_venta, inventario, total_venta, cliente, usuario):
    
    with open("Inventario.json", "w", encoding="utf-8") as f:
        json.dump(inventario, f, ensure_ascii=False, indent=2)

    
    if os.path.exists("Facturas.json"):
        with open("Facturas.json", "r", encoding="utf-8") as f:
            facturas = json.load(f)
    else:
        facturas = []

    numero_factura = len(facturas) + 1
    iva = round(total_venta * 0.15, 2)
    total_con_iva = round(total_venta + iva, 2)

    from datetime import datetime
    nueva_factura = {
        "numero": numero_factura,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "cliente": cliente,
        "articulos": lista_venta,
        "subtotal": round(total_venta, 2),
        "iva": iva,
        "total": total_con_iva
    }
    facturas.append(nueva_factura)

    with open("Facturas.json", "w", encoding="utf-8") as f:
        json.dump(facturas, f, ensure_ascii=False, indent=2)

    print(f"\nFactura #{numero_factura} registrada con éxito.")
    print(f"Cliente: {cliente}")
    print(f"Subtotal: {total_venta}")
    print(f"IVA (15%): {iva}")
    print(f"TOTAL: {total_con_iva}")
    print("----------------------------------------------------------------------------------------------")
    print("Enter para volver al menu principal")
    os.system("pause")
    from principal import menu_principal
    menu_principal(usuario)

def mostrar_factura(numero_factura, usuario):
    os.system("cls")
    print("*"*26, "Imprimir Factura", "*"*26)

    # Cargar facturas desde el archivo
    facturas = []
    if os.path.exists("Facturas.json"):
        with open("Facturas.json", "r", encoding="utf-8") as f:
            facturas = json.load(f)

    if not facturas:
        print("No hay facturas registradas.")
        os.system("pause")
        from principal import menu_principal
        menu_principal(usuario)
        return

    factura = next((f for f in facturas if f["numero"] == numero_factura), None)
    if not factura:
        print("Factura no encontrada.")
        os.system("pause")
        from principal import menu_principal
        menu_principal(usuario)
        return
    
    with open("Facturas.json", "r", encoding="utf-8") as f:
        facturas = json.load(f)

    print(f"\nFactura #{factura['numero']} - Fecha: {factura['fecha']} Cliente: {factura['cliente']}")
    print("-" * 70)
    print(f"{'Cod':<10}{'Nombre':<20}{'Cant':>5}{'Precio':>10}{'Subtotal':>10}")
    print("-" * 70)
    for art in factura["articulos"]:
        print(f"{art['cod']:<10}{art['nombre']:<20}{art['cantidad']:>5}{art['precio']:>10.2f}{art['subtotal']:>10.2f}")
    print("-" * 70)
    print(f"{'Subtotal:':>55} {factura['subtotal']:>10.2f}")
    print(f"{'IVA (15%):':>55} {factura['iva']:>10.2f}")
    print(f"{'TOTAL:':>55} {factura['total']:>10.2f}")
    print("-" * 70)
    os.system("pause")
    from principal import menu_principal
    menu_principal(usuario)

def anular_factura_fichero(numero_factura, usuario):
    os.system("cls")
    print("*************ANULAR FACTURA**************")

    if not os.path.exists("Facturas.json"):
        print("No hay facturas registradas.")
        os.system("pause")
        from principal import menu_principal
        menu_principal(usuario)
        return

    with open("Facturas.json", "r", encoding="utf-8") as f:
        facturas = json.load(f)

    with open("Inventario.json", "r", encoding="utf-8") as f:
        inventario = json.load(f)

    idx = next((i for i, f in enumerate(facturas) if f["numero"] == numero_factura), None)
    if idx is None:
        print("Factura no encontrada.")
        os.system("pause")
        from principal import menu_principal
        menu_principal(usuario)
        return



    for art_vendido in facturas[idx]["articulos"]:
        for art_inv in inventario:
            if art_inv["cod"] == art_vendido["cod"]:
                art_inv["cantidad"] += art_vendido["cantidad"]
                break

    facturas.pop(idx)

    
    for i, factura in enumerate(facturas, start=1):
        factura["numero"] = i

    with open("Facturas.json", "w", encoding="utf-8") as f:
        json.dump(facturas, f, ensure_ascii=False, indent=2)
    with open("Inventario.json", "w", encoding="utf-8") as f:
        json.dump(inventario, f, ensure_ascii=False, indent=2)

    print("Factura anulada, stock devuelto y numeración actualizada.")
    os.system("pause")
    from principal import menu_principal
    menu_principal(usuario)





