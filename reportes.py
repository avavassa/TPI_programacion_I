"""
Módulo reportes.py

Funciones de salida y análisis de datos:
- mostrar_tabla_paises(): Muestra lista formateada de países.
- buscar_pais_nombre(): Busca países por coincidencia en el nombre.
- filtrar_paises(): Filtra por continente, rango de población o superficie.
- ordenar_paises(): Ordena la lista usando algoritmo de burbuja.
- mostrar_estadisticas(): Calcula promedios, máximos, mínimos y conteo por continente.
"""

from utilidades import normalizar_texto

def mostrar_tabla_paises(lista_paises):
    """Muestra de manera formateada la lista de países en consola."""
    if not lista_paises:
        print("No hay registros para mostrar.")
        return
    # Encabezado    
    print("\n" + "-" * 75)
    print(f"{'Nombre':<20} | {'Población':<15} | {'Superficie (km2)':<16} | {'Continente':<15}")
    print("-" * 75)
    for pais in lista_paises: # Recorre la lista e imprime datos
        print(f"{pais['nombre']:<20} | {pais['poblacion']:<15} | {pais['superficie']:<16} | {pais['continente']:<15}")
    print("-" * 75 + "\n")

def buscar_pais_nombre(lista_paises):
    """Busca países por coincidencia exacta o parcial en el nombre."""
    print("\n--- BUSCAR PAÍS ---")
    criterio = input("Ingrese el nombre (o parte del nombre) a buscar: ").strip().lower()
    criterio_norm = normalizar_texto(criterio)  # Normaliza texto para busqueda efectiva
    
    if not criterio:
        print("Error: El criterio de búsqueda no puede estar vacío.")
        return
        
    coincidencias = [] # Crea una lista de coincidencias
    for pais in lista_paises: # Recorre lista buscando coincidencias y las guarda si encuentra
        if criterio_norm in pais["nombre_norm"]:
            coincidencias.append(pais)
            
    if coincidencias: # Si hay elementos en la lista de coincidencias, los muestra
        print(f"\nSe encontraron {len(coincidencias)} coincidencias:")
        mostrar_tabla_paises(coincidencias)
    else:
        print("No se encontraron países con ese criterio de búsqueda.")

def filtrar_paises(lista_paises):
    """Filtra los países según continente, rangos de población o rangos de superficie."""
    if not lista_paises:
        print("No hay datos para aplicar filtros.")
        return
    # Muestra opciones de filtrado
    print("\n=== OPCIONES DE FILTRADO ===")
    print("1. Filtrar por Continente")
    print("2. Filtrar por Rango de Población")
    print("3. Filtrar por Rango de Superficie")
    opcion = input("Seleccione tipo de filtro (1-3): ").strip()
    
    resultados = [] # Crea una lista de resultados
    
    if opcion == "1": # Filtrado por continente
        continente = input("Ingrese el continente a filtrar: ").strip()
        continente_norm = normalizar_texto(continente) # Normaliza el ingreso para búsqueda
        for p in lista_paises:
            if p["continente_norm"] == continente_norm: # Compara ingreso con campo continente normalizado
                resultados.append(p) # Agrega a lista resultados si encuentra coincidencias

    elif opcion == "2": # Filtrado por población
        try: # Solicita al usuario el rango de población
            min_pob = int(input("Población mínima: "))
            max_pob = int(input("Población máxima: "))
            if min_pob > max_pob: # Verifica consistencia de los datos ingresados
                print("Error: El valor mínimo no puede ser mayor al máximo.")
                return
            for p in lista_paises: # Recorre la lista de países
                if min_pob <= p["poblacion"] <= max_pob: # Identifica poblaciones entre el rango establecido
                    resultados.append(p) # Agrega a la lista de resultados
        except ValueError:
            print("Error: Los rangos deben ser números enteros.")
            return
            
    elif opcion == "3": # Filtrado por superfície
        try: # Solicita al usuario el rango de superfície
            min_sup = int(input("Superficie mínima (km2): "))
            max_sup = int(input("Superficie máxima (km2): "))
            if min_sup > max_sup: # Verifica consistencia de los datos ingresados
                print("Error: El valor mínimo no puede ser mayor al máximo.")
                return
            for p in lista_paises:
                if min_sup <= p["superficie"] <= max_sup: # Identifica superfícies entre el rango establecido
                    resultados.append(p)
        except ValueError:
            print("Error: Los rangos deben ser números enteros.")
            return
    else:
        print("Opción de filtrado no válida.")
        return
        
    if resultados: # Muestra resultados si la lista no está vacía
        mostrar_tabla_paises(resultados)
    else:
        print("Ningún país cumple con los criterios del filtro aplicado.")

