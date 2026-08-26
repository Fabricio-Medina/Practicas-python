nums = []
print ("Introduce 5 numeros enteros.")
for add in range (5):
    num = int (input ("Introduce un numero: "))
    nums.append(num)

while True:
    mayor = nums[0]#variable mayor, que almacena el primer numero de la lista
    menor = nums[0]#variable menor, que igualmente almacena el primer numero ya que mayor se modificara y no regresara a su valor original.
    suma = 0
    string = "ANALIZADOR DE SECUENCIAS"
    print (f"\n{string.center(46, '=')}\nLista actual: {nums}")
    menu = int (input("1.Agregar un numero.\n2.Eliminar un numero.\n3.Mostrar informacion de la lista.\n4.Contar un numero.\n5.Analizar secuencia.\n6.Mostrar lista.\n7.Salir\nQue opcion deseas?: "))
    if menu == 1:
        num = int (input("Que numero deseas agregar: "))
        nums.append(num)  
    elif menu == 2:
        eliminate = int (input("Que numero deseas eliminar: "))
        if nums.count(eliminate) < 1:
            print (f"El numero {eliminate} no se encuentra en la lista {nums}.")
        for eliminar in range(nums.count(eliminate)):
               nums.remove(eliminate)        
    elif menu == 3:
        print (f"Cantidad de numeros: {len(nums)}")
        for numeros in nums:
            if numeros > mayor:
                mayor = numeros#Primero guarda temporalmente el primer valor de la lista en numeros, despues verifica si numeros es mayor que la variable 'mayor'
                               # Como numeros es mayor que la variable 'mayor', entonces guarda el valor de el numero que sigue de la lista en la variable 'mayor'
                               #Y cuando no se cumple esa funcion, if deja de ejecutarse y se imprime la variable 'mayor' con el ultimo numero guardado.

            if numeros < menor:#Con for se guarda temporalmente el primer elemento de la lista en la variable 'numeros', despues verifica si la variable  'numeros es menor a
                               #la variable 'menor', como se cumple la condicion, se guarda el valor de 'numeros' dentro de la variable menor, sucesivamente hasta que se deje
                               #de cumplir la condicion y se imprime en pantalla el ultimo valor guardado en 'menor'.
                menor = numeros
        for numeros in nums:
            suma += numeros
        print (f"Mayor: {mayor}\nMenor: {menor}\nSuma: {suma}\nPromedio: {suma / len(nums)}")
    elif menu == 4:
        conteo = int (input("Que numero quieres contar?: "))
        if nums.count(conteo) >= 1:
            print (f"El numero {conteo}, se repite {nums.count(conteo)} veces.")
        else:
            print (f"El numero {conteo} no se encuentra dentro de la lista {nums}")
    elif menu == 5:
        if len(nums) <= 1:
            print (f"Tu secuencia {nums} tiene que tener minimo dos numeros.")
            continue
        anterior = nums[0]
        resultado = nums[1] - nums[0]
        verificacion = True 
        for actual in nums[1:]:
            resultado1 = actual - anterior
            anterior = actual
            if resultado != resultado1:
                verificacion = False
                break
        if verificacion:
                print (f"Tu secuencia {nums} cuenta con una progresion aritmetica de {resultado}.")
        else:
            print (f"Tu secuencia {nums} no cuenta con una progresion aritmetica.")
    elif menu == 6:
        print (f"Lista actual: {nums}")
    elif menu == 7:
        print ("Hasta luego.")
        break
    else:
        print (f"Esta opcion no existe")
        
