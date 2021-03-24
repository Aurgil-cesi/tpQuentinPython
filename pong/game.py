import pygame
from pygame import draw, display, event, key
from balle import Balle
from barre import Barre

class Game:

    def __init__(self):
        pygame.init()

        self.running = True

        screen_size = (800, 600)
        self.screen = display.set_mode(screen_size)

        self.balle = Balle(self.screen, (screen_size[0] / 2, screen_size[1] / 2))
        self.balle.direction = "right"

        self.barres = (Barre(self.screen), Barre(self.screen, coords = (screen_size[0], screen_size[1])))

        while self.running:
    
            self.events()
            self.update()
        
    def update(self):
        self.screen.fill((0, 0, 0))

        self.balle.update()
        for barre in self.barres:
            barre.update()
        display.update()

    def events(self):

        # Holding
        keys = key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.barres[0].move("down")
        elif keys[pygame.K_UP]:
            self.barres[0].move("up")
        elif keys[pygame.K_LEFT]:
            pass
        elif keys[pygame.K_RIGHT]:
            pass

        # Downed
        for evt in event.get():
            if evt.type == pygame.QUIT:
                self.running = False
            
            if evt.type == pygame.KEYDOWN:
                if evt.key == pygame.K_LEFT:
                    pass
                elif evt.key == pygame.K_RIGHT:
                    pass
                elif evt.key == pygame.K_UP:
                    pass
                elif evt.key == pygame.K_DOWN:
                    pass