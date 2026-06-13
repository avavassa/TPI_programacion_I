"""
Módulo operaciones.py

Contiene las operaciones que modifican los datos de la lista de países:
- agregar_pais(): Añade un nuevo país validando que no exista y que los datos sean correctos.
- actualizar_pais(): Modifica la población y superficie de un país existente.
"""
from utilidades import normalizar_texto

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