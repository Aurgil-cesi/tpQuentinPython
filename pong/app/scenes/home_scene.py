from .scene import Scene
import pygame
import pygame_gui
from .select_game_scene import Select_game_scene

class Home_scene(Scene):

    def __init__(self, game):
        super(Home_scene, self).__init__(game)

        # Relative coords
        (screen_w, screen_h) = self.screen.get_size()
        coords_rel_x, coords_rel_y = screen_w / 2, screen_h / 2

        # Start button
        start_button_size = (100, 50)
        start_button_coords = (coords_rel_x - start_button_size[0] / 2, coords_rel_y - start_button_size[1] / 2)
        self.start_button = pygame_gui.elements.UIButton(
            relative_rect = pygame.Rect(
                start_button_coords, start_button_size
            ),
            text = "Commencer",
            manager = self.manager
        )

        # Titre de l'application
        font = pygame.font.Font(None, 64)
        title = font.render("Aurgil - PyPong", True, (255, 255, 255))
        title_rec = title.get_rect()

        title_size = (title_rec.width, title_rec.height)
        title_coords = (coords_rel_x - (title_size[0] / 2), start_button_coords[1] - title_size[1] - 20)
        title_rec.x, title_rec.y = title_coords[0], title_coords[1]
        self.title = (title, title_rec)

    def __del__(self):
        self.start_button.kill()

    def update(self, evts):
        self.events(evts)
        self.screen.blit(self.title[0], self.title[1])

    def events(self, evts):
        for evt in evts:
            if evt.type == pygame.USEREVENT:
                if evt.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if evt.ui_element == self.start_button:
                        self.game.scene = Select_game_scene(self.game)