#el punto, ., que indica la carpeta en la que estamos parados;
#y los dos puntos, .., que indica la carpeta superior.

#os.mkdir(ruta), el cual sirve para crear una carpeta en la ruta indicada (si queremos crearla en la carpeta donde estamos parados solo tenemos que poner el nombre de la carpeta).
#os.chdir(ruta), el cual nos permite movernos de carpeta hasta la ruta indicada.

#os.mkdir("../Escritorio/carpeta")

# crear la carpeta Prácticas en el directorio actual:
#os.mkdir("Prácticas")

# crear la carpeta Teorías en el directorio superior:
#os.mkdir("../Teorías")

# movernos a la carpeta Prácticas:
#os.chdir("Prácticas")

# movernos desde Prácticas a Teorías
#os.chdir("../../Teorías")


#import os
#import glob

#os.listdir()
#['Ej1.py', 'Ej3.py', 'archivo2.txt', 'Ej2.py', 'Ej4.py', 'documento.txt', 'Ej5.py'...]
#glob.glob("*")
#['Ej1.py', 'Ej3.py', 'archivo2.txt', 'Ej2.py', 'Ej4.py', 'documento.txt', 'Ej5.py'...]
#glob.glob("*.py")
#['Ej1.py', 'Ej3.py', 'Ej2.py', 'Ej4.py', 'Ej5.py'...]

#el método listdir de la biblioteca os y el método glob de la biblioteca glob. 
#Con el primero obtenemos una lista de todos los archivos que se encuentran en una carpeta, mientras que con el segundo, además de esto, tenemos la posibilidad de listar archivos específicos.
#glob me ayuda para hacerme una lista de todos los archivos ej:txt que tengo, y con un for recorrer uno atras de otro

#Escribir un script en el cual debemos movernos a la carpeta Informes y obtener los archivos *.txt que hayan allí. 
# Por cada archivo hay que obtener, por un lado, cuántas veces aparece la palabra "estado" y por otro lado la cantidad de líneas. 
# Por último, hay que crear una carpeta que se llame Apellidos, donde hay que crear un archivo llamado Lista.txt que contenga en cada línea la primer línea de cada archivo .txt obtenidos anteriormente.

#!/usr/bin/env python3

import os, glob, sys

def ejercicio_rutas():
    os.chdir("Informes")
    txt = glob.glob("*.txt")
    cantidad_estado = []
    cantidad_lineas = []
    for archivo in txt:
        with open(archivo, "r") as file:
            file_completa = file.read()
            cantidad_estado.append(file_completa.count("estado"))
            cantidad_lineas.append(file_completa.count("\n"))

    os.mkdir("Apellido")
    with open("Apellido/Lista.txt", "w") as salida:
        for archivo in txt:
            with open(archivo, "r") as file:
                #primer_linea = file.readline()
                #salida.write(primer_linea)
                salida.write(file.readline())
if __name__ == "__main__":
    print(ejercicio_rutas())




