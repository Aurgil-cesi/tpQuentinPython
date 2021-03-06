from flask import json
from .resource import Resource

class Player_resource(Resource):

    def __init__(self, service):
        super(Player_resource, self).__init__(service)

    def all(self):

        players = self.service.all()

        return self.server.response_class(
            response = self.modelClass.toJsons(players),
            status = 200,
            mimetype = "application/json"
        )

    def one(self, id):

        player = self.service.one(id)

        if(player):
            return self.server.response_class(
                response = player.toJson(),
                status = 200,
                mimetype = "application/json"
            )
        else:
            return self.server.response_class(
                status = 404
            )

    def create(self, player):

        player = self.service.create(self.modelClass(
            username = player['username']
        ))
    
        return self.server.response_class(
            status = 201,
        )