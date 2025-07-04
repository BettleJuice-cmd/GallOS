//Autores: Adolfo C. Ramírez A.
//         Andy S. Díaz M.
//         Joshua I. Donaire Z.
//         Kenneth M. Zamora H.
//Fecha:
//Versión: 1.0
//Descripción: En este pseudocódigo se gestionara cada artículo que se encuentra disponible en la tienda, el programa hará lo siguiente, 
//podrá ver el inventario

Algoritmo GallOS_Inventario
	
	Definir articulo Como Caracter
	Definir cantidad Como Entero
	Definir i, j, max, pos Como Entero
	i=1
	max=1000000
	Dimensionar articulo[max]
	Dimensionar cantidad[max]
	
	Escribir "======================================="
    Escribir "     STOCK ACTUAL - SACOS WILO"
    Escribir "======================================="
    Para j <- 1 Hasta i - 1 Hacer
        Si articulo[j] <> "" Entonces
            Escribir j, ".", articulo[j], " - ", cantidad[j], " sacos"
        FinSi
    FinPara
	
FinAlgoritmo
