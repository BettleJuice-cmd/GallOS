Algoritmo modificarUsuario
	
	Definir listaUsuarios, listaContra Como Caracter
	Definir usuarioBuscado, nuevoUsuario, nuevaContra Como Caracter
	Definir i, encontrado, totalUsuarios Como Entero
	
	Dimensionar listaUsuarios[100]
	Dimensionar listaContra[100]
	
	listaUsuarios[1]="Wilo"
	listaContra[1]="wilo1234"
	
	listaUsuarios[2]="Adolfo"
	listaContra[2]="contra1"
	
	listaUsuarios[3]="Andy"
	listaContra[3]="contra2"
	
	listaUsuarios[4]="Joshua"
	listaContra[4]="contra3"
	
	listaUsuarios[5]="Kenneth"
	listaContra[5]="contra4"
	
	totalUsuarios=5
	encontrado=0
	
	Escribir "============================================"
    Escribir "       MODIFICACI�N DE USUARIOS EXISTENTES"
    Escribir "============================================"
	
	Para i=1 Hasta totalUsuarios Hacer
		Escribir i, ".", listaUsuarios[i]
	FinPara
	
	Escribir "--------------------------------------------------------"
	Escribir"Ingrese el nombre EXACTO del usuario que desea modificar:"
	Leer usuarioBuscado
	
	Para i=1 Hasta totalUsuarios Hacer
		Si listaUsuarios[i]=usuarioBuscado Entonces
			Escribir "Usuario encontrado en la posici�n ", i
			
			Escribir "Ingrese el nuevo nombre del usuario (deje vac�o para mantenerlo igual)"
			Leer nuevoUsuario
			
			Si nuevoUsuario<>"" Entonces
				listaUsuarios[i]=nuevoUsuario
			FinSi
			
			Escribir "Ingrese la nueva contrase�a (deja vac�o para mantener la misma contrase�a)"
			Leer nuevaContra
			
			Si nuevaContra<>"" Entonces
				listaContra[i]=nuevaContra
			FinSi
			
			Escribir "Usuario modificado exitosamente..."
			encontrado=1
		FinSi
	FinPara
	
	Limpiar Pantalla
	
	Si encontrado=0 Entonces
		Escribir "El usuario no fue encontrado..."
	FinSi
	
	Escribir "============================================"
    Escribir "                 SACOS WILO"
	Escribir "                  USUARIOS"
	Para i=1 Hasta totalUsuarios Hacer
		Escribir i, ".", listaUsuarios[i]
	FinPara
    Escribir "============================================"
	
FinAlgoritmo
