#pedir al usuario un numero y decir si ese numero es positivo, negativo o cero

num= int(input("Ingrese un numero: "))  #pedir al usuario que ingrese un numero y almacenarlo en la variable num

if num > 0:                             #ver si el numero ingresado es mayor que cero
    print("El numero es positivo")
elif num < 0:                           #ver si el numero ingresado es menor que cero
    print("El numero es negativo")
else:                                   #ver si el numero ingresado es igual a cero
    print("El numero es cero")
