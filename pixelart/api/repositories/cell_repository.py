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

    def create(self, cells):
        if(not isinstance(cells, list)):
            cells = [cells]

        for cell in cells:
            self.cursor.execute(f"insert into cell (x, y, color) values ({cell.x}, {cell.y}, {cell.color})")
        self.connection.commit()

    def update(self, cell):
        cell_row = self.one(cell.x, cell.y)

        if cell_row:
            self.cursor.execute(f"update cell set color = {cell.color} where x = {cell.x} and y = {cell.y}")
            self.connection.commit()
        else:
            self.create(cell)

    def place(self, cells):

        # Récupération des identifiants des celules existantes
        query_ids = ""
        idx = 0
        for cell in cells:
            if idx != 0:
                query_ids += " or "
            query_ids += f"x = {cell.x} and y = {cell.y}"
            idx += 1
        query = f"select x, y from cell where {query_ids}"
        self.cursor.execute(query)
        cell_exists_id = self.cursor.fetchall()
        
        for cell in cells:

            found = False
            for id in cell_exists_id:
                if cell.x == id[0] and cell.y == id[1]:
                    found = True
                    break

            if found:
                self.cursor.execute(f"update cell set color = {cell.color} where x = {cell.x} and y = {cell.y}")
            else:
                self.cursor.execute(f"insert into cell (x, y, color) values ({cell.x}, {cell.y}, {cell.color})")

        self.connection.commit()