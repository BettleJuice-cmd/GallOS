//Autores: Adolfo C. Ramírez A.
//         Andy S. Díaz M.
//         Joshua I. Donaire Z.
//         Kenneth M. Zamora H.
//Fecha:
//Versión: 1.0
//Descripción: Este pseudocódigo se encargará de imprimir las facturas de venta
	




Algoritmo GallOS_imprimir
	
	Definir listaVentas,nombreFactura Como Caracter
	Definir opcion,opcion2 como Entero
	
	
	
	Dimensionar listaVentas[5]
	
	listaVentas[0]="1..........Carlos Gutierrez------23/04/2021"
	listaVentas[1]="2..........Fofo Arauz------12/07/2023"
	listaVentas[2]="3..........Kenneth Zamora------23/05/2023"
	listaVentas[3]="4..........Joshua Donaire------09/09/11"
	listaVentas[4]="5..........Maverick Lopez------03/10/2024"
	
	
	Escribir "======================================================"
	Escribir "                    SACOS WILO                        "
	Escribir "======================================================"
	Escribir " En: Facturar                            ",FechaActual()  
	Escribir "     ¡BIENVENIDO A LA SECCION DE IMPRIMIR VENTAS!     "
	Escribir "Por favor, seleccione la opcion que desee ejecutar    "
	
	Mientras opcion <>3 Hacer
		Escribir "Digite un numero para seleccionar una accion"
		Escribir "1.................Mostrar los nombres de todas las facturas de ventas"
		Escribir "2.................Imprimir factura de venta"
		Escribir "3.................Salir'
		leer opcion
		
		
		Segun opcion Hacer
			1:
				Escribir "Estas son todas las facturas de venta registradas"
				Escribir listaVentas[0]
				Escribir listaVentas[1]
				Escribir listaVentas[2]
				Escribir listaVentas[3]
				Escribir listaVentas[4]
				Escribir "Presione cualquier tecla para continuar"
				Esperar Tecla
				Limpiar Pantalla
				
			2:
				Escribir "Ingrese el nombre de la factura de venta que quiere imprimir:"
				Leer nombreFactura
				
				Escribir "IMPRIMIENDO FACTURA..."
				Escribir "Presione cualquier tecla para continuar"
				Esperar Tecla
				Limpiar Pantalla
				
				
			3:
				Escribir "Saliendo de IMPRIMIR FACTURA..."
				
		FinSegun
	
	FinMientras
	
	
	
	
	
	
	
	
FinAlgoritmo
