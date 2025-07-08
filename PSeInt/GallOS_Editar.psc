Algoritmo GallOS_Editar
	Definir articulo Como Caracter
	Definir cantidad, codigo, precio Como Entero
	Definir i, j, max, pos Como Entero
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
		Escribir "  PRODUCTOS DISPONIBLES PARA EDITAR"
		Escribir "======================================="
		Para i = 1 Hasta max Hacer
			Si articulo[i] <> "" Entonces
				Escribir i, ". ", articulo[i], " - ", cantidad[i], " sacos ", "| ", "código del articulo ",codigo[i], " precio del producto:", precio[i], " C$"
			FinSi
		FinPara
		
		Escribir ""
		Escribir "Ingrese el número del producto que desea editar:"
		Leer pos
		
		Si pos >= 1 Y pos < i Y articulo[pos] <> "" Entonces
			Escribir "Producto actual:"
			Escribir "Nombre: ", articulo[pos]
			Escribir "Cantidad: ", cantidad[pos], " sacos"
			Escribir "Código: ", codigo[pos]
			Escribir "Precio: ", precio[pos], " C$" 
			
			Escribir ""
			Escribir "Ingrese el nuevo nombre:"
			Leer articulo[pos]
			Escribir "Ingrese la nueva cantidad de sacos:"
			Leer cantidad[pos]
			Escribir "Inregsa el nuevo código:"
			Leer codigo[pos]
			Escribir "Ingresa el nuevo precio"
			Leer precio[pos]
			
			Limpiar Pantalla
			Escribir "Producto editado correctamente."
		Sino
			Escribir "Número inválido o producto ya eliminado."
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
