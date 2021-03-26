from .service import Service

class Cell_service(Service):

    def __init__(self, repository):
        super(Cell_service, self).__init__(repository = repository, modelname = "cell")

    def all(self):

        rows = self.repository.all()

        cells = list(map(lambda row: self.modelClass(
            x = row[0],
            y = row[1],
            color = row[2]
        ), rows))

        return cells

    def update(self, cell):

        self.repository.update(cell)

    def place(self, cells):
        self.repository.place(cells)