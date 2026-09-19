#pedir al usuario que ingrese 3 numeros y que indique cual es el mayor

num1= int(input("Ingrese el primer numero: "))                  #pedir al usuario que ingrese el primer numero y almacenarlo en la variable num1
num2= int(input("Ingrese el segundo numero: "))                 #pedir al usuario que ingrese el segundo numero y almacenarlo en la variable num2
num3= int(input("Ingrese el tercer numero: "))                  #pedir al usuario que ingrese el tercer numero y almacenarlo en la variable num3

if num1 > num2 and num1 > num3:                                 #ver si el primer numero ingresado es mayor que el segundo y el tercer numero
    print("El primer numero es el mayor y es:", num1)
elif num2 > num1 and num2 > num3:                               #ver si el segundo numero ingresado es mayor que el primer y el tercer numero
    print("El segundo numero es el mayor y es:", num2)
else:
    print("El tercer numero es el mayor y es:", num3)
