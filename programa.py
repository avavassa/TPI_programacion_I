import os

ARCHIVO_CSV = "paises.csv"

def verificar_e_inicializar_csv():
    if not os.path.exists(ARCHIVO_CSV):
        with open(ARCHIVO_CSV, "w", encoding="utf-8") as archivo:
            archivo.write("nombre,poblacion,superficie,continente\n")
            archivo.write("Argentina,45376763,2780400,América\n")
            archivo.write("Japón,125800000,377975,Asia\n")
            archivo.write("Brasil,213993437,8515767,América\n")
            archivo.write("Alemania,83149300,357022,Europa\n")

def cargar_desde_csv():
    lista_paises = []
    verificar_e_inicializar_csv()
    
    try:
        with open(ARCHIVO_CSV, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            if len(lineas) <= 1:
                return lista_paises
                
            for i in range(1, len(lineas)):
                linea = lineas[i].strip()
                if not linea:
                    continue
                    
                datos = linea.split(",")
                if len(datos) == 4:
                    try:
                        pais = {
                            "nombre": datos[0].strip(),
                            "poblacion": int(datos[1].strip()),
                            "superficie": int(datos[2].strip()),
                            "continente": datos[3].strip()
                        }
                        lista_paises.append(pais)
                    except ValueError:
                        print(f"Error de formato en linea {i+1}: Datos numericos invalidos.")
                else:
                    print(f"Error de formato en linea {i+1}: Cantidad de columnas incorrecta.")
    except IOError:
        print("Error: No se pudo leer el archivo de datos.")
        
    return lista_paises

def guardar_en_csv(lista_paises):
    try:
        with open(ARCHIVO_CSV, "w", encoding="utf-8") as archivo:
            archivo.write("nombre,poblacion,superficie,continente\n")
            for pais in lista_paises:
                linea = f"{pais['nombre']},{pais['poblacion']},{pais['superficie']},{pais['continente']}\n"
                archivo.write(linea)
        print("Cambios guardados con exito en el archivo CSV.")
    except PermissionError:
        print("Error: El archivo CSV esta abierto en otro programa. Cierrelo e intente de nuevo.")
    except IOError:
        print("Error: Ocurrio un problema al guardar los datos.")

def mostrar_tabla_paises(lista_paises):
    if not lista_paises:
        print("No hay registros para mostrar.")
        return
        
    print("\n" + "-" * 75)
    print(f"{'Nombre':<20} | {'Poblacion':<15} | {'Superficie (km2)':<16} | {'Continente':<15}")
    print("-" * 75)
    for pais in lista_paises:
        print(f"{pais['nombre']:<20} | {pais['poblacion']:<15} | {pais['superficie']:<16} | {pais['continente']:<15}")
    print("-" * 75 + "\n")

def agregar_pais(lista_paises):
    print("\n--- AGREGAR NUEVO PAÍS ---")
    
    nombre = input("Nombre del pais: ").strip()
    if not nombre:
        print("Error: El nombre no puede estar vacio.")
        return

    for p in lista_paises:
        if p["nombre"].lower() == nombre.lower():
            print("Error: El pais ya existe.")
            return
            
    try:
        poblacion = int(input("Poblacion (entero): "))
        if poblacion < 0:
            print("Error: La poblacion no puede ser negativa.")
            return
            
        superficie = int(input("Superficie en km2 (entero): "))
        if superficie < 0:
            print("Error: La superficie no puede ser negativa.")
            return
    except ValueError:
        print("Error: La poblacion y la superficie deben ser numeros enteros.")
        return
        
    continente = input("Continente: ").strip()
    if not continente:
        print("Error: El continente no puede estar vacio.")
        return
        
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente.capitalize()
    }
    lista_paises.append(nuevo_pais)
    print(f"Pais '{nombre}' registrado exitosamente en memoria.")

def actualizar_pais(lista_paises):
    print("\n--- ACTUALIZAR DATOS DE PAÍS ---")
    nombre_buscar = input("Ingrese el nombre exacto del pais a modificar: ").strip().lower()
    
    encontrado = None
    for pais in lista_paises:
        if pais["nombre"].lower() == nombre_buscar:
            encontrado = pais
            break
            
    if encontrado:
        print(f"Datos actuales -> Poblacion: {encontrado['poblacion']} | Superficie: {encontrado['superficie']}")
        try:
            nueva_pob = int(input("Nueva Poblacion (entero): "))
            nueva_sup = int(input("Nueva Superficie en km2 (entero): "))
            
            if nueva_pob < 0 or nueva_sup < 0:
                print("Error: Los valores no pueden ser negativos.")
                return
                
            encontrado["poblacion"] = nueva_pob
            encontrado["superficie"] = nueva_sup
            print(f"Datos de '{encontrado['nombre']}' actualizados en memoria.")
        except ValueError:
            print("Error: Los ingresos deben ser numeros enteros.")
    else:
        print("Error: El pais especificado no se encuentra registrado.")

def buscar_pais_nombre(lista_paises):
    print("\n--- BUSCAR PAÍS ---")
    criterio = input("Ingrese el nombre (o parte del nombre) a buscar: ").strip().lower()
    
    if not criterio:
        print("Error: El criterio de busqueda no puede estar vacio.")
        return
        
    coincidencias = []
    for pais in lista_paises:
        if criterio in pais["nombre"].lower():
            coincidencias.append(pais)
            
    if coincidencias:
        print(f"\nSe encontraron {len(coincidencias)} coincidencias:")
        mostrar_tabla_paises(coincidencias)
    else:
        print("No se encontraron paises con ese criterio de busqueda.")

