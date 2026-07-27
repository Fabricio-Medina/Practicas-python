print ("=====================")
print ("Tienda de descuentos.")
print ("===================== \n")
print ("Menu de opciones: \n")
print ("Presione 1 para Ropa.")
print ("Presione 2 para Electronica. \n")
opcion =  int (input ("Cual es la opcion que deseas elegir?: "))
if opcion == 1:
    print ("\n Ha seleccionado la categoria de Ropa. \n")
    opcion_1 = input ("Necesita playera, pantalon o calzado?: ")
    opcion_1 = opcion_1.lower()
    if opcion_1 == "playera":
        print ("Tiene un 10% de descuento.")
    elif opcion_1 == "pantalon":
        print ("Tiene un 15% de descuento.")
    elif opcion_1 == "calzado":
        print ("Tiene 5% de descuento.")
    else:
        print ("No se encuentra disponible.")

elif opcion == 2:
    print ("\n Ha seleccionado la categoria de Electronica. \n")
    opcion_2 = input ("Necesita laptop o celular?: ")
    opcion_2 = opcion_2.lower()
    if opcion_2 == "laptop":
        print ("Tiene %5 de descuento")
    elif opcion_2 == "celular":
        print ("Tiene 20% de descuento")
    else:
        print ("Unidades agotadas.")
else:
    print ("Esta opcion no existe.")
     


