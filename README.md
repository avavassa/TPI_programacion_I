# TPI Programación I - Sistema de Gestión de Países

## Descripción

Aplicación desarrollada en Python para la gestión de información de países mediante una interfaz de consola interactiva.

El sistema permite almacenar, consultar, modificar y analizar información relacionada con distintos países, incluyendo nombre, población, superficie y continente. Los datos se almacenan en un archivo CSV, permitiendo conservar los cambios realizados entre ejecuciones.

---

## Funcionalidades implementadas

* Visualización de todos los países registrados.
* Alta de nuevos países con validaciones.
* Actualización de población y superficie de países existentes.
* Búsqueda de países por nombre (coincidencia exacta o parcial).
* Filtrado por continente.
* Filtrado por rango de población.
* Filtrado por rango de superficie.
* Ordenamiento por nombre, población o superficie.
* Ordenamiento ascendente y descendente.
* Cálculo de indicadores estadísticos:

  * País con mayor población.
  * País con menor población.
  * Promedio de población.
  * Promedio de superficie.
  * Cantidad de países por continente.
* Persistencia de datos mediante archivo CSV.

---

## Estructura de datos

La información se almacena en una lista de diccionarios.

Ejemplo:

```python
{
    "nombre": "Argentina",
    "poblacion": 45376763,
    "superficie": 2780400,
    "continente": "America"
}
```

Para optimizar búsquedas y comparaciones también se utilizan campos normalizados internos.

---

## Instrucciones de uso

1. Descargar o clonar el repositorio.
2. Ubicarse en la carpeta del proyecto.
3. Ejecutar:

```bash
python3 programa.py
```

4. Utilizar el menú interactivo para acceder a las distintas funcionalidades.

Al finalizar, seleccionar la opción **"Guardar cambios y Salir"** para guardar los datos en el archivo CSV.

---

## Ejemplos de uso

### Mostrar todos los países

```
---------------------------------------------------------------------------
Nombre               | Población       | Superficie (km2) | Continente     
---------------------------------------------------------------------------
Argentina            | 45376763        | 2780400          | America        
Japón                | 125800000       | 377975           | Asia           
Brasil               | 213993437       | 8515767          | America        
Alemania             | 83149300        | 357022           | Europa         
Nauru                | 11947           | 20               | Oceania        
Vanuatu              | 327778          | 12189            | Oceania        
Austrália            | 26713205        | 7741220          | Oceania        
Mongolia             | 3493629         | 1564116          | Asia           
Vietnam              | 101343800       | 331210           | Asia           
China                | 1419321277      | 9598089          | Asia           
Rusia                | 143957079       | 17098242         | Europa         
Zimbabwe             | 15993524        | 390760           | Africa         
Egipto               | 106600000       | 1002450          | Africa         
Canadá               | 41288599        | 9984670          | America        
Bosnia y Herzegovina | 3406568         | 51197            | Europa         
Grecia               | 10372000        | 131957           | Europa         
Cuba                 | 10892659        | 110860           | America        
Nigeria              | 227882845       | 910770           | Africa         
Seychelles           | 99202           | 455              | Africa         
---------------------------------------------------------------------------
```
---

### Buscar país

Entrada:

```text
--- BUSCAR PAÍS ---
Ingrese el nombre (o parte del nombre) a buscar: an
```

Salida:
```
Se encontraron 3 coincidencias:

---------------------------------------------------------------------------
Nombre               | Población       | Superficie (km2) | Continente     
---------------------------------------------------------------------------
Alemania             | 83149300        | 357022           | Europa         
Vanuatu              | 327778          | 12189            | Oceania        
Canadá               | 41288599        | 9984670          | America        
---------------------------------------------------------------------------
```
---

### Estadísticas

Salida:

```text
==================================================
             ESTADÍSTICAS GENERALES               
==================================================
País con MAYOR población: China (1419321277 hab.)
País con MENOR población: Nauru (11947 hab.)
Promedio de población global: 135790716.42 habitantes
Promedio de superficie global: 3208387.84 km2

Cantidad de países por continente:
 -> America: 4
 -> Asia: 4
 -> Europa: 4
 -> Oceania: 3
 -> Africa: 4
==================================================
```

---

## Video demostrativo

Enlace al video:

**[PEGAR AQUÍ EL LINK DEL VIDEO]**

---

## Documentación

Documentación en PDF:

**AGREGAR EL PDF A LA RAÍZ UNA VEZ QUE ESTÉ EL VIDEO**

---

## Integrantes y participación

* Ana Termignoni: persistencia CSV y validaciones, revisión y documentación.
* Georgina Daniela Maldonado: diseño general del sistema, búsquedas, filtros y estadísticas.
