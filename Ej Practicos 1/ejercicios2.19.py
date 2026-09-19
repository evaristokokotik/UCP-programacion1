#Una panadería vende el kg pan a $500. El pan que no es del día tiene un descuento del
#60%. Escribir un programa que comience leyendo cuantos kg que no son del día vendió.
#Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que
#se le hace por no ser pan del día y el costo final total.

kg_pan = float(input("Ingrese la cantidad de kg de pan que no son del día vendidos: "))
precio = 500 * kg_pan
descuento = precio * 0.6
costo_final = precio - descuento
print("El precio habitual de una barra de pan es:", round(precio, 2))
print("El descuento que se le hace por no ser pan del día es:", round(descuento, 2))
print("El costo final total es:", round(costo_final, 2))