import pygame
import pygame_gui
from scenes.game_scene import Game_scene
from scenes.home_scene import Home_scene

class Game:

    def __init__(self):
        pygame.init()

        self.running = True

        # Création de l'écran
        screen_size = (800, 600)
        self.screen = pygame.display.set_mode(screen_size)

        # Tick d'update
        self.tick = pygame.time.Clock().tick(40)

        # Initialisation du manager de pygame_gui
        self.manager = pygame_gui.UIManager(screen_size)

        # Chargement de la scene par défaut
        self.scene = Home_scene(self)

        # Boucle du jeu
        while self.running:
            self.update()
        
    def update(self):
        evts = pygame.event.get()

        self.screen.fill((0, 0, 0))

        self.events(evts)

        self.manager.update(self.tick)
        self.manager.draw_ui(self.screen)

        self.scene.update(evts)
        pygame.display.update()

    def events(self, evts):
        for evt in evts:
            if evt.type == pygame.QUIT:
                self.running = False

            elif evt.type == pygame.KEYDOWN:
                if evt.key == pygame.K_w:
                    if isinstance(self.scene, Home_scene):
                        self.scene = Game_scene(self)
                    elif isinstance(self.scene, Game_scene):
                        self.scene = Home_scene(self)

            self.manager.process_events(evt)