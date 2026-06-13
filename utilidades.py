"""
Módulo utilidades.py

Contiene funciones auxiliares reutilizables en todo el programa:
- normalizar_texto(): Elimina acentos y convierte a minúsculas para búsquedas.
"""

import unicodedata # Módulo nativo para normalización de nombres de países y continentes

def normalizar_texto(texto):
    """Convierte a minúsculas y elimina acentos."""
    if not texto:
        return ""
    # Descomponer caracteres acentuados en base + diacrítico
    texto = unicodedata.normalize('NFD', texto)
    # Filtrar solo caracteres no diacríticos (letras, números, espacios)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
    return texto.lower()