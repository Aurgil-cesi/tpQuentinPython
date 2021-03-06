from flask import request
from constants import app

from web.game_resource import Game_resource
from services.game_service import Game_service
from repositories.game_repository import Game_repository

# Initialisation de la ressource
game_res = Game_resource(service = Game_service(repository = Game_repository()))

# Routes
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

@app.route("/games/players")
def games_players():
    if request.method == "GET":
        return game_res.allWithPlayers()