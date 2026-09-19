#Escribir el algoritmo que, a partir de la cantidad de bancos de un aula y la cantidad de
#alumnos inscriptos para un curso, permita determinar si alcanzan los bancos existentes.
#De no ser así, informar además cuántos bancos sería necesario agregar.

bancos = int(input("Ingrese la cantidad de bancos en el aula: "))
alumnos = int(input("Ingrese la cantidad de alumnos inscriptos: "))
if alumnos <= bancos:
    print("Alcanzan los bancos existentes.")
else:
    bancos_necesarios = alumnos - bancos
    print("No alcanzan los bancos existentes. Se necesitan agregar", bancos_necesarios, "bancos.")
    