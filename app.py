from flask import Flask, render_template, request, flash, redirect, url_for
import random
from funciones import sorteoEscalas, sorteoTemas
app = Flask(__name__)
# A veces da error. Incluir secret key por si acaso
#app.secret_key = "ljkfdsaldskjfdalkj"


@app.route("/")
def home():
    m = sorteoEscalas()
    return render_template("home.html", m=m)

@app.route("/repertorio")
def repertorio():
    filas = sorteoTemas() 
    return render_template("repertorio.html", filas = filas)




if __name__ == "__main__":
    app.run(debug=True)

