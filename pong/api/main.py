from flask import Flask
from web.resource import Resource
from repositories.repository import Repository
from constants import app, database
from configuration import SERVEUR_HOST, SERVEUR_PORT, SERVEUR_DEBUG

# Initialisation statiques
Repository.db = database
Resource.server = app

# Ajout des routes
import player_routes
import game_routes

# Start
if __name__ == "__main__":
    app.run(host = SERVEUR_HOST, port = SERVEUR_PORT, debug = SERVEUR_DEBUG)