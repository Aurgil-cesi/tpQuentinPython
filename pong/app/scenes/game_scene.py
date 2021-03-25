import pygame
from balle import Balle
from barre import Barre
from direction import Direction

class Game_scene:

    def __init__(self, screen):
        self.screen = screen

        screen_size = self.screen.get_size()
        self.balle = Balle(self.screen, (screen_size[0] / 2, screen_size[1] / 2), speed = 0.2)
        self.balle.direction = Direction.DOWN_RIGHT

        barre_size = (5, 64)
        self.barres = (
            Barre(self.screen, size = barre_size, speed = 0.5), 
            Barre(
                self.screen, 
                coords = (screen_size[0] - barre_size[0], screen_size[1] - barre_size[1]), 
                size = barre_size,
                controls = {Direction.UP: pygame.K_o, Direction.DOWN: pygame.K_l},
                speed = 0.5
            )
        )

    def update(self, evts):
        self.collis()
        self.events(evts)

        self.balle.update()
        for barre in self.barres:
            barre.update()
        pygame.display.update()

    def events(self, evts):
        for evt in evts:
            if evt.type == pygame.USEREVENT:
                self.balle.reset()

    def collis(self):
        balleRect = pygame.Rect(self.balle.coords, (self.balle.size, self.balle.size))
        for idx in range(len(self.barres)):
            barreRect = pygame.Rect(self.barres[idx].coords, self.barres[idx].size)
            
            if(balleRect.colliderect(barreRect)):
                if idx == 0:
                    if(self.balle.direction == Direction.LEFT):
                        self.balle.direction = Direction.RIGHT
                    elif self.balle.direction == Direction.DOWN_LEFT:
                        self.balle.direction = Direction.DOWN_RIGHT
                    elif self.balle.direction == Direction.UP_LEFT:
                        self.balle.direction = Direction.UP_RIGHT
                elif idx == 1:
                    if self.balle.direction == Direction.RIGHT:
                        self.balle.direction = Direction.LEFT
                    elif self.balle.direction == Direction.UP_RIGHT:
                        self.balle.direction = Direction.UP_LEFT
                    elif self.balle.direction == Direction.DOWN_RIGHT:
                        self.balle.direction = Direction.DOWN_LEFT

                self.balle.speed += 0.01