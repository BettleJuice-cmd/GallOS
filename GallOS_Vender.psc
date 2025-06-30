Algoritmo GallOS_Vender
	
	Definir cliente,fecha, direccion Como Caracter
	Definir total, precioUnit, cantidadTotal como real
	Definir opcion, codigo, cantidad, opcFin,codigoSaco Como Entero
	
	Escribir "======================================================"
	Escribir "                  SACOS WILO                          "
	Escribir "======================================================"
	Escribir "   En: Facturar                		    ",FechaActual()
	
	Escribir "       ¡BIENVENIDO A LA SECCION DE VENTAS!            "
	mientras opcion<>3 Hacer
		Escribir "Por favor, seleccione la opción que desee ejecutar...."
		Escribir "1.... Nueva Ventana"
		Escribir "2.... Salir"
		leer opcion
		Segun opcion Hacer
			1:
				Dimensionar  [9]
				
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
					Escribir "Desea concluir su venta? (Digite 0 para concluir)"
					leer opcFin
				hasta que opcFin=0
			
		
		
		FinSegun
	FinMientras

	
	
	
FinAlgoritmo
