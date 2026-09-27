import os

# VARIABLE GLOBAL: Arreglo de diccionarios para el catálogo[cite: 2]
catalogo = [
    {"codigo": 101, "nombre": "Café con leche", "precio": 1500},
    {"codigo": 102, "nombre": "Medialuna", "precio": 700},
    {"codigo": 103, "nombre": "Sándwich de miga", "precio": 1800},
    {"codigo": 104, "nombre": "Agua mineral 500 ml", "precio": 1000},
    {"codigo": 105, "nombre": "Empanada", "precio": 1200},
    {"codigo": 106, "nombre": "Chipá (100 g)", "precio": 1300}
]

#3 FUNCIONES (Devuelven un valor)

def buscar_precio(codigo):
    # Recibe el código y devuelve su precio asociado
    for producto in catalogo:
        if producto["codigo"] == codigo:
            return producto["precio"]
    return 0

def calcular_recaudacion_diaria(matriz, dia_idx):
    # Recibe la matriz y el índice del día, devuelve el total en pesos
    total = 0
    for i in range(6):
        total = total + (matriz[i][dia_idx] * catalogo[i]["precio"])
    return total

def obtener_mas_vendido(matriz):
    # Recibe la matriz y devuelve el nombre del producto más vendido
    max_ventas = -1
    mas_vendidos = [] 
    
    for i in range(6):
        # Sumar toda la fila para obtener el total del producto
        suma_unidades = 0
        for j in range(5):
            suma_unidades = suma_unidades + matriz[i][j]
            
        # Manejo de empates guardando en un arreglo auxiliar
        if suma_unidades > max_ventas:
            max_ventas = suma_unidades
            mas_vendidos = [catalogo[i]["nombre"]]
        elif suma_unidades == max_ventas and suma_unidades > 0:
            mas_vendidos.append(catalogo[i]["nombre"])
            
    return mas_vendidos


#3 PROCEDIMIENTOS (No devuelven nada)

def mostrar_menu():
    # No recibe parámetros, solo imprime las opciones
    print("\nMENU PRINCIPAL")
    print("1. Ver catálogo")
    print("2. Registrar una venta")
    print("3. Ver informes semanales")
    print("4. Salir")

def guardar_datos(dia, codigo, cantidad):
    # Recibe datos para escribir su contenido físico en el archivo de texto
    # Se abre en modo "a" (append) para agregar sin borrar lo anterior
    archivo = open("ventas_semana.txt", "a")
    archivo.write(str(dia) + "," + str(codigo) + "," + str(cantidad) + "\n")
    archivo.close()

def registrar_venta(matriz):
    # Recibe la matriz para actualizar sus cantidades tras el ingreso por teclado
    dia = int(input("Ingrese el día (1=Lunes a 5=Viernes): "))
    if dia < 1 or dia > 5:
        print("Día incorrecto.")
        return

    codigo = int(input("Ingrese el código del producto: "))
    cantidad = int(input("Ingrese la cantidad: "))

    indice_prod = -1
    # Bucle for con validación y salida interna usando break
    for i in range(len(catalogo)):
        if catalogo[i]["codigo"] == codigo:
            indice_prod = i
            break
            
    # Si el código es válido, se suma a la matriz y se guarda en el archivo
    if indice_prod != -1:
        matriz[indice_prod][dia - 1] = matriz[indice_prod][dia - 1] + cantidad
        # Guardado inmediato después de cada venta registrada para evitar pérdida de datos
        guardar_datos(dia, codigo, cantidad)
        print("Venta registrada exitosamente.")
    else:
        print("Error: El código ingresado no existe.")


# PROCEDIMIENTOS AUXILIARES Y BLOQUE PRINCIPAL

def inicializar_datos(matriz):
    # Reconstruye la matriz leyendo el archivo secuencialmente
    if os.path.exists("ventas_semana.txt"):
        archivo = open("ventas_semana.txt", "r")
        for linea in archivo:
            dia, codigo, cantidad = map(int, linea.strip().split(","))
            for i in range(6):
                if catalogo[i]["codigo"] == codigo:
                    matriz[i][dia - 1] = matriz[i][dia - 1] + cantidad
                    break
        archivo.close()
    else:
        # Si el archivo es inexistente, crea uno nuevo en blanco
        archivo = open("ventas_semana.txt", "w")
        archivo.close()

def mostrar_informes(matriz):
    print("\n INFORME SEMANAL")
    no_vendidos = []
    
    # 1. Unidades de cada producto y 4. Productos no vendidos
    print("Unidades vendidas por producto:")
    for i in range(6):
        suma_unidades = sum(matriz[i])
        print("- " + catalogo[i]["nombre"] + ": " + str(suma_unidades))
        if suma_unidades == 0:
            no_vendidos.append(catalogo[i]["nombre"])
            
    # 2. Recaudación por día y 5. Recaudación total
    print("\n Recaudación por día:")
    nombres_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    total_semana = 0
    max_rec_dia = -1
    dia_top = ""
    
    for j in range(5):
        rec_dia = calcular_recaudacion_diaria(matriz, j)
        print("- " + nombres_dias[j] + ": $" + str(rec_dia))
        total_semana = total_semana + rec_dia
        if rec_dia > max_rec_dia:
            max_rec_dia = rec_dia
            dia_top = nombres_dias[j]
            
    # 3. Producto más vendido y día de mayor recaudación
    mas_vendidos = obtener_mas_vendido(matriz)
    print("\n Producto/s más vendido/s: " + str(mas_vendidos))
    print("Día de mayor recaudación: " + dia_top)
    
    print("Productos sin ventas: " + str(no_vendidos))
    print("Recaudación TOTAL: $" + str(total_semana))


def main():
    # Variable local: Matriz de 6 filas por 5 columnas inicializada en 0
    matriz_ventas = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    
    # Cargar datos previos para no perder la información al iniciar
    inicializar_datos(matriz_ventas)
    
    opcion = 0
    # Estructura while para evitar que el programa termine tras una operación
    while opcion != 4:
        mostrar_menu()
        opcion = int(input("Elija una opción: "))
        
        if opcion == 1:
            print("\nCatálogo:")
            for p in catalogo:
                print(str(p["codigo"]) + " - " + p["nombre"] + " - $" + str(p["precio"]))
        elif opcion == 2:
            registrar_venta(matriz_ventas)
        elif opcion == 3:
            mostrar_informes(matriz_ventas)
        elif opcion == 4:
            print("Cerrando programa...")
        else:
            print("Opción inválida.")

# Ejecutar programa
main()