print ("================")
print ("Sistema de becas")
print ("================")
nombre = input ("Cual es tu nombre?: ")
edad = int (input ("Cual es tu edad?: "))
promedio = float (input ("Cual es tu promedio?: "))
if edad < 15:
    print("No cumples con la edad minima.")
    
elif edad >= 15:
    if promedio >= 9.5:
        print ("Recibe beca completa.")
    elif promedio >= 8.5 and promedio < 9.50:
        actividad = input (nombre + " participas en actividades extracurriculares, si o no?: ")
        actividad = actividad.lower()
        
        if actividad == "si":
            print ("Recibe beca parcial.")
        else:
            print ("Buen promedio pero necesitas partipar en actividades extracurriculares.")
    else:
        print ("No cumples con el promedio necesario " + nombre)

    
print ("Nos dio gusto conocerte " + nombre + " ten un buen dia.")
         
    
