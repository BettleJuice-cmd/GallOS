//Autores: Adolfo C. Ramírez A.
//         Andy S. Díaz M.
//         Joshua I. Donaire Z.
//         Kenneth M. Zamora H.
//Fecha:
//Versión: 1.0
//Descripción: En este pseudocódigo se gestionara cada artículo que se encuentra disponible en la tienda, el programa hará lo siguiente, 
//podrá agregar un ariticulo nuevo con su cantidad

Algoritmo GallOS_Agregar
	Definir articulo Como Caracter
	Definir cantidad Como Entero
	Definir i, max Como Entero
	i=1
	max=1000000
	Dimensionar articulo[max]
	Dimensionar cantidad[max]
	
	Para i=1 Hasta max Hacer
		Escribir "========== BIENVENIDO A SACOS WILO =========="
		Escribir "Escriba el nombre del artículo ", i, ":"
		leer articulo[i]
		Escribir "Ingrese la cantidad del artículo ", i, ":"
		leer cantidad[i]
	FinPara
	
FinAlgoritmo
