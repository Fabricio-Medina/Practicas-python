print ("======================")
print ("Sistema de descuentos.")
print ("====================== \n")
nombre = input ("Introduce tu nombre: ")
precio = float (input ("Precio del producto 1: "))
precio_1 = float (input ("Precio del producto 2: "))
precio_2 = float (input ("Precio del producto 3: "))
subtotal = precio + precio_1 + precio_2
membresia = input ("Cuenta con membresia? (si/no): ")
membresia = membresia.lower()
print ("================")
print ("TICKET DE COMPRA")
print ("================")
print ("Cliente: ", nombre)
if subtotal == 0 and membresia == "no":
        print ("Introduce un valor que no sea igual a 0.")
elif subtotal == 0 and membresia == "si":
        print ("Introduce un valor que no sea igual a 0.")
elif subtotal >= 2000:
    print ("Total", subtotal)
    descuento = subtotal * 0.10
    print ("Se le hara un descuento de: ", descuento)
    subtotal -= descuento
    print ("Total: ", subtotal)
    if membresia == "si":
        descuento_1 = subtotal * 0.05
        print ("Se le hara un descuento del 5% por contar con membresia: ", descuento_1)
        subtotal -= descuento_1
        print ("Total: ", subtotal)
elif subtotal < 2000 and subtotal > 0:
    print ("Total: ", subtotal)
    if membresia == "si":
        descuento_2 = subtotal * 0.05
        print ("Se le hara un descuento del 5% por contar con membresia: ", descuento_2)
        subtotal -= descuento_2
        print ("Total: ", subtotal)
else:
    print ("Dato invalido")
