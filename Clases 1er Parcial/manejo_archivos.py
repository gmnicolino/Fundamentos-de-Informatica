#Definir un procedimiento que lea los archivos .txt que estan en la carpeta marzo, y copie la primera linea de cada uno en un archivo dentro de la carpeta resultados (que debe estar dentro de new)

#!/usr/bin/env python3

import os, glob, sys

#movemos a marzo
# extraemos los .txt
# leemos las primeras primeras_lineas
# hacemos carpeta de salida (resultado)
# hacer archivo(salida.txt)
# poner lineas en archivo nuevo

def primeras_lineas(path_a_txt, path_resultado, salida):
    os.chdir(path_a_txt)
    textos = glob.glob("*.txt")          #extraemos todos los archivos con txt
    primer_linea = []
    for txt in textos:
        with open(txt, "r") as texto:
            primer_linea.append (texto.readline())

    os.chdir("../../")      #.. es una carpeta arriba ../.. son dos carpetas, es lo mismo que ../../
    os.mkdir(path_resultado)
    os.chdir(path_resultado)
    with open(salida, "a") as final_txt:
        for linea in primer_linea:
            final_txt.write(linea)

primeras_lineas("datos/marzp", "resultado", "salida.txt")

