Algoritmo PesosADolar
	
	// Definir variables globales
	Definir pesos, tasaCambio, resultado Como Real;
	
	// Mostrar mensaje al usuario
	Escribir "Ingresa la cantidad de pesos colombianos:";
	// Capturar datos
	Leer pesos;
	
	// Mostrar mensaje al usuario
	Escribir "Ingresa la tasa de cambio para el d�lar:";
	// Capturar datos
	Leer tasaCambio;
	
	// Convertir pesos a d�lares
	resultado <- pesos / tasaCambio;
	
	// Mostrar resultado
	Escribir "La cantidad de d�lares equivalentes es: ", resultado;
	
FinAlgoritmo
