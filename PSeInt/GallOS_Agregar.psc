Algoritmo GallOS_Agregar
	Definir articulo Como Caracter
	Definir cantidad, codigo, precio Como Entero
	Definir i, max, opc Como Entero
	i=1
	max=100
	Dimensionar articulo[max]
	Dimensionar cantidad[max]
	Dimensionar codigo[max]
	Dimensionar precio[max]
	
	Escribir "========== BIENVENIDO A SACOS WILO =========="
	Escribir "Precione 1 para agregar un artículo y 0 para salir"
	Leer opc
	Limpiar Pantalla
	
	Mientras opc=1 Hacer
		Escribir "========== BIENVENIDO A SACOS WILO =========="
		Escribir "Ingrese el código del artículo ", i, ":"
		Leer codigo[i]
		Escribir "Escriba el nombre del artículo ", i, ":"
		leer articulo[i]
		Escribir "Ingrese la cantidad del artículo ", i, ":"
		leer cantidad[i]
		Escribir "Ingrese el precio del producto ", i, ":"
		Leer precio[i]
		Escribir "Precione 1 para agregar un artículo y 0 para salir"
		Leer opc
		i=i+1
	FinMientras
	
	Limpiar Pantalla
	
	Escribir "======================================="
	Escribir "       PRODUCTOS DISPONIBLES"
	Escribir "======================================="
	Para i = 1 Hasta i Hacer
		Si articulo[i] <> "" Entonces
			Escribir i, ". ", articulo[i], " - ", cantidad[i], " sacos ", "| ", "código del articulo ",codigo[i], " precio del producto:", precio[i], " C$"
		FinSi
	FinPara
	Escribir "Saliendo del sistema..."
	
FinAlgoritmo
