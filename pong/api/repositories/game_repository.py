from .repository import Repository

class Game_repository(Repository):

    def __init__(self):
        super(Game_repository, self).__init__()

    def all(self):
        
        self.cursor.execute("select id, name from game")
        return self.cursor.fetchall()

    def allWithPlayers(self):
        self.cursor.execute(" ".join([
            "select gp.game_id, g.name, gp.player_id, p.username",
            "from game g",
            "left join game_player gp on g.id = gp.game_id",
            "left join player p on gp.player_id = p.id"
        ]))
        
        return self.cursor.fetchall()

    def one(self, id):
        self.cursor.execute(f"select id, name from game where id = '{id}'")
        return self.cursor.fetchone()

    def create(self, game):
        self.cursor.execute(f"insert into game (name) values ('{game.name}')")
        self.connection.commit()