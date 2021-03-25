from .service import Service

class Game_service(Service):

    def __init__(self, modelClass):
        super(Game_service, self).__init__(modelClass)

    def all(self):

        self.cursor.execute(f"select id, name from game")
        rows = self.cursor.fetchall()

        games = list(map(lambda row: self.modelClass(
            id = row[0],
            name = row[1]
        ), rows))

        return games

    def one(self, id):

        self.cursor.execute(f"select id, name from game where id = '{id}'")
        row = self.cursor.fetchone()

        if(row):
            return self.modelClass(
                id = row[0],
                name = row[1]
            )
        else:
            return None

    def create(self, game):

        self.cursor.execute(f"insert into game (name) values ('{game.name}')")
        self.connection.commit()