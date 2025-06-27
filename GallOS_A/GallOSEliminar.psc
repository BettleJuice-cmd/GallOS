//Autores: Adolfo C. Ramírez A.
           Andy S. Díaz M.
           Joshua I. Donaire Z.
           Kenneth M. Zamora H.
//Fecha:
//Versión: 1.0
//Descripción: En este pseudocódigo se gestionara cada artículo que se encuentra disponible en la tienda, el programa hará lo siguiente, 
//podrá elimar un artículo 

Algoritmo GallOS_Eliminar
	
	Definir articulo Como Caracter
	Definir cantidad Como Entero
	Definir i, j, max, pos Como Entero
	i=1
	max=1000000
	Dimensionar articulo[max]
	Dimensionar cantidad[max]
	
	Escribir "======= BIENVENIDO A SACOS WILO ======="
	Escribir "======================================="
    Escribir "    INVENTARIO ANTES DE ELIMINAR"
    Escribir "======================================="
    Para j <- 1 Hasta i - 1 Hacer
        Si articulo[j] <> "" Entonces
            Escribir j, ". ", articulo[j], " - ", cantidad[j], " sacos"
        FinSi
    FinPara
	
	Si pos >= 1 Y pos < i Y articulo[pos] <> "" Entonces
        Escribir ""
        Escribir "Eliminando: ", articulo[pos], " (", cantidad[pos], " sacos)"
        articulo[pos] <- ""
        cantidad[pos] <- -1
        Escribir "Producto eliminado correctamente."
    Sino
        Escribir "Posición inválida o producto ya eliminado."
    FinSi
	
FinAlgoritmo