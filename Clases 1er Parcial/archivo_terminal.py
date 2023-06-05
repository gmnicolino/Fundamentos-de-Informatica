#Modificar el script anterior para que pueda incorporar el nombre de los archivos desde la terminal
import os

archivo1 = input("Ingrese el nombre del primer archivo: ")
archivo2 = input("Ingrese el nombre del segundo archivo: ")

if not os.path.exists(archivo1):
    print(f"Error: {archivo1} no existe.")
    exit(1)

if not os.path.exists(archivo2):
    print(f"Error: {archivo2} no existe.")
    exit(1)

temp_filename = "temp.txt"

# Renombrar el primer archivo al nombre temporal
os.rename(archivo1, temp_filename)

# Renombrar el segundo archivo al nombre del primer archivo
os.rename(archivo2, archivo1)

# Renombrar el primer archivo (renombrado temporalmente) al nombre del segundo archivo
os.rename(temp_filename, archivo2)

print(f"{archivo1} y {archivo2} han sido intercambiados.")


