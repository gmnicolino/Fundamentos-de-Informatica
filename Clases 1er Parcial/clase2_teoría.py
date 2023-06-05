#Para ejecutar un script tengo que estar en la carpeta donde esta el script
#Para ejecutarlo lo voy a hacer en la terminal de bash (nunca adentro del interprete) 
#Si en la terminal que estoy llamo"python" y me salen >>> (estoy adentro de python) entonces tengo que salir (exit()) y luego poner ./nombre_script.py
#ESO TENGO QUE PONER?

#Comandos útiles: ls, pwd, cd (comandos de la terminal)
#cd --> cambio de directorio
#ls --> lista de archivos de un directorio
#pwd --> path del directorio en el que estoy

#no usar como scripts los nombres de bibliotecas

#atajos útiles:
#ctr + s --> guardar
#ctr + j --> terminal
#ctr + d --> selector múltiple (salimos con ESC)
#ctr + a --> selecciona todo

#¿que es una variable? --> asignarle un espacio en la memoria a un tipo de dato en particular
#¿que es un argumento? --> definido en una función (no existe por fuera). Se guardan de forma momentanea en la memoria. 
#¿que es sript? --> archivo con una extensión (.py)
#¿que es print?
# ¿que es input? -->pasarle a mi script un parametreo extra que me brinda información la terminal 

#bultin --> funciones que vienen con python

#nombre = str(input("escriba un nombre: "))

#os --> me permite dialogar con la terminal, fuera del interprete
#sys --> toma parametros que le pase al script desde la terminal


#os.stat: nos permite obtener estadísticas de un archivo (como por ejemplo su tamaño)
#os.rename: nos permite renombrar archivos
#os.rmdir: nos permite eliminar directorios
#os.path.dirname: nos permite obtener el directorio donde un archivo está contenido
#os.getcwd: nos permite conocer el directorio donde estamos
#os.path.exists: nos permite saber si un archivo existe
#os.path.join: nos permite concatenar rutas (por ejemplo, combinar /una y ruta para obtener /una/ruta)

#!/bin/python3
import os, sys

archivo = sys.argv[1] #declaro una variable que le estoy dando como valor en memoria un argumento. Toma los argumentos que le pasamos al scrypt por consola.
#El corchete es 1, significa que siempre voy a tomar el primero
#Es decir leo solo la primer palabra que escriben en la terminal

def saludador(nombre):
    hola_nombre = "hola" + " " + nombre
    return hola_nombre
print(saludador("julian"))

#otra forma (mejor forma)
def saludador(nombre):
    return "hola" + " " + nombre
print(saludador("julian"))

#este codigo asi no figura bien si queres usar otro nombre
def saludador(nombre):
    return "hola" + " " + nombre
if __name__ == "__main__":
  print(saludador("Ana"))

#MANIPULACIÓN DE ARCHIVOS
#Para trabajar con el archivo ejecutable, voy a usar bibliotectas particulares como os
#Los archivos de lectura, escritura, etc (no ejecutables)
#Python puede leer un texto todo en una linea o linea a linea
#OPEN es la palabra que me permite abrir el archivo pero hay que recordar que siempre hay que cerrarlo
#open(path_al_archivo, modo) 
#- "path_al_archivo" es un objeto de tipo str que indica la ruta en la que se encuentra el archivo. (me dice la ubicacion de mi archivo en la computadora)
#- "modo" es un objeto de tipo str que indica la forma en la que Python accederá al archivo en cuestión. (la forma en la que yo voy a decidir como voy a manipular este archivo)
#modo tambien es un str

#r --> abre un archivo solo para lectura
#r+ --> abre un archivo para lectura y escritura
#a --> Abre un archivo para agregar información. Si el archivo no existe, crea un nuevo archivo para escritura (el mas seguro para escribir)
#w --> Abre un archivo solo para escritura. Sobreescribe el archivo si este ya existe. Si el archivo no existe, crea un nuevo archivo para escritura
#(w sobreescribe un archivo existente)

#Siempre es importante cerrar el archivo, con CLOSE:
#archivo = open(path_al_archivo, modo) 
#archivo.close()

#Una forma para no tener que cerar el archivo
