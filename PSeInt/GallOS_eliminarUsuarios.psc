Algoritmo eliminarUsuarios
	
	Definir listaUsuarios, listaContra Como Caracter
	Definir usuarioBuscado Como Caracter
	Definir i, j, encontrado, totalUsuarios Como Entero
	
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
	
	
	Limpiar Pantalla
	
	Escribir "============================================"
    Escribir "           ELIMINACIÓN DE USUARIOS"
    Escribir "============================================"
    Escribir "Lista actual de usuarios:"
	
	Para i=1 Hasta totalUsuarios Hacer
		Escribir i, ".", listaUsuarios[i]
	FinPara
	
	Escribir "--------------------------------------"
	Escribir "Ingrese el nombre EXACTO del usuario que desee eliminar"
	Leer usuarioBuscado
	
	Si listaUsuarios[i]=usuarioBuscado Y usuarioBuscado<>"Wilo" Entonces
		
	FinSi
	
	Para i=1 Hasta totalUsuarios Hacer
		Si listaUsuarios[i]=usuarioBuscado Entonces
			encontrado=1
			
			Para j=i Hasta totalUsuarios-1 Hacer
				listaUsuarios[j]=listaUsuarios[j+1]
				listaContra[j]=listaContra[j+1]
			FinPara
			
			listaUsuarios[totalUsuarios]=""
			listaContra[totalUsuarios]=""
			
			totalUsuarios=totalUsuarios-1
			Escribir "Usuario eliminado..."
		FinSi
	FinPara
	
	Limpiar Pantalla
	
	Si encontrado=0 Entonces
		Escribir "El usuario no fue encontrado"
	FinSi
	
	Escribir "============================================"
    Escribir "      FIN DEL PROCESO DE ELIMINACIÓN"
	Escribir "            Usuarios existentes"
	Para i=1 Hasta totalUsuarios Hacer
		Escribir i, ".", listaUsuarios[i]
	FinPara
    Escribir "============================================"
	
FinAlgoritmo
