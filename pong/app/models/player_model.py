import requests

class Player_model:
    _url = "http://localhost:5002/players"

    def __init__(self, username, id = None):
        self.id = id
        self.username = username

    @staticmethod
    def all():
        json = requests.get(Player_model._url).json()

        return list(map(lambda player: Player_model(
            id = player["id"],
            username = player["username"]
        ), json))

    @staticmethod
    def one(id):
        json = requests.get(f"{Player_model._url}/{id}").json()

        return Player_model(
            id = json["id"],
            username = json["username"],
        )

    @staticmethod
    def create(player):
        requests.post(
            Player_model._url,
            dumps({
                "username": player.username
            }),
            headers = {
                "content-type": "application/json"
            }
        )