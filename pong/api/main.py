from flask import Flask
from web.resource import Resource
from services.service import Service
from constants import app, database

# Initialisation statiques
Service.db = database
Resource.server = app

# Ajout des routes
import player_routes
import game_routes

# Start
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5002, debug = True)