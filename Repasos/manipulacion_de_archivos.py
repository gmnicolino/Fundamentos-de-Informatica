"""Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo.
Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en cuestión con 
respecto a la cantidad total de palabras. (escribi porcentaje en frecuencia)
"""

# Counter: es una subclase de diccionario que se utiliza para realizar conteos sobre listas, palabras #
"""Contar la frecuencia de elementos en una lista, crear histogramas y analizar datos de texto"""
# Collections: Biblioteca

from collections import Counter

def frecuencia_p(archivo):
    # Abrir archivo de entrada
    with open(archivo, 'r') as archivo:
        # Leer el contenido del archivo y dividir en palabras
        contenido = archivo.read()
        palabras = contenido.split()

        # Contar la frecuencia de cada palabra
        frecuencias = Counter(palabras)

        # Calcular la frecuencia de cada palabra como porcentaje
        # por cada palabra y frecuencia en la lista de "frecuencias" donde items() = palabras
        for palabra, frecuencia in frecuencias.items():
            total_palabras = len(palabras)
            frecuencias_porcentaje = {palabra: (frecuencia / total_palabras) * 100} # me muestra: {"Hola": porcentaje que representa}
            print(frecuencias_porcentaje)

print(frecuencia_p("arch3.txt"))

#la suma de los porcentajes son el 100%