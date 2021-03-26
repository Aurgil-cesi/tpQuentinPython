import pygame
from rect import Rect
from colors import Colors

class Cell(Rect):

    COLOR_CHOOSEN = 0
    COLORS_LIST = [
        Colors.WHITE,
        Colors.BLACK
    ]

    def __init__(self, game, coords, size):
        super(Cell, self).__init__(game, coords, size)

        self._color = Colors.BLACK

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        if(isinstance(color, int)):
            self._color = Cell.COLORS_LIST[color]
        elif(isinstance(color, Colors)):
            self._color = color

    def update(self, evts):
        self.process_events(evts)

    def process_events(self, evts):

        for evt in evts:
            if evt.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if(self.collidepoint(pos)):
                    self.color = Cell.COLOR_CHOOSEN

        # self.color = Cell.COLOR_CHOOSEN