Algoritmo aniadorUsuario
	
	Definir listaUsuarios, listaContra, usuario, contrasenia Como Caracter
	
	Dimensionar listaUsuarios[100] 
	Dimensionar listaContra[100]
	
	listaUsuarios[1]="GallOS"
	listaContra[1]="wilo1234"
	
	Limpiar Pantalla
	
	Repetir
		Escribir "============================================"
		Escribir "        BIENVENIDO ", listaUsuarios[1]
		Escribir "       SISTEMA DE GESTIÓN DE USUARIOS"
		Escribir "============================================"
		Escribir "Por favor escriba la contraseña para añadir a un usuario nuevo"
		Leer contrasenia
		Si contrasenia<>listaContra[1] Entonces
			Escribir "Contraseña incorrecta, intentalo de nuevo..."
			Leer contrasenia
		FinSi
		Limpiar Pantalla
	Hasta Que contrasenia=listaContra[1]	
	
	Repetir
		Escribir "============================================"
		Escribir "        BIENVENIDO A SACOS WILO "
		Escribir "       SISTEMA DE GESTIÓN DE USUARIOS"
		Escribir "============================================"
		Escribir ""
		Escribir "Ingrese el nombre del nuevo usuario (0 para salir): "
		Leer usuario
		
		Si usuario<>"0" Entonces
			Escribir "Ingresa la contraseña del usuario (", usuario, ")"
			Leer contrasenia
			
			Escribir "Usuario añadido..."
		FinSi
	Hasta Que usuario="0"
	
	Limpiar Pantalla
	
	Escribir "============================================"
	Escribir "        GRACIAS POR USAR SACOS WILO"
	Escribir "============================================"
	
FinAlgoritmo