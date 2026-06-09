import os # Módulo nativo para manejo de archivos y rutas
import csv  # Módulo nativo para una lectura y escritura robusta
import unicodedata # Módulo nativo para normalización de nombres de países y continentes


ARCHIVO_CSV = "paises.csv"

#-------------- FUNCIONES AUXILIARES --------------#

def normalizar_texto(texto):
    """Convierte a minúsculas y elimina acentos."""
    if not texto:
        return ""
    # Descomponer caracteres acentuados en base + diacrítico
    texto = unicodedata.normalize('NFD', texto)
    # Filtrar solo caracteres no diacríticos (letras, números, espacios)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
    return texto.lower()

def verificar_e_inicializar_csv():
    """Verifica la existencia del archivo CSV y lo inicializa si no existe."""
    if not os.path.exists(ARCHIVO_CSV):
        try:
            with open(ARCHIVO_CSV, "w", encoding="utf-8", newline="") as archivo:
                escritor = csv.writer(archivo)
                # Encabezados obligatorios
                escritor.writerow(["nombre", "poblacion", "superficie", "continente"])
                # Registros base solicitados por la cátedra
                escritor.writerows([
                    ["Argentina", 45376763, 2780400, "America"],
                    ["Japón", 125800000, 377975, "Asia"],
                    ["Brasil", 213993437, 8515767, "America"],
                    ["Alemania", 83149300, 357022, "Europa"]
                ])
        except IOError:
            print("Error: No se pudo inicializar el archivo base CSV.")

def cargar_desde_csv():
    """Lee los datos desde el archivo CSV y los carga en una lista de diccionarios."""
    lista_paises = []
    verificar_e_inicializar_csv()
    
    try:
        with open(ARCHIVO_CSV, "r", encoding="utf-8") as archivo:
            # Usamos csv.DictReader para leer directamente cada fila como un diccionario
            lector = csv.DictReader(archivo)
            
            # Validamos que los encabezados sean correctos
            if lector.fieldnames and [f.strip() for f in lector.fieldnames] != ["nombre", "poblacion", "superficie", "continente"]:
                print("Error de formato: Los encabezados del archivo CSV no son válidos.")
                return lista_paises

            for i, fila in enumerate(lector, start=2):
                try:
                    # Limpieza de espacios en blanco y conversión de tipos
                    nombre = fila["nombre"].strip()
                    poblacion = int(fila["poblacion"].strip())
                    superficie = int(fila["superficie"].strip())
                    continente = fila["continente"].strip()
                    # Crea diccionario con datos originales y normalizados para busquedas efectivas
                    pais = {
                        "nombre": nombre,
                        "poblacion": poblacion,
                        "superficie": superficie,
                        "continente": continente,
                        "nombre_norm": normalizar_texto(nombre), # Agrega entrada de nombre normalizado
                        "continente_norm": normalizar_texto(continente) # Nombre continente normalizado
                    }
                    lista_paises.append(pais)
                except (ValueError, KeyError, AttributeError):
                    print(f"Error de formato en línea {i}: Datos inválidos o columnas incompletas.")
    except IOError:
        print("Error: No se pudo leer el archivo de datos.")
        
    return lista_paises

def guardar_en_csv(lista_paises):
    """Guarda la lista actual de países en el archivo CSV."""
    try:
        with open(ARCHIVO_CSV, "w", encoding="utf-8", newline="") as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"] # Identifica los campos donde guardar la información
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            
            escritor.writeheader()
            for pais in lista_paises:
                escritor.writerow({k: pais[k] for k in campos}) # Omite los campos de normalización al guardar en CSV
        print("Cambios guardados con éxito en el archivo CSV.")
    except PermissionError:
        print("Error: El archivo CSV está abierto en otro programa. Ciérrelo e intente de nuevo.")
    except IOError:
        print("Error: Ocurrió un problema al guardar los datos.")

#-------------- FUNCIONES PRINCIPALES --------------#

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

