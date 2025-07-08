import os

class Usuario:
    def __init__(self, username, password, es_admin=False):
        self.username = username
        self.password = password
        self.es_admin = es_admin

    @staticmethod
    def autenticar(username, password):
        try:
            with open("usuarios.dat", "r") as f:
                for linea in f:
                    partes = linea.strip().split()
                    if len(partes) == 3 and partes[0] == username and partes[1] == password:
                        return Usuario(partes[0], partes[1], partes[2] == "True")
        except FileNotFoundError:
            pass
        return None

    def guardar(self):
        with open("usuarios.dat", "a") as f:
            f.write(f"{self.username} {self.password} {self.es_admin}\n")

def registrar_usuario():
    os.system("cls")
    print("=== REGISTRAR NUEVO USUARIO ===")
    username = input("Nuevo usuario: ")
    password = input("Contraseña: ")
    es_admin = False  # Siempre será usuario normal
    usuario = Usuario(username, password, es_admin)
    usuario.guardar()
    print("Usuario registrado exitosamente.")
    os.system("pause")

def registrar_admin():
    os.system("cls")
    print("=== REGISTRAR NUEVO ADMINISTRADOR ===")
    username = input("Nuevo usuario admin: ")
    password = input("Contraseña: ")
    es_admin = True
    usuario = Usuario(username, password, es_admin)
    usuario.guardar()
    print("Administrador registrado exitosamente.")
    os.system("pause")

def login():
    os.system("cls")
    print("=== INICIAR SESIÓN ===")
    username = input("Usuario: ")
    password = input("Contraseña: ")
    usuario = Usuario.autenticar(username, password)
    if usuario:
        print("¡Inicio de sesión exitoso!")
        os.system("pause")
        return usuario
    else:
        print("Usuario o contraseña incorrectos.")
        os.system("pause")
        return None