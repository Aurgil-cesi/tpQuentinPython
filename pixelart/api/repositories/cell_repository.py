from .repository import Repository

class Cell_repository(Repository):

    def __init__(self):
        super(Cell_repository, self).__init__()

    def all(self):

        self.cursor.execute("select x, y, color from cell")
        return self.cursor.fetchall()

    def one(self, x, y):
        print(x, y)
        self.cursor.execute(f"select x, y, color from cell where x = {x} and y = {y}")
        return self.cursor.fetchone()

    def create(self, cell):
        self.cursor.execute(f"insert into cell (x, y, color) values ({cell.x}, {cell.y}, {cell.color})")
        self.connection.commit()

    def update(self, cell):
        cell_row = self.one(cell.x, cell.y)

        if cell_row:
            self.cursor.execute(f"update cell set color = {cell.color} where x = {cell.x} and y = {cell.y}")
            self.connection.commit()
        else:
            self.create(cell)