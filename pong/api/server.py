from flask import Flask, render_template, request, json
import sqlite3 as sql
from database.database import Database
from web.resource import Resource

# Initialisation
app = Flask(__name__, template_folder = "templates")
database = Database()

# Resources
Resource.db = database
Resource.server = app
from web.player_resource import Player_resource

player_res = Player_resource()

# Routes
@app.route("/players", methods=["POST", "GET"])
@app.route("/players/<id>", methods=["GET"])
def player(id=None):
    if request.method == "GET" and id == None:
        return player_res.players()
    elif request.method == "GET" and id != None:
        return player_res.player(id)
    elif request.method == "POST":
        return player_res.create(request.get_json())

# Start
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5002, debug = True)