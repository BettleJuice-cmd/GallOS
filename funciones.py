from ficheros import Articulo

def aumentar_stock():
    cod = input("Código: ")
    art = Articulo()
    if art.leer(cod):
        cantidad = int(input("¿Cuánto agregar? "))
        art.cantidad += cantidad
        Articulo.modificar(cod, nueva_cant=art.cantidad)
    else:
        nombre = input("Nombre: ")
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: "))
        Articulo(cod, nombre, cantidad, precio).guardar()

def dar_baja_articulo():
   cod = input("Código a eliminar: ")
   if Articulo.eliminar(cod):
       print("Eliminado.")
   else:
      print("No encontrado.")

def modificar_articulo():
    cod = input("Código a modificar: ")
    art = Articulo()
    if art.leer(cod):
     print(f"Actual: {art.nombre}, {art.cantidad}, {art.precio}")
     cod = input("Nuevo codigo: (enter = sin cambios) ") or art.cod
     nombre = input("Nuevo nombre (enter = sin cambio): ") or art.nombre
     cant = input("Nueva cantidad:(enter = sin cambios) ") or art.cantidad
     precio = input("Nuevo precio: (enter = sin cambios) ") or art.precio
     Articulo.modificar(
                    nuevo_cod=cod,
                    nuevo_nombre=nombre,
                    nueva_cant=int(cant),
                    nuevo_precio=float(precio))
    else:
     print("No existe.")
     input("ENTER para continuar...")


def listar_articulos():
    Articulo.listar()
    input("ENTER para continuar...")