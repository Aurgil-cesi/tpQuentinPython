import pygame
from balle import Balle
from barre import Barre

class Game:

    def __init__(self):
        pygame.init()

        self.running = True

        screen_size = (800, 600)
        self.screen = pygame.display.set_mode(screen_size)

        self.balle = Balle(self.screen, (screen_size[0] / 2, screen_size[1] / 2), speed = 0.2)
        self.balle.direction = "down_right"

        barre_size = (5, 64)
        self.barres = (
            Barre(self.screen, size = barre_size, speed = 0.5), 
            Barre(
                self.screen, 
                coords = (screen_size[0] - barre_size[0], screen_size[1] - barre_size[1]), 
                size = barre_size,
                controls = {"up": pygame.K_o, "down": pygame.K_l},
                speed = 0.5
            )
        )

        while self.running:
            self.collis()
            self.events()
            self.update()
        
    def update(self):
        self.screen.fill((0, 0, 0))

        self.balle.update()
        for barre in self.barres:
            barre.update()
        pygame.display.update()

    def events(self):

        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                self.running = False
            
            if evt.type == pygame.KEYDOWN:
                pass

            if evt.type == pygame.USEREVENT:
                self.balle.reset()

    def collis(self):
        balleRect = pygame.Rect(self.balle.coords, (self.balle.size, self.balle.size))
        for idx in range(len(self.barres)):
            barreRect = pygame.Rect(self.barres[idx].coords, self.barres[idx].size)
            
            if(balleRect.colliderect(barreRect)):
                if idx == 0:
                    if(self.balle.direction == "left"):
                        self.balle.direction = "right"
                    elif self.balle.direction == "down_left":
                        self.balle.direction = "down_right"
                    elif self.balle.direction == "up_left":
                        self.balle.direction = "up_right"
                elif idx == 1:
                    if self.balle.direction == "right":
                        self.balle.direction = "left"
                    elif self.balle.direction == "up_right":
                        self.balle.direction = "up_left"
                    elif self.balle.direction == "down_right":
                        self.balle.direction = "down_left"

                self.balle.speed *= 1.05