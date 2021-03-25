import pygame
from scenes.game_scene import Game_scene

class Game:

    def __init__(self):
        pygame.init()

        self.running = True

        screen_size = (800, 600)
        self.screen = pygame.display.set_mode(screen_size)

        self.scene = Game_scene(self.screen)
        while self.running:
            self.update()
        
    def update(self):
        evts = pygame.event.get()

        self.screen.fill((0, 0, 0))

        self.events(evts)
        self.scene.update(evts)

    def events(self, evts):
        for evt in evts:
            if evt.type == pygame.QUIT:
                self.running = False

        return evts