# python.exe -m venv .venv
# cd .venv/Scripts
# activate.bat
# py -m ensurepip --upgrade
# pip install -r requirements.txt

from flask import Flask

from flask import render_template
from flask import request
from flask import jsonify, make_response

import mysql.connector

import datetime
import pytz

from flask_cors import CORS, cross_origin

con = mysql.connector.connect(
    host="82.197.82.90",
    database="u861594054_practica4",
    user="u861594054_renepratica4",
    password="A!3!*ooC2l"
)

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    if not con.is_connected():
        con.reconnect()

    con.close()

    return render_template("index.html")

@app.route("/app")
def app2():
    if not con.is_connected():
        con.reconnect()

    con.close()

    return "<h5>Hola mamá estoy en Practica 8 :D❤️</h5>"

@app.route("/clientes")
def clientes():
    if not con.is_connected():
        con.reconnect()

    cursor = con.cursor(dictionary=True)
    sql    = """SELECT * FROM clientes"""

    cursor.execute(sql)
    registros = cursor.fetchall()

    
    con.close()
    return render_template("clientes.html", clientes=registros)


@app.route("/agenda")
def agenda():
    if not con.is_connected():
        con.reconnect()

    cursor = con.cursor(dictionary=True)
    sql    = """SELECT * FROM eventos INNER JOIN clientes ON clientes.idCliente = eventos.idCliente"""

    cursor.execute(sql)
    registros = cursor.fetchall()
    
    con.close()
    return render_template("agenda.html", agenda=registros)

