# PRACTICA EXPRESIONES REGULARES

#Ejercicio 1
import re

def caracteres_permitidos(string):
    return bool(re.search("[a-zA-Z0-9]", string))

print("El string ....")

#Ejercicio 2
import re

def caracteres_permitidos(string):
    return not bool(re.search("[^a-zA-Z0-9]", string))

print("El string", "ABCDEFabcdef123450", "tiene todos los caracteres permitidos?")
print(caracteres_permitidos("ABCDEFabcdef123450"))
print(("El string", "ABCDEFabcdef123450!", "tiene todos los caracteres permitidos?"))
print(caracteres_permitidos("ABCDEFabcdef123450!"))

# Ejercicio 3, parte 1
import re

def encontrar_patron(string):
    patron = "he*"
    if re.search(patron, string) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"

print(encontrar_patron("a"))
print(encontrar_patron("h"))
print(encontrar_patron("he"))
print(encontrar_patron("heeeeeee"))

# Ejercicio 3, parte 2

import re

def encontrar_patron(string):
    patron = "he+"
    if re.search(patron, string) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"

print(encontrar_patron("a"))
print(encontrar_patron("h"))
print(encontrar_patron("he"))
print(encontrar_patron("heeeeeee"))

# Ejercicio 3, parte 3

import re

def encontrar_patron(string):
    patron = "he?"
    if re.search(patron, string) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"

print(encontrar_patron("a"))
print(encontrar_patron("h"))
print(encontrar_patron("he"))
print(encontrar_patron("heeeeeee"))

# Ejercicio 3, parte 4

import re

def encontrar_patron(string):
    patron = "he{2,3}"
    if re.search(patron, string) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"

print(encontrar_patron("hheeeeeey"))
print(encontrar_patron("he"))
print(encontrar_patron("hhhe"))
print(encontrar_patron("heeeeeee"))

#los patrones en expresiones regulares son string
#todo en expresines regulares en string

#Ejercicio 4
import re

def palabras_unidas(string):
    patron = "^[a-z]+_[a-z]+$"
    if re.search(patron, string) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"

string = input("ingrese una palabra: ")
print(palabras_unidas(string))

#^ --> ingreso de linea
#$ --> fin de linea

#Ejercicio 8
import re

def extraer_numeros(string):
    resultado = re.split("\D+", string)
    for elemento in resultado:
        print(elemento)

string = "Hoy curse 2 materias, 1 Probabilidad y 2 Informatica"
print(extraer_numeros(string))

#Ejercicio 9
import re

def entre_guiones(string):
    return re.findall(r"-(.*?)-" , string)

string = "Hoy curse dos materias -Probabilidad y Informatica- en ese mismo orden -primero Probabilidad y segundo Informatica-"
print(entre_guiones(string))

#para que vea los guiones en el medio tengo que agregarle el signo de pregunta
#el punto significa cualquier caracter

# Ejercicio 10
import re

def get_substr(string):
    return re.findall("[@|&](.*?)[@|&]", string)

string = "sdaf@dsfa&fasdf& sdf @   dsf  dfds@sdaf@sdfasd  ewr"

lista_subtr = get_substr ("sdaf@dsfa&fasdf& sdf @   dsf  dfds@sdaf@sdfasd  ewr")

resultado = {}
print(get_substr(string))

#Ejercicio 11
import re 

def dos_P(lista):
    for elemento in lista:
        resultado = re.match("(P\w*)\W(P\w*)", elemento)
        if resultado is not None:
            print(resultado.group())

lista = ["Practica Python", "Practica C++", "Practica Expresiones", "Practica POO"]
print(dos_P(lista))