def ordenar_paises(lista_paises):
    """Ordena una copia de la lista usando el algoritmo de ordenamiento Burbuja (Múltiple criterio)."""
    if not lista_paises:
        print("No hay datos para ordenar.")
        return
    # Muestra menu de opciones de ordenamiento
    print("\n=== OPCIONES DE ORDENAMIENTO ===")
    print("1. Ordenar por Nombre")
    print("2. Ordenar por Población")
    print("3. Ordenar por Superficie")
    criterio = input("Seleccione criterio (1-3): ").strip()
    
    if criterio not in ["1", "2", "3"]:
        print("Criterio inválido.")
        return
    # Pide el sentido del ordenamiento
    print("1. Ascendente")
    print("2. Descendente")
    sentido = input("Seleccione sentido (1-2): ").strip()
    
    if sentido not in ["1", "2"]:
        print("Sentido inválido.")
        return
    # Determina la clave de ordenamiento: si 1 nombre, si 2 población, sino superficie:
    clave = "nombre_norm" if criterio == "1" else ("poblacion" if criterio == "2" else "superficie")
    
    lista_ordenada = list(lista_paises) # Crea una copia de la lista para que no se modifique la original al ordenar
    n = len(lista_ordenada)

    for i in range(n): # Bucle externo: controla cuantas pasadas se debe hacer
        for j in range(0, n - i - 1): # Bucle interno: recorre comparando elementos vecinos, a cada pasada hace una comparación
                                      # menos porque ya se ordenó
            valor_actual = lista_ordenada[j][clave]
            valor_siguiente = lista_ordenada[j+1][clave]
            
            intercambiar = False
            if sentido == "1" and valor_actual > valor_siguiente: # Si el sentido es ascendente y el valor actual es mayor al siguiente
                intercambiar = True                               # se debe intercambiarlos
            elif sentido == "2" and valor_actual < valor_siguiente: # Si el sentido es descendente, al contrario
                intercambiar = True
                
            if intercambiar: # Intercambio de posiciones
                lista_ordenada[j], lista_ordenada[j+1] = lista_ordenada[j+1], lista_ordenada[j]
                
    mostrar_tabla_paises(lista_ordenada)

def mostrar_estadisticas(lista_paises):
    """Calcula y muestra indicadores estadísticos requeridos a partir del dataset."""
    if not lista_paises:
        print("No hay datos suficientes para calcular estadísticas.")
        return
        
    print("\n==================================================")
    print("             ESTADÍSTICAS GENERALES               ")
    print("==================================================")
    # Inicializacióon de variables
    pais_max_pob = lista_paises[0] 
    pais_min_pob = lista_paises[0]
    
    suma_poblacion = 0
    suma_superficie = 0
    conteos_continente = {} # Crea un diccionario vacío para conteo de continentes
    
    for pais in lista_paises: # Recorre la lista de países
        suma_poblacion += pais["poblacion"] # Suma poblaciones totales
        suma_superficie += pais["superficie"] # Suma superficies totales
        
        if pais["poblacion"] > pais_max_pob["poblacion"]: # Compara población con máxima
            pais_max_pob = pais                           # si es mayor, guarda el nombre del país
        if pais["poblacion"] < pais_min_pob["poblacion"]: # Compara población con mínima
            pais_min_pob = pais                           # si es menor, guarda el nombre del país
            
        cont = pais["continente_norm"].capitalize() # Obtiene el valor de la clave continente_norm
        conteos_continente[cont] = conteos_continente.get(cont, 0) + 1 # Incrementa el contador del continente; si no existe, comienza en 0
                                                                       
    total_paises = len(lista_paises)
    promedio_pob = suma_poblacion / total_paises # Cálculo de promedio de población
    promedio_sup = suma_superficie / total_paises # Cálculo de promedio de superficie
    
    print(f"País con MAYOR población: {pais_max_pob['nombre']} ({pais_max_pob['poblacion']} hab.)")
    print(f"País con MENOR población: {pais_min_pob['nombre']} ({pais_min_pob['poblacion']} hab.)")
    print(f"Promedio de población global: {promedio_pob:.2f} habitantes")
    print(f"Promedio de superficie global: {promedio_sup:.2f} km2")
    
    print("\nCantidad de países por continente:")
    for continente, cantidad in conteos_continente.items(): # Para cada tupla en el diccionario conteos_continente
        print(f" -> {continente}: {cantidad}")              # imprime valores
    print("==================================================\n")