"""
Módulo database.py

Gestiona la persistencia de datos en archivo CSV.
Funciones:
- verificar_e_inicializar_csv(): Crea el archivo si no existe.
- cargar_desde_csv(): Lee el CSV y devuelve lista de países.
- guardar_en_csv(): Guarda los cambios en el archivo.
"""

import os # Módulo nativo para manejo de archivos y rutas
import csv  # Módulo nativo para una lectura y escritura robusta
from utilidades import normalizar_texto   # importa desde utilidades la función de normalización

ARCHIVO_CSV = "paises.csv"

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