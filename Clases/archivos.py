import os

archivo1 = "archivo1.txt"
archivo2= "archivo2.txt"

os.rename(archivo1, archivo1 + ".temp")
os.rename(archivo2, archivo1)
os.rename(archivo1 + ".temp", archivo2)

#Otra opcion de la segunda parte:
#os.rename(archivo1,"temporal")
#os.rename(archivo2, archivo1)
#os.rename("temporal", archivo2)

#sacar los archivos y Tarea_correcta.py de la carpeta TAREA para hacer funcionar


#OTRO EJERCICIO 

#¡Desafío final! Creá un script swap.py que tome dos nombres de archivo y renombre al primero con el nombre del segundo, y al segundo lo renombre con el nombre del primero. Ejemplo:

#$ cat hola.txt
#hola
#$ cat chau.txt
#chau
#$ ./swap.py hola.txt chau.txt
#$ cat hola.txt
#chau
#$ cat chau.txt
#hola

import sys
import os

if len(sys.argv) != 3:
    print("Usage: python swap.py <mi_nombre.txt> <nuevo_archivo1.txt>")
    sys.exit(1)

mi_nombre.txt = sys.argv[1]
file2 = sys.argv[2]

if not os.path.exists(mi_nombre.txt):
    print(f"Error: {mi_nombre.txt} does not exist.")
    sys.exit(1)

if not os.path.exists(nuevo_archivo1.txt):
    print(f"Error: {nuevo_archivo1.txt} does not exist.")
    sys.exit(1)

temp = mi_nombre.txt + '.temp'

# Renombrar file1 a temp
os.rename(mi_nombre.txt, temp)

# Renombrar file2 a file1
os.rename(nuevo_archivo1.txt, mi_nombre.txt)

# Renombrar temp a file2
os.rename(temp, nuevo_archivo1.txt)

print(f"{mi_nombre.txt} y {nuevo_archivo1.txt} han sido intercambiados.")