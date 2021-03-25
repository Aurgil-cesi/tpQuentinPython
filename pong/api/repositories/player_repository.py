from .repository import Repository

class Player_repository(Repository):

    def __init__(self):
        super(Player_repository, self).__init__()

    def all(self):
        self.cursor.execute(f"select id, username from player")
        return self.cursor.fetchall()

    def one(self, id):
        self.cursor.execute(f"select id, username from player where id = '{id}'")
        return self.cursor.fetchone()

    def create(self, player):
        self.cursor.execute(f"insert into player (username) values ('{player.username}')")
        self.connection.commit()