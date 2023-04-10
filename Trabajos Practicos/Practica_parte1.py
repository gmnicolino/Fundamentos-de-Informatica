# PRÁCTICA DE INTRODUCCIÓN A PYTHON

# #Ejercicio 1
def siguiente(numeros):
    return numeros + 1
print("Ejercicio 1")
print(siguiente(5))

def anterior(numeros):
    return numeros - 1
print("Ejercicio 1")
print(anterior(3))

# #Ejercicio 2
def doble(numeros):
    return 2 * numeros
print("Ejercicio 2")
print(doble(4))

# #otra forma de realizar el 2
def doble(num):
    return num*2

# #Ejercicio 3
def doble_del_anterior(numeros):
    return 2 * (numeros - 1)
print("Ejercicio 3")
print(doble_del_anterior(3))

def doble_del_siguiente(numeros):
    return 2 * (numeros + 1)
print("Ejercicio 3")
print(doble_del_siguiente(5))

# #una mejor forma de realizar el 3
def doble2(n):
    return str(doble(anterior(n))) + " " + str(doble(siguiente(n)))
print("Ejercicio 3")
print(doble2(2))

# #Ejercicio 4
def retirar_dinero(saldo,monto_a_retirar):
   return saldo - monto_a_retirar
print("Ejercicio 4")
print(retirar_dinero(150000,45000))

def retirar_dinero(saldo,monto_a_retirar):
   return max(saldo - monto_a_retirar, 0)
print("Ejercicio 4")
print(retirar_dinero(150000,45000))

# #Ejercicio 5 para comparar cosas pongo ==
def dia_de_la_semana_favorito(dia):
    return dia == "Sábado"

print("Ejercicio 5")
print(dia_de_la_semana_favorito("Lunes"))
print(dia_de_la_semana_favorito("Sábado"))

# #Ejercicio 6
def dentro_del_rango_de_longitud_de_onda(longitud):
    return ((223.0 < longitud) and (longitud < 586.8)) 
print("Ejercicio 6")
print(dentro_del_rango_de_longitud_de_onda(777.0))
print(dentro_del_rango_de_longitud_de_onda(123.0))
print(dentro_del_rango_de_longitud_de_onda(366.0))


#Ejercicio 7
def dentro_del_rango_de_longitud_de_onda_y_distinto_de_numero(longitud):
    return ((223.0 < longitud) and (longitud < 586.8) and (longitud != 314.5))

print("Ejercicio 7")
print(dentro_del_rango_de_longitud_de_onda_y_distinto_de_numero(777.0))
print(dentro_del_rango_de_longitud_de_onda_y_distinto_de_numero(123.0))
print(dentro_del_rango_de_longitud_de_onda_y_distinto_de_numero(314.5))
print(dentro_del_rango_de_longitud_de_onda_y_distinto_de_numero(340.5))


# #Ejercicio 8
def tiene_descuento(edad):
    return (12 >= edad) or (edad >= 60)

print("Ejercicio 8")

print(tiene_descuento(8))
print(tiene_descuento(12))
print(tiene_descuento(14))
print(tiene_descuento(60))
print(tiene_descuento(65))

#Ejercicio 9 
def funcion_xor(bool1, bool2):
    if (bool1 == True and bool2 == False) or (bool1 == False and bool2 == True):
        return True
    else:
        return False
print("Ejercicio 9")
print(funcion_xor(True, False))

#otra forma
def funcion_xor(bool1, bool2):
    return(bool1 == True and bool2 == False) or (bool1 == False and bool2 == True)

print("Ejercicio 9")
print(funcion_xor(True, False))
print(funcion_xor(False, True))
print(funcion_xor(True, True))
print(funcion_xor(False, False))

#Ejercicio 10
def hola_usuario(nombre, apellido):
    return "hola " + nombre + " " + apellido
# print("Ejercicio 10")

print(hola_usuario("giovanna", "nicolino"))




#datos que se pueden usar distintos
#palabra ="hola"
#palabra.strartswith("H")
#str.startswith(palabra,"H")

# #Ejercicio 11
def empieza_con_H(palabra):
    if palabra[0] == "H":
        return len(palabra)
    else:
        return "la palabra no empieza por H"

print("Ejercicio 11")
print(empieza_con_H("Horoscopo"))
print(empieza_con_H("Celular"))

# #Ejercicio 12
def empieza_con_buenos(palabra):
    return palabra.startswith("Buenos") or palabra.startswith("Buenas")
print("Ejercicio 12")
print(empieza_con_buenos("Buenos dias"))
print(empieza_con_buenos("dias"))


#nunca poner un return y un booleano

#Ejercicio 13

def es_multiplo(numero1, numero2):
    return numero2 % numero1 == 0
#print("Ejercicio 13")
print(es_multiplo(4,2))
print(es_multiplo(3,9))

#otra forma de hacer el ejercicio 13
numero1 = int(input("introduzca un numero1: "))
numero2 = int(input("introduzca un numero2: "))
def es_multiplo(numero1, numero2):
    return numero2 % numero1 == 0
print(es_multiplo(numero1, numero2))


# Ejercicio 14
numero = int(input("ingrese un numero"))
print("Ejercicio 14")

if numero %2 == 0:
         print("es numero par")
elif numero == 0:
     print("es igual a cero")
else:
     print("es impar")


# Ejercicio 15
def contar_a(frase):
  contador = 0
  for i in range(0,len(frase)):
    if frase[i]=='a' or frase[i]=='A':
      contador +=1
  return contador

print("Ejercicio 15")

print(contar_a('Hola como Andas?'))
# print('Hola como Andas?'.count('a'))


# Ejercicio 16
def contar_meses(cantidad_dinero):
  contador_meses=0
  while cantidad_dinero >= 60000:
    cantidad_dinero = cantidad_dinero -60000 
    #cantidad_dinero -= 60000
    contador_meses += 1
  return contador_meses

print("Ejercicio 16")

print(contar_meses(55000))
print(contar_meses(60000))
print(contar_meses(65000))
print(contar_meses(119000))
print(contar_meses(120000))
print(contar_meses(125000))
