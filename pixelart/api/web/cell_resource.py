from flask import json
from .resource import Resource

class Cell_resource(Resource):

    def __init__(self, service):
        super(Cell_resource, self).__init__(service)

    def all(self):

        cells = self.service.all()

        return self.server.response_class(
            response = self.modelClass.toJsons(cells),
            status = 200,
            mimetype = "application/json"
        )

    def update(self, cell):

        self.service.update(self.modelClass(
            x = cell["x"],
            y = cell["y"],
            color = cell["color"]
        ))

        return self.server.response_class(
            status = 201
        )