def agregar_pais(lista_paises):
    """Añade un nuevo país a la lista validando que no se repita ni tenga campos vacíos."""
    print("\n--- AGREGAR NUEVO PAÍS ---")
    
    nombre = input("Nombre del país: ").strip()
    if not nombre:
        print("Error: El nombre no puede estar vacío.")
        return

    # Evita duplicados utilizando nombre normalizado
    nombre_norm = normalizar_texto(nombre)
    for p in lista_paises:
        if p["nombre_norm"] == nombre_norm:
            print("Error: El país ya existe.")
            return
            
    try: # Verifica que población y superficie no sean negativas
        poblacion = int(input("Población (entero): "))
        if poblacion < 0:
            print("Error: La población no puede ser negativa.")
            return
            
        superficie = int(input("Superficie en km2 (entero): "))
        if superficie < 0:
            print("Error: La superficie no puede ser negativa.")
            return
    except ValueError:
        print("Error: La población y la superficie deben ser números enteros.")
        return

    continentes_validos_norm = ["asia", "africa", "america", "oceania", "europa"] # Lista de continentes válidos normalizados
    while True: # Bucle que valida el continente ingresado
        continente = input("Continente: ").strip()
        if not continente:
            print("Error: El continente no puede estar vacío.")
            continue
        continente_norm = normalizar_texto(continente)
        if continente_norm in continentes_validos_norm:
            # Guardamos el continente con capitalización correcta (ej. "America")
            continente_guardado = continente.capitalize()
            break
        else:
            print("Error: Continente no válido. Use: Asia, Africa, América, Oceanía, Europa.")
        
    nuevo_pais = {
        "nombre": nombre.title(),  # Guardamos con formato estándar estético
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente_guardado,
        "nombre_norm": nombre_norm,
        "continente_norm": continente_norm
    }
    lista_paises.append(nuevo_pais) # Agrega diccionario al final de la lista
    print(f"País '{nuevo_pais['nombre']}' registrado exitosamente.")

def actualizar_pais(lista_paises):
    """Actualiza la población y superficie de un país existente."""
    print("\n--- ACTUALIZAR DATOS DE PAÍS ---")
    nombre_buscar = input("Ingrese el nombre exacto del país a modificar: ").strip()
    
    if not nombre_buscar:
        print("Error: El nombre no puede estar vacío.")
        return
        
    nombre_buscar_norm = normalizar_texto(nombre_buscar) # Normaliza valor ingresado para buscar

    encontrado = None
    for pais in lista_paises: # Recorre la lista buscando la clave y la guarda si encuentra
        if pais["nombre_norm"] == nombre_buscar_norm:
            encontrado = pais
            break
            
    if encontrado: # Devuelve datos si encontró el país buscado
        print(f"Datos actuales -> Población: {encontrado['poblacion']} | Superficie: {encontrado['superficie']}")
        try: # Pide al usuario nuevos datos
            nueva_pob = int(input("Nueva Población (entero): "))
            nueva_sup = int(input("Nueva Superficie en km2 (entero): "))
            
            if nueva_pob < 0 or nueva_sup < 0: # Verifica que población y superficie ingresadas sean positivas
                print("Error: Los valores no pueden ser negativos.")
                return
            # Actualiza valores en caso de que sean válidos
            encontrado["poblacion"] = nueva_pob
            encontrado["superficie"] = nueva_sup
            print(f"Datos de '{encontrado['nombre']}' actualizados en memoria.")
        except ValueError:
            print("Error: Los ingresos deben ser números enteros.")
    else:
        print("Error: El país especificado no se encuentra registrado.")

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


#----------------- MENÚ PRINCIPAL -----------------#

def ejecutar_menu_tpi():
    """Módulo principal que ejecuta el menú de opciones interactivo."""
    paises_sistema = cargar_desde_csv()
    
    while True:
        print("==================================================")
        print("    TPI PROGRAMACIÓN 1: GESTIÓN DE PAÍSES        ")
        print("==================================================")
        print("1. Mostrar todos los países")
        print("2. Agregar un país")
        print("3. Actualizar población y superficie de un país")
        print("4. Buscar un país por nombre")
        print("5. Filtrar países (Continente / Rangos)")
        print("6. Ordenar países")
        print("7. Mostrar indicadores estadísticos")
        print("8. Guardar cambios y Salir")
        print("==================================================")
        
        opcion = input("Seleccione una opción (1-8): ").strip()
        
        if opcion == "1":
            mostrar_tabla_paises(paises_sistema)
        elif opcion == "2":
            agregar_pais(paises_sistema)
        elif opcion == "3":
            actualizar_pais(paises_sistema)
        elif opcion == "4":
            buscar_pais_nombre(paises_sistema)
        elif opcion == "5":
            filtrar_paises(paises_sistema)
        elif opcion == "6":
            ordenar_paises(paises_sistema)
        elif opcion == "7":
            mostrar_estadisticas(paises_sistema)
        elif opcion == "8":
            guardar_en_csv(paises_sistema)
            print("Finalizando ejecución de la aplicación.")
            break
        else:
            print("Error: Opción inválida. Intente ingresando un número entre 1 y 8.")

if __name__ == "__main__":
    ejecutar_menu_tpi()
