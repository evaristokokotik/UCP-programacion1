#Escribir el algoritmo que, a partir de la cantidad de bancos de un aula y la cantidad de
#alumnos inscriptos para un curso, permita determinar si alcanzan los bancos existentes.
#De no ser así, informar además cuántos bancos sería necesario agregar.

cantbancos= int(input("Ingrese la cantidad de bancos del aula: "))  #pedir al usuario que ingrese la cantidad de bancos del aula
cantalumnos= int(input("Ingrese la cantidad de alumnos inscriptos: "))  #pedir al usuario que ingrese la cantidad de alumnos inscriptos

bancos_necesarios = cantalumnos - cantbancos  #calcular la cantidad de bancos necesarios

if cantalumnos <= cantbancos:
    print("Los bancos existentes son suficientes.")
else:
    print(f"Los bancos existentes no son suficientes. Se necesitan agregar {bancos_necesarios} bancos.")