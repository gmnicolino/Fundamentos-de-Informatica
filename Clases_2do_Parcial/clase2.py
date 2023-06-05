# TAREA: https://pokeapi.com/api/v2/pokemon/ditto
#1. describir las partes de la url
#2. ¿que respuesta obtenes al hacer un get a esa url?
#3. ¿cual es el content type de esa respuesta?
#4. ¿cual es el status code de la respuesta?
#5. ¿cuantas habilidades tiene este pokemon?


#1. La URL proporcionada se divide en varias partes:

# - Protocolo: "https://" indica que se utiliza el protocolo seguro HTTP para la comunicación.
# - Dominio: "pokeapi.com" es el dominio del sitio web al que se hace la solicitud.
# - Ruta: "/api/v2/pokemon/ditto" es la ruta específica dentro del dominio que se está solicitando. En este caso, se está solicitando información sobre el Pokémon llamado "ditto".

# 2. Al hacer una solicitud GET a la URL "https://pokeapi.com/api/v2/pokemon/ditto", se obtiene una respuesta con información sobre el Pokémon Ditto. Dicha respuesta contiene detalles como su nombre, número de la Pokédex, altura, peso, estadísticas, habilidades y más.

# 3. El tipo de contenido (content type) de la respuesta puede variar según la configuración del servidor. Sin embargo, en general, la API de PokeAPI suele devolver respuestas en formato JSON. Por lo tanto, es probable que el content type de esta respuesta sea "application/json".

# 4. El código de estado (status code) de la respuesta puede variar según la situación. Sin embargo, si la solicitud es exitosa y se encuentra la información del Pokémon Ditto, el status code típico sería 200, que indica una respuesta exitosa.

# 5. El número de habilidades que tiene el Pokémon Ditto puede ser obtenido al analizar la respuesta de la solicitud. 
# El campo correspondiente a las habilidades se encuentra en la estructura JSON de la respuesta. Cada habilidad se representa como un objeto dentro de una lista. 
# Para determinar cuántas habilidades tiene Ditto, se puede contar el número de elementos en esa lista de habilidades.



#RESPUESTAS CORRECTAS:

#Para que una API sea rest tienen que en algun momento mapear recursos
#Cada vez que tenemos un recurso distinto la URL cambia

#PROTOCOLO: https://
#DOMINIO : www.mercadolibre.com     (el dominio está enmascarando un IP)
#RECURSOS : /aros_de_plata

#Recursos son las cosas que puedo consultar en la base de datos

#Dominio se compra y es como la máscara que se le pone a las IP


#La URL funciona localizando un recurso que accedo a traves de internet
#La PAD (accedo de forma local) es la direccion exacta hacia una carpeta, recurso en una computadora exacta.

#2.
import requests

respuesta = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")

contenido_respuesta =respuesta.json()
print(contenido_respuesta)

#JSON expresa como un diccionario

print(contenido_respuesta.keys)

#Me da todos los contenidos asociados al recurso DITTO por los detalles de las habilidades, forma, peso, base de experiencia, etc

print(respuesta.headers["Content-Type"])

#Me devuelve: application/json; charset=utf-8
#Puede traer un HTML no es un lenguaje de programacion, es un lenguaje de hipertexto (es un texto en si)

#Por protocolo http se pueden enviar solamente textos

print(respuesta.status_code)

#Me devuelve: 200 (esto significa que esta todo OK)

print(f`Tiene {len(contenido_respuesta["abilities"])} habilidades´)
print(contenido_respuesta["abilities"])


#               ----------------------------------------------------------------------------------------------------------------------------------------

import requests 

rta = requests.get("https://pokeapi.co/api/v2/ability/150")
print(rta.json())

#ability es un recurso porque puedo acceder a ella ....?

#cuando usamos /un recurso , con un get traemos todos los items de ese recurso
#puedo acceder a cada uno de los items con: /recurso/id
#id es el item en particular (esta asociado a la base de datos) (accedo a un item particular de ese recurso)

#A todas las bases de datos les puedo poner un id mio para que no me la hackeen.

#Parametros: lo que agrego a la URL 


#https://github.com/AJVelezRueda/Fundamentos_de_informatica/blob/master/WEB_%26_HTTP/HTTP_%26_REST.md#3-parametros

#Puedo filtrar mediante la URL a que cosas quiero acceder de la API, a traves de las query params (todas las claves que le paso a la API atraves de la URL para filtrar la busqueda en su base de datos)

#/recurso (get) es listar todos los recursos
#/recurso /id (get) me muestra el item del recurso
#/recurso /id (delete) borra ese item
#/recurso /id (post/patch) modifica ese item

#El patch es para reescribir
#El post es para escribir de cero

#Si hacemos post a una URL estamos pidiendo que nos anote los datos en la base de datos ...???
#Si hacemos un post a la URL le tengo que pasar los datos (puede ser por json.data)

# GET /ventas/: consultar todos (listar)
# DELETE /ventas/: borrar todos
# POST /ventas/: crear uno
# POST /ventas/1 crear uno con ID (QMP no lo soporta)
# GET /ventas/1: consultar uno
# PUT /ventas/1: modificar uno
# DELETE /ventas/1: eliminar uno

#Cuando quiero crear un nuevo item lo hago sobre el /recursos no el /recursos/id
#Quedaria: /recurso (post) agrega un item 

#FLAT
#BACK
#FRONT


