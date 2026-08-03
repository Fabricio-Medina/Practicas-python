nombre = input ("Introduce tu nombre: ")
cont = input ("Antes de continuar, quieres seguir (si/no): ")
cont = cont.lower()
boletoN, boletoA = 70, 120
total_boletosN = 0
total_boletosA = 0
total_1 = total_boletosN + total_boletosA
total_2 = 0
while cont == "si":
    print ("================")
    print ("MENU DE OPCIONES")
    print ("================")
    print ("\n 1. Comprar Boletos\n 2. Ver resumen de compra.\n 3. Salir \n")
    opcion = int (input ("Selecciona tu opcion: "))
    
    if opcion == 1:
        print ("Boleto niño $", boletoN)
        print ("Boleto adulto $", boletoA)
        pregunta = input ("Boleto para niño, (si/no): ")
        pregunta1 = input ("Boleto para adulto, (si/no): ")
        pregunta = pregunta.lower()
        pregunta1 = pregunta1.lower()
        if pregunta == "si" and pregunta1 == "si":
            total_boletosN += int (input ("Boletos niño: "))
            total_boleto = total_boletosN * boletoN
            total_boletosA += int (input ("Boletos adulto: "))
            total_boleto2 = total_boletosA * boletoA
            total_0 = total_boleto + total_boleto2
            
            if total_boletosN >= 1 and total_boletosA >= 1:
                 print ("Total $", total_0)
            elif total_boletosN <= 0 or total_boletosA <=0:
                print ("Esta cantidad de boletos no es valida.")
            
            
        elif pregunta == "no" and pregunta1 == "si":
            total_boletosA += int (input ("Boletos adulto: "))
            total_2 += total_boletosA * boletoA
            if total_boletosA >= 1:
                 print ("Total $", total_2)
            elif total_boletosA <= 0:
                print ("Esta cantidad de boletos no es valida.")
            
        elif pregunta == "si" and pregunta1 == "no":
            print ("\nNecesitas un acompañante adulto.")
            print ("Presiona 1. si")
            print ("Presiona 2. no \n")
            intento = int (input ("Que opcion deseas: "))
            if intento == 2:
                print ("Gracias por visitarnos.")
                break
                
            elif intento == 1:
                print ("Boleto niño $", boletoN)
                print ("Boleto adulto $", boletoA)
                pregunta = input ("Boleto para niño, (si/no): ")
                pregunta1 = input ("Boleto para adulto, (si/no): ")
                pregunta = pregunta.lower()
                pregunta1 = pregunta1.lower()
                
                if pregunta == "si" and pregunta1 == "si":
                    
                    total_boletosN += int (input ("Boletos niño: "))
                    total_boleto = total_boletosN * boletoN
                    total_boletosA += int (input ("Boletos adulto: "))
                    total_boleto2 = total_boletosA * boletoA
                    total_0 = total_boleto + total_boleto2
                    total += total_boletosN
                    if total_boletosN >= 1 and total_boletosA >= 1:
                        print ("Total $", total_0)
                    elif total_boletosN <= 0 or total_boletosA <=0:
                        print ("Esta cantidad de boletos no es valida.")
                    
                elif pregunta == "no" and pregunta1 == "si":
                    
                    total_boletosA += int (input ("Boletos adulto: "))
                    total_2 += total_boletosA * boletoA
                    if total_boletosA >= 1:
                         print ("Total $", total_2)
                    elif total_boletosA <= 0:
                        print ("Esta cantidad de boletos no es valida.")
                    
                elif pregunta == "si" and pregunta1 == "no":
                    print ("\nNecesitas un acompañante adulto.")
                    print ("Presiona 1. si")
                    print ("Presiona 2. no \n")
                    intento = int (input ("Que opcion deseas: "))
                    if intento == 2:
                        print ("Gracias por visitarnos")
                        break
                        
    elif opcion == 2:
        print ("=================")
        print ("RESUMEN DE COMPRA")
        print ("=================")
        if total_1 >= 1:
            print ("Cliente: ", nombre)
            print ("Total boletos adulto: ", total_boletosA)    
            print ("Total boletos niño: ", total_boletosN) 
            print ("Total: ", total_1)
        elif total_1 == 0:
            print ("Cliente: ", nombre)
            print ("Total boletos adulto: ", total_boletosA)     
            print ("Total: ", total_2)
        else:
            print ("Aun no se realizan compras: ")
    elif opcion == 3:
        print ("Gracias por tu visita, hasta luego.")
        break
    else:
        print ("Opcion no disponible.")

            
        
                               




    

    
                        
            
        
        
    
    
