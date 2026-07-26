print ("Calculadora de potencias")
nombre = input ("Bienvenido(a), Cual es tu nombre?: ")
print (nombre + " ahora vamos a elevar los numeros enteros que quieras a la potencia que sea.")
numero = int (input ("Escribe el numero que quieres elevar: "))
potencia = int (input ("Ahora escribe el numero de la potencia o exponente: "))
resultado = numero ** potencia
print (nombre + " el resultado es: ", resultado)
