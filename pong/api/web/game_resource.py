from flask import json
from .resource import Resource

class Game_resource(Resource):

    def __init__(self, service):
        super(Game_resource, self).__init__(service)

    def all(self):
        
        games = self.service.all()

        return self.server.response_class(
            response = self.modelClass.toJsons(games),
            status = 200,
            mimetype = "application/json"
        )

    def allWithPlayers(self):

        games = self.service.allWithPlayers()

        return self.server.response_class(
            response = self.modelClass.toJsons(games),
            status = 200,
            mimetype = "application/json"
        )

    def one(self, id):
        
        game = self.service.one(id)

        if(game):
            return self.server.response_class(
                response = game.toJson(),
                status = 200,
                mimetype = "application/json"
            )
        else:
            return self.server.response_class(
                status = 404
            )

    def create(self, gameJson):

        self.service.create(self.modelClass(
            name = gameJson["name"]
        ))

        return self.server.response_class(
            status = 201,
        )
        