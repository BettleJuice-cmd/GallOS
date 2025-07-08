Algoritmo GallOS_Eliminar
	
	Definir articulo Como Caracter
	Definir cantidad, codigo, precio Como Entero
	Definir i, max, pos Como Entero
	i=1
	Dimensionar articulo[4]
	Dimensionar cantidad[4]
	Dimensionar codigo[4]
	Dimensionar precio[4]
	
	articulo[1]="Saco quitanlero"
	cantidad[1]=25
	codigo[1]=111
	precio[1]=8
	
	articulo[2]="Sacos de 110 lb"
	cantidad[2]=28
	codigo[2]=222
	precio[2]=8
	
	articulo[3]="Sacos rojos 150 lb"
	cantidad[3]=40
	codigo[3]=333
	precio[3]=13
	
	articulo[4]="Sacos rojos 200 lb"
	cantidad[4]=30
	codigo[4]=444
	precio[4]=15
	
	max=4
	
	Escribir "======= BIENVENIDO A SACOS WILO ======="
	Escribir "======================================="
    Escribir "    INVENTARIO ANTES DE ELIMINAR"
    Escribir "======================================="
    Para i = 1 Hasta max Hacer
		Si articulo[i] <> "" Entonces
			Escribir i, ". ", articulo[i], " - ", cantidad[i], " sacos ", "| ", "código del articulo ",codigo[i], " precio del producto:", precio[i], " C$"
		FinSi
	FinPara
	
	Escribir "Ingrese el número del artículo que desea eliminar"
	Leer pos
	
	Si pos >= 1 Y pos < i Y articulo[pos] <> "" Entonces
        Escribir ""
        Escribir "Eliminando: ", articulo[pos], " (", cantidad[pos], " sacos, código ", codigo[pos], " precio: ", precio[pos], "C$)"
        articulo[pos]=""
        cantidad[pos]=-1
		codigo[pos]=-1
		precio[pos]=-1
        Escribir "Producto eliminado correctamente."
    Sino
        Escribir "Posición inválida o producto ya eliminado."
    FinSi
	
	Escribir "======================================="
	Escribir "       PRODUCTOS DISPONIBLES"
	Escribir "======================================="
	Para i = 1 Hasta max Hacer
		Si articulo[i] <> "" Entonces
			Escribir i, ". ", articulo[i], " - ", cantidad[i], " sacos ", "| ", "código del articulo ",codigo[i], " precio del producto:", precio[i], " C$"
		FinSi
	FinPara
	
FinAlgoritmo	