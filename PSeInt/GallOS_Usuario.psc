Algoritmo GallOSUsuario
	
	Definir i, j Como Entero
	Definir usuario, contrasenia Como Caracter
	Definir pos, opc, max Como Entero
	max=1000000
	i=1
	Dimensionar usuario[max]
	Dimensionar contrasenia[max]
	
	Mientras opc<>4 Hacer
		Escribir "Digite una de las siguientes opciones"
		Escribir "1.....Agregar un usuario"
		Escribir "2.....Modificar un usuario"
		Escribir "3.....Eliminar un usuario"
		Escribir "4.....Salir del programa"
		leer opc
		
		Segun opc Hacer
			1:
				Escribir "Escriba el nombre del nuevo usuario"
				Leer usuario[i]
				Escribir "Digite una contraseña"
				Leer contrasenia[i]
				i=i+1
			2:
				Si i=1 Entonces
					Escribir "No hay ningun usuario"
				SiNo
					Para j=1 Hasta i-1 Hacer
						Si usuario[j]<>"" Entonces
							Escribir j, ".", usuario[j]
						FinSi
					FinPara
					
					Escribir "Ingresa el número de usuario que desea modificar"
					Leer pos
					
					Si pos>=1 Y pos<i Y usuario[pos]<>"" Entonces
						Escribir "Usuario actual ", usuario[pos], " contaseña actual ", contrasenia[pos]
						Escribir "Escriba el nuevo nombre del usuario"
						Leer usuario[pos]
						Escribir "Escriba la nueva contraseña del usuario (", usuario[pos], ")"
						Leer contrasenia[pos]
						Escribir "El usuario ha sido actualizado..."
						
					SiNo
						Escribir "El usuario no existe o fue eliminado"
					FinSi
				FinSi
			3:
				Si i=1 Entonces
					Escribir "No hay usuarios registrados"
				SiNo
					Para j=1 Hasta i-1 Hacer
						Si usuario[j]<>"" Entonces
							Escribir j, ".", usuario[j], contrasenia[j]
							Escribir "Digite el usuario que desea eliminar"
							Leer opc
						FinSi
						Si pos>=1 Y pos<i Y usuario[pos]<>"" Entonces
							usuario[pos]=""
							contrasenia[pos]=""
						FinSi
					FinPara
				FinSi
				
			5:
				Escribir "Saliendo del programa..."
		FinSegun
	FinMientras
FinAlgoritmo
