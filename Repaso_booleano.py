#BOOLEANO

#Si tengo tiene_hambre, el complemento será not tiene_hambre

#Pedir un número impar utilizando el not
def es_par (numero):
    return numero % 2
def es_impar(numero):
    return not es_par(numero)
print(es_impar(5))

def es_menor_de_edad(edad):
    return edad < 18
def es_mayor_de_edad(edad):
    return not es_menor_de_edad(edad)
print(es_mayor_de_edad(17))

#el correcto sería?
def es_mayor_de_edad(edad):
    return edad >= 18

print(es_mayor_de_edad(17))

#pero en este caso no estoy utilizando es_menor_de_edad

#usando el and
def es_paripatetica(carrera,pais,km):
    return es_paripatetica == ("filosofia","Grecia", 2)
print(es_paripatetica("filosofia", "Grecia", 2))

#ALGO ESTOY HACIENDO MAL PORQUE NO ME DA FALSE CUANDO TENDRIA QUE SER TRUE

#Repasar booklet for

