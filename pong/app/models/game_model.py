import requests

class Game_model:
    _url = "http://localhost:5002/games"

    def __init__(self, name, players = [], id = None):
        self.id = id
        self.name = name
        self.players = players

    @staticmethod
    def all():
        json = requests.get(Game_model._url).json()

        return list(map(lambda game: Game_model(
            id = game["id"],
            name = game["name"],
            players = game["players"]
        ), json))