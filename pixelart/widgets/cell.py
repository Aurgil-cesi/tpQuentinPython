import pygame
from rect import Rect
from colors import Colors

class Cell(Rect):

    COLORS_LIST = [
        Colors.WHITE,
        Colors.BLACK
    ]

    def __init__(self, game, coords, size):
        super(Cell, self).__init__(game, coords, size)

        self.color = Cell.COLORS_LIST[1]

    def update(self, evts):
        self.process_events(evts)

    def process_events(self, evts):
        pass