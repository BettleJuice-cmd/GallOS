class Articulo:
    def __init__(self, cod="", nombre="", cantidad=0, precio=0.0):
        self.cod = cod
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def guardar(self):
        with open("Inventario.dat", "a", encoding="utf-8") as f:
            f.write(f"{self.cod} {self.nombre} {self.cantidad} {self.precio}\n")

    def leer(self, cod_buscado):
        with open("Inventario.dat", "r", encoding="utf-8") as f:
            for linea in f:
                partes = linea.strip().split()
                if partes[0] == cod_buscado:
                    self.cod = partes[0]
                    # Nombre puede tener espacios: desempaca desde índice 1 hasta len-3
                    self.nombre = " ".join(partes[1:-2])
                    self.cantidad = int(partes[-2])
                    self.precio = float(partes[-1])
                    return True
        return False

    
    def listar():
        try:
            with open("Inventario.dat", "r", encoding="utf-8") as f:
                print(f"{'Cod':<6} {'Nombre':<20} {'Cant':>5} {'Precio':>8}")
                print("-" * 42)
                for linea in f:
                    partes = linea.strip().split()
                    cod = partes[0]
                    nombre = " ".join(partes[1:-2])
                    cantidad = partes[-2]
                    precio = partes[-1]
                    print(f"{cod:<6} {nombre:<20} {cantidad:>5} {precio:>8}")
        except FileNotFoundError:
            print("Inventario vacío.")


    def modificar(cod, nueva_cant=None, nuevo_precio=None, nuevo_nombre=None):
        lineas = []
        encontrado = False
        with open("Inventario.dat", "r", encoding="utf-8") as f:
            for linea in f:
                partes = linea.strip().split()
                if partes[0] == cod:
                    nombre = nuevo_nombre or " ".join(partes[1:-2])
                    cantidad = nueva_cant if nueva_cant is not None else int(partes[-2])
                    precio = nuevo_precio if nuevo_precio is not None else float(partes[-1])
                    lineas.append(f"{cod} {nombre} {cantidad} {precio}\n")
                    encontrado = True
                else:
                    lineas.append(linea)
        if encontrado:
            with open("Inventario.dat", "w", encoding="utf-8") as f:
                f.writelines(lineas)
        return encontrado

    def eliminar(cod):
        lineas = []
        eliminado = False
        with open("Inventario.dat", "r", encoding="utf-8") as f:
            for linea in f:
                if linea.strip().split()[0] != cod:
                    lineas.append(linea)
                else:
                    eliminado = True
        if eliminado:
            with open("Inventario.dat", "w", encoding="utf-8") as f:
                f.writelines(lineas)
        return eliminado
