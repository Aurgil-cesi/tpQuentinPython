import requests
from json import dumps

class Cell_model:

    _url = "http://localhost:5003"

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    @staticmethod
    def all():
        json = requests.get(f"{Cell_model._url}/full").json()

        return list(map(lambda cell: Cell_model(
            x = cell["x"],
            y = cell["y"],
            color = cell["color"]
        ), json))

    @staticmethod
    def update(cell):
        requests.post(
            f"{Cell_model._url}/place",
            dumps({
                "x": cell.x,
                "y": cell.y,
                "color": cell.color
            }),
            headers = {
                "content-type": "application/json"
            }
        )