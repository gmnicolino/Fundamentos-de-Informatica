#!/usr/bin/env python3
#directamente sabe que lo voy a ejecutar con python
import os, glob, sys
#importo bibliotecas

def ejercicio_rutas():
    os.chdir("../Informes")
txt = glob.glob("*.txt")
#creamos la variable txt para que funcione en otras funciones la funcion glob.glob(crea lista de nombres de archivos en la carpeta que selecionamos antes)

cantidad_estado = []
cantidad_lineas = []    #variable en forma de lista para ver cuantas veces aparece estado en cada archivo y la cantidad de lineas de cada uno

for archivo in txt:      #archivo es una varaiable tal como txt
        with open(archivo, 'r') as file:
            lineas = file.read()
            cantidad_estado.append(lineas.count("estado"))  #a la lista de cantidad de estado le agrego la funcion que cuenta la cantidad de veces que aparece estado asi ya se agrega automaticamente
            cantidad_lineas.append(file.count("\n")) #cueentala cantidad de saltos en el file

os.mkdir("Apellido")
with open('Apellidos/Lista.txt', 'w') as salida:     #creamos una lista llamada lista.txt y le marcamos que la haga dentro de Apellidos y la nombramos salida para las funciones
    for archivo in txt:
        with open (archivo, 'r') as f:
            salida.write(f.readline()) #guardo la funcion de leer cada linea y combertirla en lista (readline)  dentro de la lista lista.txt llamada salida