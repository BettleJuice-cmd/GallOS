//Autores: Adolfo C. Ramírez A.
           Andy S. Díaz M.
           Joshua I. Donaire Z.
           Kenneth M. Zamora H.
//Fecha:
//Versión: 1.0
//Descripción: En este pseudocódigo se gestionara cada artículo que se encuentra disponible en la tienda, el programa hará lo siguiente, 
//añadir un artículo, editar un artículo, elimar un artículo, ver el inventario y salir del programa

Algoritmo GestionarArticulo
	
	// Definimos las variables que iremos a utilizar
	Definir max, opc, pos Como Entero
	Definir i, j Como Entero
	Definir cantidad Como Entero
	Definir articulo Como Caracter
	i=1
	max=100
	Dimensionar articulo[max]
	Dimensionar cantidad[max]
	
	Mientras opc<>5 Hacer
		Escribir "Digite una de las siguientes opciones: "
		Escribir "1....Añadir un ariticulo"
		Escribir "2....Editar un articulo"
		Escribir "3....Eliminar un articulo"
		Escribir "4....Ver el inventario"
		Escribir "5....Salir"
		Leer opc
		
		Segun opc Hacer
			1:
				// En esta parte el propietario digita el artículo y la cantidad que se desea agregar
				Escribir "Escriba el nombre del artículo ", i, ":"
				Leer articulo[i]
				Escribir "Ingrese la cantidad del artículo ", i, ":"
				Leer cantidad[i]
				i=i+1
			2:
				// En este apartado el propietario edita el artículo que el desee
				
				// En esta condicional si no existe ningún artículo revotará lo siguiente
				Si i=1 Entonces
					Escribir "El inventario está vacío, no hay artículos para editar."
				// Si lo anterior no es verdadero lo lleverá a editar el artículo que el haya escogido
				Sino
					Escribir "Artículos disponibles para editar:"
					// Lo que hace la variable "j" es que va revisando cada arreglo que existe y arroja luego una lista de los arreglos que existan
					Para j=1 Hasta i-1 Hacer
						Si articulo[j]<>"" Entonces
							Escribir j, ". ", articulo[j], " - ", cantidad[j], " unidades"
						FinSi
					FinPara
					
					// Acá se pide que el usuario digitge el número de la lista que desea editar 
					Escribir "Ingrese el número del artículo que desea editar:"
					Leer pos
					
					// Si el número que digito el usuario coinciden con los que existe, el usuario, podrá editar ese artículo
					Si pos>=1 Y pos<i Y articulo[pos]<>"" Entonces
						Escribir "Artículo actual: ", articulo[pos], " - ", cantidad[pos], " unidades"
						// El propietario podrá asignar el nuevo nombre del artículo que eligio
						Escribir "Ingrese el nuevo nombre del artículo:"
						Leer articulo[pos]
						// El propietario podrá asignar una nueva cantidad de ese artículo editado
						Escribir "Ingrese la nueva cantidad del artículo:"
						Leer cantidad[pos]
						// Por último se lanzará un mensaje de que fue editado correctamente
						Escribir "Artículo editado correctamente."
					// Si el número que digito el usuario no existe dentro de la lista lanzará este mensaje:
					Sino
						Escribir "Número inválido o artículo ya eliminado."
					FinSi
				FinSi
			3:
				Si i=1 Entonces
					Escribir "El inventario está vacio, no hay artículos para eliminar"
				SiNo
					Escribir "Artículos disponibles para eliminar"
					Para j=1 Hasta i-1 Hacer
						Si articulo[j]<>"" Entonces
							Escribir j, ". ", articulo[j], " - ", cantidad[j], " unidades"
						FinSi
					FinPara
					Escribir "Ingrese el número del artículo que desea eliminar:"
					Leer pos
					
					Si pos>=1 Y pos<i Y articulo[pos]<>"" Entonces
						Escribir "Eliminando: ", articulo[pos], " (", cantidad[pos], " sacos)"
						articulo[pos]=""
						cantidad[pos]=-1
					SiNo
						Escribir "Número invalido o producto ya eliminado"
					FinSi
				FinSi
			4:
				Si i=1 Entonces
					Escribir "El inventario esta vacio"
					Para i=1 Hasta totalProducto Hacer
						Escribir i, ".", articulo[i], "(", cantidad[i],"cantidad)"
					FinPara
					
				SiNo
					Escribir "Lista de artículos actuales"
					Para j=1 Hasta i-1 Hacer
						Si articulo[j]<>"" Entonces
							Escribir j, ". ", articulo[j], " - ", cantidad[j], " unidades"
						FinSi
					FinPara
				FinSi
			5:
				Escribir "Saliendo del programa..."
			De Otro Modo:
				Escribir "Digite de nuevo una opcion correcta"
		FinSegun
	FinMientras
	
FinAlgoritmo
