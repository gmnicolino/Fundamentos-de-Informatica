from flask import Flask, render_template
from markupsafe import escape 

jugadores = {
    1:{"nombre":"Juan", "edad": 18, "experiencia": "si"},
    2:{"nombre":"Roman", "edad": 21, "experiencia": "no"}
}

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("home.html")

@app.get("/jugadores")
def get_all_jugadores():
        return render_template("jugadores.html", jugadores = jugadores.items())

@app.get("/jugadores/<int:id>")
def get_jugadores(id):
    if id in jugadores:
        jugador=jugadores[id]
        return render_template("jugador.html", id=id, jugador=jugador)
    else:
        return ("No existe el jugador", 404)