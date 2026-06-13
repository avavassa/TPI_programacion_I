"""
main.py

Punto de entrada principal del programa.
Coordinación del menú interactivo y llamadas a los módulos.
"""

from database import cargar_desde_csv, guardar_en_csv
from operaciones import agregar_pais, actualizar_pais
from reportes import mostrar_tabla_paises, buscar_pais_nombre, filtrar_paises, ordenar_paises, mostrar_estadisticas

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
