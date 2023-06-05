#pytest reconoce un directorio que se llama test (Esto me lo sugieren los paquetes)
#Estructura de un proyecto flask, carpetas dentro de flask:
#               assets (aca iran todos los recursos extras ej:logos, imagenes, etc)
#               app.py (en este archivo tenemos los endpoints-rutas de mi API)
#               templates (vamos a tener todas las pantabllas de mi aplicación) (no estan estaticas estas pantallas) (HTML)
#               static --> css (aqui vamos a tener los estilos de mis pantallas)

#Las API ponen los recursos

#Para que sea una API rest, los endpoints tienen que mapear recursos (cada URL mapea un recurso) y ademas que soporten bien los verbos HTTP

#Decorador: @ + " "
# @app: determina la ruta y el metodo HTTP
#       un metodo de esta app es get, el route de la aplicacion en general se escribe con ("/")

#   /prendas  --get-->  buscar las prendas
#   /prendas  --post-->  agregar una prenda nueva


# en una API rest todo lo que no sea recurso no nos permitira hacer una API rest

#   /prendas/<id>  --get-->  traiga una sola prenda de id == <id>
#   /prendas/<id>  --patch-->  modificar esa prenda

#si fuera una API cerrada voy a tener que tener un "usuarios" porque seria informacion que tengo que usar dentro de la app y tendra que quedar almacenado en la base de datos


#  ------------------------------------------------------------------------------------------------------------------------------------------------
#       MAQUETADO

# Un archivo HTML no es un lenguaje que opera contra el sistema operativo (como si lo hace Python)
# La informacion que se envia a traves del protocolo HTTP es si o si texto. 
#HTML es un hipertexto 
# Se basa en etiquetas (subestructuras/cintenedores/cajitas que se pueden dibujar con HTML)

#FRONT de la APP:
#HTML me da la estructura de la IQ   ???
#CSS maquilla o decora la base que busca HTML
#JS(...) lo dinamico sabe las estructuras maquilladas

# HTML etiquetas de distintos tipos que me permiten dibujar en la pantalla
#<nombre_etiqueta></nombre_etiqueta>


#Etiqueta de parrafo: delimita el bloque de texto <p>   </p>
#Cada p me delimita un parrafo
#La barra invertida es para cerrar


#HTML delimita el documento
