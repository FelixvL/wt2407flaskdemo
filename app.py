from flask import Flask
import dinsdag
#   Huis h = new Huis("vlakbij 13")
app = Flask(__name__)
# Server
@app.route("/")   # endpoints   REST
def hello_world():
    return "<h1>Hello, World!!!!</h1>"

@app.route("/anders")   # endpoints   REST
def anderefunctie():
    return "<h1>Hello, Anders!!!!</h1>"

@app.route("/optellen/<getal1>/<getal2>")   # endpoints   REST
def lekkeroptellen(getal1, getal2):
    return dinsdag.optellen(int(getal1), int(getal2))



