import pygame
from scenes.canvas_scene import Canvas_scene
from constants import GRILLE_SIZE, CELL_SIZE

class Game:

    def __init__(self):
        pygame.init()

        self.running = True

        # Création de l'écran
        screen_size = (GRILLE_SIZE[0] * CELL_SIZE[0], GRILLE_SIZE[1] * CELL_SIZE[1])
        self.screen = pygame.display.set_mode(screen_size)

        # Tick d'update
        self.tick = pygame.time.Clock().tick(40)

        # Chargement de la scene par défaut
        self.scene = Canvas_scene(self)

        # Boucle du jeu
        while self.running:
            self.update()
        
    def update(self):
        evts = pygame.event.get()

        self.screen.fill((255, 255, 255))

        self.process_events(evts)

        self.scene.update(evts)
        pygame.display.update()

    def process_events(self, evts):
        for evt in evts:
            if evt.type == pygame.QUIT:
                self.running = False