from flask import Flask
from web.resource import Resource
from repositories.repository import Repository
from services.service import Service
from constants import app, database
from configuration import SERVEUR_HOST, SERVEUR_PORT, SERVEUR_DEBUG

# Models
from models.player_model import Player_model
from models.game_model import Game_model
Service.models = {
    "player": Player_model,
    "game": Game_model
}

# Initialisation statiques
Repository.db = database
Resource.server = app

# Ajout des routes
import player_routes
import game_routes

# Start
if __name__ == "__main__":
    app.run(host = SERVEUR_HOST, port = SERVEUR_PORT, debug = SERVEUR_DEBUG)