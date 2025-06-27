//Autores: Adolfo C. Ramírez A.
//         Andy S. Díaz M.
//         Joshua I. Donaire Z.
//         Kenneth M. Zamora H.
//Fecha:
//Versión: 1.0
//Descripción: En este pseudocódigo se gestionara cada artículo que se encuentra disponible en la tienda, el programa hará lo siguiente, 
//podrá editar un artículo y su cantidad

Algoritmo GallOS_Editar
	Definir articulo Como Caracter
	Definir cantidad Como Entero
	Definir i, j, max, pos Como Entero
	i=1
	max=1000000
	Dimensionar articulo[max]
	Dimensionar cantidad[max]
	
	Escribir "======= BIENVENIDO A SACOS WILO ======="

		Si i = 1 Entonces
			Escribir "El inventario está vacío, no hay productos para editar."
		Sino
			Escribir "======================================="
			Escribir "  PRODUCTOS DISPONIBLES PARA EDITAR"
			Escribir "======================================="
			Para j <- 1 Hasta i - 1 Hacer
				Si articulo[j] <> "" Entonces
					Escribir j, ". ", articulo[j], " - ", cantidad[j], " sacos"
				FinSi
			FinPara
			
			Escribir ""
			Escribir "Ingrese el número del producto que desea editar:"
			Leer pos
			
			Si pos >= 1 Y pos < i Y articulo[pos] <> "" Entonces
				Escribir "Producto actual:"
				Escribir "Nombre: ", articulo[pos]
				Escribir "Cantidad: ", cantidad[pos], " sacos"
				
				Escribir ""
				Escribir "Ingrese el nuevo nombre del producto:"
				Leer articulo[pos]
				Escribir "Ingrese la nueva cantidad de sacos:"
				Leer cantidad[pos]
				
				Escribir "Producto editado correctamente."
			Sino
				Escribir "Número inválido o producto ya eliminado."
			FinSi
		FinSi
	
FinAlgoritmo