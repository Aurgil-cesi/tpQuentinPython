from flask import request
from constants import app

from web.player_resource import Player_resource
from services.player_service import Player_service
from models.player_model import Player_model

# Initialisation de la ressource
player_res = Player_resource(Player_service(Player_model))

# Les routes
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