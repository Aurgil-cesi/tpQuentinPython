from flask import json

class Model:

    def __init__(self):
        pass

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    @staticmethod
    def toJsons(models):
        return json.dumps(models, default=lambda o: o.__dict__)