from flask import json
from .resource import Resource

class Player_resource(Resource):

    def __init__(self):
        super(Player_resource, self).__init__()

    def players(self):

        (connection, cursor) = self.db.connect()

        query = f"select id, username from player"
        cursor.execute(query)
        rows = cursor.fetchall()

        players = list(map(lambda row: {
            "id": row[0],
            "username": row[1]
        }, rows))

        return self.server.response_class(
            response = json.dumps(players),
            status = 200,
            mimetype = "application/json"
        )

    def player(self, id):

        (connection, cursor) = self.db.connect()

        query = f"select id, username from player where id = '{id}'"
        cursor.execute(query)
        row = cursor.fetchone()

        if(row):
            player = {
                "id": row[0],
                "username": row[1],
            }

            return self.server.response_class(
                response = json.dumps(player),
                status = 200,
                mimetype = "application/json"
            )
        else:
            return self.server.response_class(
                status = 404
            )

    def create(self, player):

        (connection, cursor) = self.db.connect()

        username = player["username"]
        query = f"insert into player (username) values ('{username}')"
        cursor.execute(query)

        connection.commit()
    
        return self.server.response_class(
            response = json.dumps(player),
            status = 201,
            mimetype = "application/json"
        )