def filtrar_paises(lista_paises):
    print("\n=== OPCIONES DE FILTRADO ===")
    print("1. Filtrar por Continente")
    print("2. Filtrar por Rango de Poblacion")
    print("3. Filtrar por Rango de Superficie")
    opcion = input("Seleccione tipo de filtro (1-3): ").strip()
    
    resultados = []
    
    if opcion == "1":
        continente = input("Ingrese el continente a filtrar: ").strip().lower()
        for p in lista_paises:
            if p["continente"].lower() == continente:
                resultados.append(p)
                
    elif opcion == "2":
        try:
            min_pob = int(input("Poblacion minima: "))
            max_pob = int(input("Poblacion maxima: "))
            for p in lista_paises:
                if min_pob <= p["poblacion"] <= max_pob:
                    resultados.append(p)
        except ValueError:
            print("Error: Los rangos deben ser numeros enteros.")
            return
            
    elif opcion == "3":
        try:
            min_sup = int(input("Superficie minima (km2): "))
            max_sup = int(input("Superficie maxima (km2): "))
            for p in lista_paises:
                if min_sup <= p["superficie"] <= max_sup:
                    resultados.append(p)
        except ValueError:
            print("Error: Los rangos deben ser numeros enteros.")
            return
    else:
        print("Opcion de filtrado no valida.")
        return
        
    if resultados:
        mostrar_tabla_paises(resultados)
    else:
        print("Ningun pais cumple con los criterios del filtro aplicado.")

def ordenar_paises(lista_paises):
    if not lista_paises:
        print("No hay datos para ordenar.")
        return

    print("\n=== OPCIONES DE ORDENAMIENTO ===")
    print("1. Ordenar por Nombre")
    print("2. Ordenar por Poblacion")
    print("3. Ordenar por Superficie")
    criterio = input("Seleccione criterio (1-3): ").strip()
    
    if criterio not in ["1", "2", "3"]:
        print("Criterio invalido.")
        return
        
    print("1. Ascendente")
    print("2. Descendente")
    sentido = input("Seleccione sentido (1-2): ").strip()
    
    if sentido not in ["1", "2"]:
        print("Sentido invalido.")
        return

    clave = "nombre" if criterio == "1" else ("poblacion" if criterio == "2" else "superficie")
    
    lista_ordenada = list(lista_paises)
    n = len(lista_ordenada)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            valor_actual = lista_ordenada[j][clave]
            valor_siguiente = lista_ordenada[j+1][clave]
            
            if clave == "nombre":
                valor_actual = valor_actual.lower()
                valor_siguiente = valor_siguiente.lower()
                
            intercambiar = False
            if sentido == "1" and valor_actual > valor_siguiente:
                intercambiar = True
            elif sentido == "2" and valor_actual < valor_siguiente:
                intercambiar = True
                
            if intercambiar:
                lista_ordenada[j], lista_ordenada[j+1] = lista_ordenada[j+1], lista_ordenada[j]
                
    mostrar_tabla_paises(lista_ordenada)

def mostrar_estadisticas(lista_paises):
    if not lista_paises:
        print("No hay datos suficientes para calcular estadisticas.")
        return
        
    print("\n==================================================")
    print("             ESTADÍSTICAS GENERALES               ")
    print("==================================================")
    
    pais_max_pob = lista_paises[0]
    pais_min_pob = lista_paises[0]
    
    suma_poblacion = 0
    suma_superficie = 0
    conteos_continente = {}
    
    for pais in lista_paises:
        suma_poblacion += pais["poblacion"]
        suma_superficie += pais["superficie"]
        
        if pais["poblacion"] > pais_max_pob["poblacion"]:
            pais_max_pob = pais
        if pais["poblacion"] < pais_min_pob["poblacion"]:
            pais_min_pob = pais
            
        cont = pais["continente"]
        if cont in conteos_continente:
            conteos_continente[cont] += 1
        else:
            conteos_continente[cont] = 1
            
    total_paises = len(lista_paises)
    promedio_pob = suma_poblacion / total_paises
    promedio_sup = suma_superficie / total_paises
    
    print(f"Pais con MAYOR poblacion: {pais_max_pob['nombre']} ({pais_max_pob['poblacion']} hab.)")
    print(f"Pais con MENOR poblacion: {pais_min_pob['nombre']} ({pais_min_pob['poblacion']} hab.)")
    print(f"Promedio de poblacion global: {promedio_pob:.2f} habitantes")
    print(f"Promedio de superficie global: {promedio_sup:.2f} km2")
    
    print("\nCantidad de paises por continente:")
    for continente, cantidad in conteos_continente.items():
        print(f" -> {continente}: {cantidad}")
    print("==================================================\n")

def ejecutar_menu_tpi():
    paises_sistema = cargar_desde_csv()
    
    while True:
        print("==================================================")
        print("    TPI PROGRAMACIÓN 1: GESTIÓN DE PAÍSES        ")
        print("==================================================")
        print("1. Mostrar todos los paises")
        print("2. Agregar un pais")
        print("3. Actualizar poblacion y superficie de un pais")
        print("4. Buscar un pais por nombre")
        print("5. Filtrar paises (Continente / Rangos)")
        print("6. Ordenar paises")
        print("7. Mostrar indicadores estadisticos")
        print("8. Guardar cambios y Salir")
        print("==================================================")
        
        opcion = input("Seleccione una opcion (1-8): ").strip()
        
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
            print("Finalizando ejecucion de la aplicacion.")
            break
        else:
            print("Error: Opcion invalida. Intente ingresando un numero entre 1 y 8.")

if __name__ == "__main__":
    ejecutar_menu_tpi()