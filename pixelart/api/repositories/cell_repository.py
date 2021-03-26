from .repository import Repository

class Cell_repository(Repository):

    def __init__(self):
        super(Cell_repository, self).__init__()

    def all(self):

        self.cursor.execute("select x, y, color from cell")
        return self.cursor.fetchall()

    def update(self, cell):
        self.cursor.execute(f"update cell set color = {cell.color} where x = {cell.x} and y = {cell.y}")
        self.connection.commit()