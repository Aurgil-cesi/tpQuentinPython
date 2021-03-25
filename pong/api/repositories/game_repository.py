from .repository import Repository

class Game_repository(Repository):

    def __init__(self):
        super(Game_repository, self).__init__()

    def all(self):
        self.cursor.execute(f"select id, name from game")
        return self.cursor.fetchall()

    def one(self, id):
        self.cursor.execute(f"select id, name from game where id = '{id}'")
        return self.cursor.fetchone()

    def create(self, game):
        self.cursor.execute(f"insert into game (name) values ('{game.name}')")
        self.connection.commit()