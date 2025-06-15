//Autores: Adolfo C. Ramírez A.
           Andy S. Díaz M.
           Joshua I. Donaire Z.
           Kenneth M. Zamora H.
//Fecha:
//Versión: 1.0
//Descripción: En este pseudocódigo se gestionara cada artículo que se encuentra disponible en la tienda, el programa hará lo siguiente, 
//añadir un artículo, editar un artículo, elimar un artículo, ver el inventario y salir del programa

Algoritmo GestionarArticulo
	
	Definir max, opc, pos Como Entero
	Definir i, j Como Entero
	Definir canti Como Entero
	Definir articulo Como Caracter
	i=1
	max=1000000
	Dimensionar articulo[max]
	Dimensionar canti[max]
	
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
				Escribir "Escriba el nombre del articulo ", i , ":"
				Leer articulo[i]
				Escribir "Ingrese la cantidad del articulo ", i , ":"
				Leer canti[i]
				i=i+1
			2:
				Si i=1 Entonces
					Escribir "El inventario está vacío, no hay artículos para editar."
				Sino
					Escribir "Artículos disponibles para editar:"
					Para j=1 Hasta i-1 Hacer
						Si articulo[j]<>"" Entonces
							Escribir j, ". ", articulo[j], " - ", canti[j], " unidades"
						FinSi
					FinPara
					
					Escribir "Ingrese el número del artículo que desea editar:"
					Leer pos
					
					Si pos>=1 Y pos<i Y articulo[pos]<>"" Entonces
						Escribir "Artículo actual: ", articulo[pos], " - ", canti[pos], " unidades"
						Escribir "Ingrese el nuevo nombre del artículo:"
						Leer articulo[pos]
						Escribir "Ingrese la nueva cantidad del artículo:"
						Leer canti[pos]
						Escribir "Artículo editado correctamente."
					Sino
						Escribir "Número inválido o artículo ya eliminado."
					FinSi
				FinSi
			3:
				
			4:
				
			5:
				Escribir "Saliendo del programa..."
			De Otro Modo:
				Escribir "Digite de nuevo una opcion correcta"
		FinSegun
	FinMientras
	
FinAlgoritmo