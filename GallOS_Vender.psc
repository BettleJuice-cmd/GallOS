//Descripcion: Esta función se encargará de vender los articulos que se encuentren en el inventario
// Autores: 
//Joshua Donaire
//Adolfo Arauz
//Andy Diaz
//Kenneth Zamora

Algoritmo GallOS_Vender
	
	Definir cliente,fecha, direccion Como Caracter
	Definir total, precioUnit, cantidadTotal como real
	Definir opcion, codigo, cantidad, opcFin,codigoSaco Como Entero
	
	Escribir "======================================================"
	Escribir "                  SACOS WILO                          "
	Escribir "======================================================"
	Escribir "   En: Facturar                		    ",FechaActual()
	
	Escribir "       ¡BIENVENIDO A LA SECCION DE VENTAS!            "
	
		Escribir "Por favor, seleccione la opción que desee ejecutar...."
		Escribir "1.... Nueva Ventana"
		Escribir "2.... Salir"
		leer opcion
		Limpiar Pantalla
		Segun opcion Hacer
			1:
				
				Escribir "======================================================"
				Escribir "                  SACOS WILO                          "
				Escribir "======================================================"
				Escribir "   En: Facturar                		    ",FechaActual()
				Escribir "      Ingrese el nombre del cliente: "
				leer cliente 
				Escribir "      Ingrse la direccion del cliente: "
				leer direccion
				Repetir 
					Escribir "Ingrese el código del saco que desea vender: "
					leer codigo
					Escribir "Ingrese la cantidad de sacos que desea vender: "
					leer cantidad
					Escribir "Desea concluir su venta? (Digite 0 para concluir 1 para continuar)"
					leer opcFin
					Limpiar Pantalla
				hasta que opcFin=0
				Escribir "======================================================"
				Escribir "                  SACOS WILO                          "
				Escribir "======================================================"
				Escribir "   En: Facturar                		    ",FechaActual()
				Escribir "   Imprimiendo Factura.......   					 "
				Escribir "   Gracias por comprar en Sacos Wilo!                 "
				Escribir "======================================================"
				
				
			2:
				Escribir "======================================================"
				Escribir "                  SACOS WILO                          "
				Escribir "======================================================"
				Escribir "   En: Facturar                		    ",FechaActual()
				Escribir "        Gracias por comprar en Sacos Wilo!            "
				Escribir "======================================================"
				
		
		
		FinSegun


	
	
	
FinAlgoritmo
