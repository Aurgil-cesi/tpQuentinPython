from flask import request
from constants import app

from web.cell_resource import Cell_resource
from services.cell_service import Cell_service
from repositories.cell_repository import Cell_repository

# Initialisation de la ressource
cell_res = Cell_resource(service = Cell_service(repository = Cell_repository()))

# Les routes
@app.route("/place", methods=["POST"])
@app.route("/full", methods=["GET"])
def players_route(id=None):
    if request.method == "GET":
        return cell_res.all()
    elif request.method == "POST":
        return cell_res.update(request.get_json())