from .service import Service

class Player_service(Service):

    def __init__(self, modelClass):
        super(Player_service, self).__init__(modelClass)

    def all(self):

        self.cursor.execute(f"select id, username from player")
        rows = self.cursor.fetchall()

        players = list(map(lambda row: self.modelClass(
            id = row[0],
            username = row[1]
        ), rows))

        return players

    def one(self, id):

        self.cursor.execute(f"select id, username from player where id = '{id}'")
        row = self.cursor.fetchone()

        if(row):
            return self.modelClass(
                id = row[0],
                username = row[1]
            )
        else:
            return None

    def create(self, player):

        print("test")
        print(player)
        self.cursor.execute(f"insert into player (username) values ('{player.username}')")
        self.connection.commit()
