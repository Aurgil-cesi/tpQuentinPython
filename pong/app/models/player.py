import requests

class Player:
    _url = "http://localhost:5002/players"

    def __init__(self, username, id = None):
        self.id = id
        self.username = username

    def player(id):
        json = requests.get(f"{Player._url}/{id}").json()

        return Player(
            id = json["id"],
            username = json["username"],
        )

    def create(player):
        requests.post(
            Player._url,
            dumps({
                "username": player.username
            }),
            headers = {
                "content-type": "application/json"
            }
        )