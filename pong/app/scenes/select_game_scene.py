from .scene import Scene
from models.player_model import Player_model
from models.game_model import Game_model
import pygame
import pygame_gui

class Select_game_scene(Scene):

    def __init__(self, game):
        super(Select_game_scene, self).__init__(game)

        self.players = Player_model.all()
        self.games = Game_model.all()

        # Relative coords
        (screen_w, screen_h) = self.screen.get_size()
        coords_rel_x, coords_rel_y = screen_w / 2, screen_h / 3

        # Texte pour demander de choisir un joueur et un jeu
        font = pygame.font.Font(None, 30)
        title = font.render("Sélectionner un joueur et une partie", True, (255, 255, 255))
        title_rec = title.get_rect()

        title_size = (title_rec.width, title_rec.height)
        title_coords = (coords_rel_x - (title_size[0] / 2), coords_rel_y - (title_size[1] / 2))
        title_rec.x, title_rec.y = title_coords[0], title_coords[1]
        self.title = (title, title_rec)

        # Sélecteur de joueur
        select_player_size = (200, 100)
        select_player_coords = (coords_rel_x - 200 - select_player_size[0] / 2, coords_rel_y + (title_size[1] / 2) + 20)
        self.select_player = pygame_gui.elements.UISelectionList(
            relative_rect = pygame.Rect(
                select_player_coords, select_player_size
            ),
            item_list = list(map(lambda player: player.username, self.players)),
            manager = self.manager
        )

        # Sélecteur de partie
        select_game_size = (200, 100)
        select_game_coords = (select_player_coords[0] + select_player_size[0] + 10, coords_rel_y + (title_size[1] / 2) + 20)
        self.select_player = pygame_gui.elements.UISelectionList(
            relative_rect = pygame.Rect(
                select_game_coords, select_game_size
            ),
            item_list = list(map(lambda game: game.name, self.games)),
            manager = self.manager
        )

        # Bouton pour commencer la partie
        # start_button_size = (100, 50)
        # start_button_coords = (select_game_size[0] - start_button_size[0] / 2, coords_rel_y - start_button_size[1] / 2)
        # self.start_button = pygame_gui.elements.UIButton(
        #     relative_rect = pygame.Rect(
        #         start_button_coords, start_button_size
        #     ),
        #     text = "Commencer",
        #     manager = self.manager
        # )

    def update(self, evts):
        self.screen.blit(self.title[0], self.title[1])