#Booleano --> True or False

#Para averiguar la longitud de textos utilizo len ==
a = len("arbol") == len("microondas")
print(a)

def es_mas_largo_que(un_string, otro_string):
  return len(un_string) > len(otro_string)

print(es_mas_largo_que("Misiones", "Córdoba"))

#Pregunta
def es_pregunta(oracion):
  return str.startswith(oracion, "¿") and str.endswith(oracion, "?")
print(es_pregunta("¿Qué hora es?"))

#Siempre que me pida definir una función hay que usar def en la primera línea + nombre de la función + (parametro1, parametro2) + : 
#En la segunda línea empezamos con return + lo que queremos que devuelva nuestra función

#Suma de longitudes
def suma_longitudes(un_string, otro_string):
  return len(un_string) + len(otro_string)
print(suma_longitudes("arbol", "juegos"))

#Mitad
def mitad(un_numero):
    return un_numero / 2
print(mitad(8))

#Definí la función es_hora_de_la_verdad, que tome una hora y nos diga si son las 12 
def es_hora_de_la_verdad(hora):
    return hora == 12
print(es_hora_de_la_verdad(11))

#Definir el doble de un número
def doble(numero):
  return 2 * numero
print(doble(5))

#Definir el triple de un número
def triple(numero):
  return 3 * numero
print(triple(5))

#Definir el siguiente de un número
def siguiente(numero):
  return numero + 1
print(siguiente(4))

#Definir el anterior de un número
def anterior(numero):
  return numero - 1
print(anterior(4))

#Definir el siguiente del doble de un número
def siguiente_del_doble(numero):
  return siguiente(doble(numero))
print(siguiente_del_doble(4))

#Definir el anterior del triple de un número
def anterior_del_triple(numero):
  return anterior(triple(numero))
print(anterior_del_triple(4))

#True si le gusta leer mas que 20 o False si menos
def le_gusta_leer(cantidad_de_libros):
  return cantidad_de_libros > 20
print(le_gusta_leer(8))

#Definir si tres numeros cumplen lo dicho luego de return
def esta_entre(numero1,numero2,numero3):
    return numero3 > numero1 > numero2
print(esta_entre(10,1,10))

#Definir tres números y diga si el primero es menor al segundo o mayor al tercero
def esta_fuera_de_rango(numero1,numero2,numero3):
    return numero3 < numero1 or numero1 < numero2
print(esta_fuera_de_rango(17,1,10))

def es_biblioteca(lugar):
 return "biblioteca" in "lugar"
print(es_biblioteca("Argentina"))

#Definir longitud de un nombre completo
def longitud_nombre_completo(nombre, apellido):
    nombre_completo = nombre + apellido
    return len(nombre_completo)
print(longitud_nombre_completo("Cosme","Fulanito"))   #VER ARCHIVO QUE DA SIEMPRE UN NUMERO MAS

#str.upper que convierte en mayúsculas un string.
#DEFINIR LA FUNCION GRITAR
def gritar(palabra):
    return palabra
print(gritar("MANUEL"))
#"¡" y "!" (al igual que los espacios y otros signos de puntuación) son strings y que los strings se pueden concatenar usando el operador +.

#Corroborar si el dia de la semana usado es igual al Sábado
def es_fin_de_semana(día_de_la_semana):
    return día_de_la_semana == "Sábado"
print(es_fin_de_semana("Jueves"))


#Corroborar si los dias de la semana usados son alguno igual al Sábado
def es_fin_de_semana(día_de_la_semana):
    return día_de_la_semana == "Sábado"
print(es_fin_de_semana("Jueves") or es_fin_de_semana("Sábado"))

#Otra forma
def es_fin_de_semana(dia): 
    return str.lower(dia) == "sábado" or str.lower(dia) == "domingo"
print(es_fin_de_semana("Lunes"))

#el str.lower me sirve para que el dia lo tome como minúscula



def cadena_num_letras(cadena):
    letras_validas = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789" #incluye el espacioo
    
    for caracter in cadena:
        if caracter not in letras_validas:
            return False
        else:
          return True

print(cadena_num_letras("&&&&"))
