print ("=================")
print ("CAJERO AUTOMATICO")
print ("================= \n")
nombre = input ("Cliente: ")
saldo = float (input ("Cual es tu saldo actual: "))
print ("\n================")
print ("MENU DE OPCIONES")
print ("================")
print ("1. Consultar saldo")
print ("2. Depositar")
print ("3. Retiro")
print ("4. Salir")
opcion = int (input ("Elige tu opcion: "))
if opcion == 1:
    print ("Su saldo actual es: ", saldo)
elif opcion == 2:
    deposito = float (input ("Cuanto dinero deseas depositar: "))
    if deposito > saldo:
        print ("Cantidad invalida.")
    if deposito < saldo:
        saldo += deposito
        print ("Tu saldo actual es: ", saldo) 
    elif deposito <= 0:
        print ("No se puede depositar esta cantidad")
elif opcion == 3:
    retiro = float (input ("Cuanto dinero desea retirar: "))
    if retiro == saldo:
        pregunta = input ("Estas seguro de retirar todo (si/no): ")
        pregunta = pregunta.lower()
        if pregunta == "si":
            saldo -= retiro
            print ("Su saldo actual es: ", saldo)
        elif pregunta == "no":
            print ("Gracias por preferir nuestros servicios.")
    elif saldo <= retiro:
        saldo -= retiro
        print ("Su saldo actual es: ", saldo )
    
elif opcion == 4:
    print ("Gracias por preferir nuestros servicios ", nombre, "hasta pronto.")
else:
    print ("Opcion no valida")
repetir = input ("Desea volver a seleccionar otra opcion (si/no): ")
repetir = repetir.lower()
if repetir == "no":
    print ("Gracias por preferir nuestros servicios ", nombre, "hasta pronto.")
    
while repetir == "si":
    print ("\n================")
    print ("MENU DE OPCIONES")
    print ("================")
    print ("1. Consultar saldo")
    print ("2. Depositar")
    print ("3. Retiro")
    print ("4. Salir")
    opcion = int (input ("Elige tu opcion: "))
    if opcion == 1:
        print ("Su saldo actual es: ", saldo)
    elif opcion == 2:
        deposito = float (input ("Cuanto dinero deseas depositar: "))
        if deposito > saldo:
            print ("Cantidad invalida.")
        if deposito < saldo:
            saldo += deposito
            print ("Tu saldo actual es 222: ", saldo) 
        elif deposito <= 0:
            print ("No se puede depositar esta cantidad")
    elif opcion == 3:
        retiro = float (input ("Cuanto dinero desea retirar: "))
        if retiro == saldo:
            pregunta = input ("Estas seguro de retirar todo (si/no): ")
            pregunta = pregunta.lower()
            if pregunta == "si":
                saldo -= retiro
                print ("Su saldo actual es: ", saldo)
            elif pregunta == "no":
                print ("Gracias por preferir nuestros servicios.")
        elif saldo <= retiro:
            saldo -= retiro
            print ("Su saldo actual es: ", saldo )
    
    elif opcion == 4:
        print ("Gracias por preferir nuestros servicios ", nombre, "hasta pronto.")
    else:
        print ("Opcion no valida")
    repetir = input ("Desea volver a seleccionar otra opcion (si/no): ")
    repetir = repetir.lower()
    if repetir == "no":
        print ("Gracias por preferir nuestros servicios ", nombre, "hasta pronto.")

