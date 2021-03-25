from flask import Flask, render_template, request, json
import sqlite3 as sql
from database.database import Database
from web.resource import Resource
from services.service import Service

# Initialisation
app = Flask(__name__, template_folder = "templates")
database = Database()

# Resources
Service.db = database
Resource.server = app

from web.player_resource import Player_resource
from services.player_service import Player_service
from models.player_model import Player_model
player_res = Player_resource(Player_service(Player_model))

from web.game_resource import Game_resource
from services.game_service import Game_service
from models.game_model import Game_model
game_res = Game_resource(Game_service(Game_model))

# Routes
@app.route("/players", methods=["POST", "GET"])
@app.route("/players/<id>", methods=["GET"])
def players_route(id=None):
    if request.method == "GET":
        if(id == None):
            return player_res.all()
        else:
            return player_res.one(id)
    elif request.method == "POST":
        return player_res.create(request.get_json())

@app.route("/games", methods=["GET", "POST"])
@app.route("/games/<id>", methods=["GET"])
def games_route(id=None):
    if request.method == "GET":
        if id == None:
            return game_res.all()
        else:
            return game_res.one(id)
    elif request.method == "POST":
        return game_res.create(request.get_json())

# Start
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5002, debug = True)