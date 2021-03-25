from .service import Service

class Game_service(Service):

    def __init__(self, repository):
        super(Game_service, self).__init__(repository = repository, modelname = "game")

    def all(self):
        rows = self.repository.all()

        games = list(map(lambda row: self.modelClass(
            id = row[0],
            name = row[1]
        ), rows))

        return games

    def allWithPlayers(self):

        rows = self.repository.allWithPlayers()
        player_model = self.models["player"]

        games = []
        current_game = None
        for row in rows:

            # Gestion de la game
            if not current_game or current_game.id != row[0]:
                current_game = self.modelClass(
                    id = row[0],
                    name = row[1]
                )
                games.append(current_game)
            
            # Gestion de ses joueurs
            if row[2]:
                current_game.players.append(player_model(
                    id = row[2],
                    username = row[3]
                ))

        return games

    def one(self, id):
        row = self.repository.one(id)

        if(row):
            return self.modelClass(
                id = row[0],
                name = row[1]
            )
        else:
            return None

    def create(self, game):
        self.repository.create(game)