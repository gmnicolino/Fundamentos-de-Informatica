#gitignore --> sirve para que cuando se suben archivos de visual a git, se ignore el archivo escrito en la carpeta de gitignore

#Expresiones regulares: patrones de texto escritos con un código particular.
    #Para validación de cosas 
    #Busqueda de textos sobre una fuente que no conozco

#Los caracteres especiales (de escape) los tenemos que incorporar para las búsquedas de strings

#"^palabra" 
#"/Apalabra" --> probablemente no la encontraremos

#readlines --> read + split (" /n")

#caracteres de cuantificación: 
    # * (git add *) --> todo 
    # + --> una o mas ocurrencias del patrón
    # ? --> cero o una
    # {n} --> exactamente n veces
    # {n,m} --> por lo menos n pero no mas de m veces


#Desafío I: ¿Construí la expresión regular que obtenga al menos 4 dígitos?
"\d{4,}"

#Desafío II: ¿Construí la expresión regular que obtenga al entre 3 y 6 letras minúsculas?
"[a-z]{3,6}"
#Que tenga una longitud entre 3 y 6

#Desafío III: ¿Construí la expresión regular que obtenga todas las apariciones del patrón ab en un string?
"ab*"

#Rangos --> [a-z]
    #Se escriben entre corchetes y se pone dentro el rango que quiere buscar
    #Si quiero que sean mayusculas u minusculas [aA, -zZ]

#import re
    #ayuda a buscar patrones especificos en un texto dado

#import re
#(r"   ", texto)

#METODO: porque es re.search(parametro1, parametro2)

import re
texto = "Estoy en la clase de Informática y luego tengo clase de Microeconomia"
patron = "clase"
print(re.search(patron, texto))

#si en la terminal luego de correr el codigo dice match = "clase" (en este caso) significa que lo encontro
#para corroborarlo hago lo siguiente:
print(texto[12:17])

#aca nos esta dando el primero
print(re.match(patron,texto))

#match busca en la primera palabra del texto
#search busca en todo el texto y te da la primera vez que aparece el patron

#split me permite separar los strings en base a un caracter en particular

#Findall
print(re.findall(patron, texto))

#Tupla es un tipo de dato que es entre parentesis, no es mutable. Se usan en general para decir este valor siempre está asociado para este valor
#Se usa para almacenar datos que se que no van a cambiar

#Listas son mutables (pueden cambiar)

#si quiero decir que tambien empieza con a en patron = "^a[a,z]"

#tanto search como match nos daban los objetitos
#para traer el resultado de los objetitos, usamos group() 
#Group() me agrupa el string --> me permite obtener el string de la busqueda que hice

print(re.search(patron, texto).group())
