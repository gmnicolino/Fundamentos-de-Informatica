from aves import pepita

#pepita sabe volar porque lo hace sin quejarse
print(pepita.volar_en_circulos())

#pepita no sabe hablar porque nos dimos cuenta que nos tira un error, porque nos dice que no es un atributo de pepita poder hablar.
print(pepita.hablar())

#a pepita le gusta comer alpiste, debemos ponerle la cantidad de gramos 
print(pepita.comer_alpiste(200))


#Sabemos que pepita es un objeto individual/unico, en particular un objeto de la clase GOlondrinas
#Entiende mensajes que las golondrinas entienden
#Tiene las caracteristicas de una golondrina (atributos)


# CLASE: agrupo objetos por caracteristicas similares
# Instancias de una clase: ser individual/unico

print("al comienzo: ", pepita.energia)

#En este print entiende el mensaje y nos responde 

pepita.volar_en_circulos
print("despues de volar: ", pepita.energia)
pepita.comer_alpiste
print("despues de comer: ", pepita.energia)

#Pepita tiene una energia basal
#Ahora sabemos que pepita cuando le damos ordenes, está haciendo algo y sabemos que eso que la caracteriza es la energia

# ESTADO: esta dado por el conjunto de sus atributos (sabe volar, comer alpiste, tiene una energia particular)
# El estado puede cambiar con el tiempo
# Ahora sabemos que el estado de pepita está dado por su energia y que pepita tiene como atributos/caracteristicas saber volar y comer alpiste
# Se puede tener mas de un estado
# El estado de los objetos de alguna forma puede cambiar o modificarse, esto lo vimos cuando le di una orden (volar/comer) y ahi el estado se modifico
# Los objetos tienen ciertos comportamientos
# El comportamiento de algun modo puede modificar su estado

print("hasta aca pepita")

from aves import anastasia

print("En el caso de anastasia, tiene una energia de: ", anastasia.energia)
print(anastasia.volar_en_circulos())
print(anastasia.energia)
print(anastasia.comer_alpiste(200))
print(anastasia.energia)

#Anastasia y Pepita no tienen el mismo estado (estado de energia)
# Aprendimos que los objetos pueden tener distintos estados y que aun con distintos estados, los objetos pueden entender los mismos mensajes

from aves import roberta

print("Llamemos a Roberta")
print("Roberta al comienzo tiene una energia de: ", roberta.energia)
roberta.volar_en_circulos()
print("Energia despues de volar: ", roberta.energia)

# Roberta gasta menos energia al volar
# Roberta entiende los mismos mensajes que Pepita y Anastasia, pero el mismo mensaje no le afecta igual que a Pepita y Anastasia

roberta.comer_alpiste()
print("Energia despues de comer alpiste: ", roberta.energia)

#Roberta no come alpiste porque es un Dragon y por eso tambien tenia mas energia 

roberta.escupir_fuego()
print("Energia despues de escupir fuego: ", roberta.energia)

#Roberta cuando escupe fuego gasta energia
#Los dragones comen peces

roberta.comer_peces(200)
print("Energia despues de comer peces: ", roberta.energia)

#Aprendimos que hay objetos que entienden los mismos objetos que entienden los mismos mensajes aunque no sean de la misma clase
# Los objetos forman parte de la clase
#Las clases engloban objetos con caracteristicas
# Cada individuo dentro de una clase se lo conoce como INSTANCIAS

#Los obejtos cuentan con una interface
# Interface es el conjunto de mensajes que entienden

#Los objetos que comparten la interfaz son polimorficos

#En estos casos vemos un polimorfismo parcial (comparten cierta parte de la interfaz)

#El polimorfismo tiene sentido para nosotros, para los objetos esto no tiene sentido porque no lo saben
# Los objetos no saben si son polimorficos
