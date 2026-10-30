#Objetivos de la semana: Introducir la estructura de datos en memoria mediante arreglos unidimensionales (vectores). 
# Aplicar las operaciones básicas con vectores: inicialización, carga de datos por teclado y recorrido.

#Ningún torneo empieza con los jugadores ya anotados por arte de magia. 
# Nuestro sistema necesita un módulo de inscripción para que el juez registre 
# a los competidores antes de repartir puntos.

#Para poder poner en marcha el torneo, lo primero que necesitamos del sistema es
#poder cargar a los jugadores y luego armar las parejas que van a
#competir. Recuerden que en el pádel se juega de a dos: ninguna pareja puede
#tener más ni menos de 2 jugadores.

#a) Ingreso de jugadores

#Al iniciar el programa, el sistema debe preguntarle al juez: "¿Cuántos jugadores van a participar en el torneo?".
# A partir de esa respuesta, debe permitir registrar cada competidor, uno por uno, con la siguiente información:
# su nombre (con el que se lo identificará dentro del torneo), y
# su categoría (el nivel en el que juega, por ejemplo 4ª, 5ª o 6ª).

#b) Armado de parejas

# Una vez cargados todos los jugadores, el sistema debe permitir formar las parejas del torneo.
# Cada pareja debe tener:
# un nombre que la identifique dentro del torneo (por ejemplo,"Los Tanos"), 
# y exactamente 2 jugadores, elegidos entre los que ya fueron inscriptos.

import json

def cargar_jugadores():
    jugadores = []
    cantidad_jugadores = int(input("¿Cuántos jugadores van a participar en el torneo? "))
    
    for i in range(cantidad_jugadores):
        nombre = str(input(f"Ingrese el nombre del jugador {i + 1}: "))
        categoria = (input(f"Ingrese la categoría del jugador {i + 1} (por ejemplo, 4ª, 5ª o 6ª): "))
        jugador = {"nombre": nombre, "categoria": categoria}
        jugadores.append(jugador)
    return jugadores

def guardar_jugadores(jugadores):
    with open("jugadores.json", "w", encoding="utf-8") as archivo:
        json.dump(jugadores, archivo, ensure_ascii=False, indent=4)

def leer_jugadores():
    with open("jugadores.json", "r", encoding="utf-8") as archivo:
        return json.load(archivo)

#APLICAMOS ORDENAMIENTO
def ordenar_seleccion_alfabetico(jugadores):
    #ordenamos la lista de jugadores por nombre en orden alfabetico
    comparaciones=0
    intercambios=0
    n=len(jugadores)

    for i in range(n-1):
        pos_min= i
        for j in range(i + 1, n):
            comparaciones += 1
            #orden alfabetico creciente
            if jugadores[j]["nombre"] < jugadores[pos_min]["nombre"]:
                pos_min = j

        if pos_min != i:
            jugadores[i], jugadores[pos_min] = jugadores[pos_min], jugadores[i]
            intercambios += 1
    return comparaciones, intercambios

def ordenar_burbuja_categoria(jugadores):
    #ordenamos la lista de jugadores por categoria en orden alfabetico
    comparaciones=0
    intercambios=0
    n=len(jugadores)
    hubo_intercambio=True
    i=0

    while i<n-1 and hubo_intercambio:
        hubo_intercambio=False
        for j in range(n-1-i):
            comparaciones+=1

            cat1=jugadores[j]["categoria"]
            cat2=jugadores[j+1]["categoria"]
            nom1=jugadores[j]["nombre"]
            nom2=jugadores[j+1]["nombre"]

            #si la categoria es mayor, o si empatan pero el nombre es mayor alfabeticamente
            if cat1>cat2 or (cat1==cat2 and nom1>nom2):
                intercambios+=1
                jugadores[j], jugadores[j+1] = jugadores[j+1], jugadores[j]
                hubo_intercambio=True
        i+=1
    return comparaciones, intercambios

def ordenar_seleccion_descendente(parejas):
    n=len(parejas)
    for i in range(n-1):
        pos_max=i
        for j in range(i+1, n):
            #bsuca el puntaje mayor para ponerlo primero
            if parejas[j]["puntos"]>parejas[pos_max]["puntos"]:
                pos_max=j
        if pos_max!=i:
            parejas[i], parejas[pos_max]=parejas[pos_max], parejas[i]

def guardar_parejas(parejas):
    with open("parejas.json", "w", encoding="utf-8") as archivo:
        json.dump(parejas, archivo, ensure_ascii=False, indent=4)


def leer_parejas():
    with open("parejas.json", "r", encoding="utf-8") as archivo:
        return json.load(archivo)        
    

def main():
    #carga inicial
    print("Inscripcion al Torneo de Paddle")
    jugadores = cargar_jugadores()
    guardar_jugadores(jugadores)
    jugadores = leer_jugadores()

#ordenamiento alfabetico de jugadores por nombre con seleccion
    print("\nOrden alfabetico (seleccion)")
    jugadores_ordenados=jugadores.copy()
    comp_sel, interc_sel= ordenar_seleccion_alfabetico(jugadores_ordenados)

    #extraemos solo los nombres para imprimirlos en orden alfabetico
    nombres_ordenados=[]
    for jugador in jugadores_ordenados:
        nombres_ordenados.append(jugador["nombre"])
    print(", ".join(nombres_ordenados))

    #ordenamiento por categoria con burbuja
    print("\nOrden por categoria (burbuja)")
    jugadores_ordenados=jugadores.copy()
    comp_bur, interc_bur=ordenar_burbuja_categoria(jugadores_ordenados)

#mostrar agrupado por categoria
    categorias_vistas = []
    for jugador in jugadores_ordenados:
        categoria = jugador["categoria"]
        if categoria not in categorias_vistas:
            categorias_vistas.append(categoria)
            print(f"\nCategoría {categoria}:")
            jugadores_categoria = []
            for j in jugadores_ordenados: # Acá tenías el error, es iterando sobre los jugadores
                if j["categoria"] == categoria:
                    jugadores_categoria.append(j["nombre"])
            print(", ".join(jugadores_categoria))

    # Cargar parejas, guardar en JSON y mostrar posiciones (CORREGIDO)
    print("\nTabla de Posiciones:")
    
    # 1. Cargamos las parejas hardcodeadas (como pide el PDF)
    parejas_nuevas = [
        {"pareja": "Los Tanos", "jugadores": ["Martin Gomez", "Lucas Peralta"], "puntos": 6},
        {"pareja": "Las Leonas", "jugadores": ["Sofia Ruiz", "Valentina Sosa"], "puntos": 9},
        {"pareja": "Doble Falta", "jugadores": ["Diego Acosta", "Camila Diaz"], "puntos": 3}
    ]

    # 2. Guardamos directamente en el archivo JSON
    guardar_parejas(parejas_nuevas)

    # 3. Leemos del archivo recién guardado y ordenamos de mayor a menor
    posiciones = leer_parejas()
    ordenar_seleccion_descendente(posiciones)

    # 4. Imprimimos la tabla
    print("\nPuesto | Pareja | Puntos")
    for i in range(len(posiciones)):
        pareja = posiciones[i]
        print(f"{i + 1} | {pareja['pareja']} | {pareja['puntos']}")

#Tabla comparativa
    print("\nTabla de Rendimiento:")
    print(f"1. Orden Alfabetico (Seleccion): Comparaciones: {comp_sel} | Intercambios: {interc_sel}")
    print(f"2. Por Categoria (Burbuja): Comparaciones: {comp_bur} | Intercambios: {interc_bur}")

main()

