import pygame

class Rect(pygame.Rect):

    def __init__(self, game, coords, size):
        super(Rect, self).__init__(coords, size)

        self.game = game
        self.screen = self.game.screen
        self.coords = coords