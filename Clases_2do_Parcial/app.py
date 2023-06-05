# API rutas (en dpoinst) --> URL en las cuales se accede a los recursos

#Cuando construimos una API programamos todas las acciones que ocurren cuando un usuario accede ... ?

#Esto ya no es un script

from flask import Flask

app = Flask(__name__)

#cuando alguien le pegue ahi vas a dar la siguiente funcion:
@app.get("/")
def home():
    return "<p>Te damos la bienvenida a MacoWins</p>"

if __name__ == "__main__":
    app.run(debug=True)

#<p>   --> etiqueta que se usa para poner texto en una página web
#Canales de comunicacion: puertos en particular

#En flask vamos a usar un puerto IP

# #TAREA: 
# from flask import Flask
# prendas = [
#     {"id":1, "tipo": "pantalon", "talle": 42}
#     {"id":2, "tipo": "pantalon", "talle": 56}
# ]
# app = Flask(__name__)

# #cuando alguien le pegue ahi vas a dar la siguiente funcion:
# @app.get("/")
# def home():
#     return "<p>Te damos la bienvenida a MacoWins</p>
