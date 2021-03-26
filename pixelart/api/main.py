from flask import Flask
from web.resource import Resource
from repositories.repository import Repository
from services.service import Service
from constants import app, database
from configuration import SERVEUR_HOST, SERVEUR_PORT, SERVEUR_DEBUG

# Models
from models.cell_model import Cell_model
Service.models = {
    "cell": Cell_model
}

# Initialisation statiques
Repository.db = database
Resource.server = app

# Ajout des routes
import cell_routes

# Start
if __name__ == "__main__":
    app.run(host = SERVEUR_HOST, port = SERVEUR_PORT, debug = SERVEUR_DEBUG)