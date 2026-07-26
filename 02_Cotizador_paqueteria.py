print ("Bienvenido(a) a la paqueteria")
nombre = input ("Cual es tu nombre?: ")
peso = float (input (nombre + " Cuanto pesa tu paquete: "))
envio = int (input ("Quiere un envio expres?, escribe 1 para Si y 2 para No: "))
costo = 100
costo_pesado = 200
if envio == 1 and peso <= 5:
    extra = costo + 50
    print (nombre + " el costo de su entrega es de: $", extra)
if envio == 1 and peso > 5:
    extra = costo_pesado + 50
    print (nombre + " el costo de su entrega es de: $", extra)
if envio == 2 and peso <= 5:
 print (nombre + " el costo de su entrega es de: $", costo)
if envio == 2 and peso > 5:
    print (nombre + " el costo de su entrega es de: $", costo_pesado)
