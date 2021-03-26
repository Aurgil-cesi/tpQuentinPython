import pygame
from rect import Rect

class Cell(Rect):

    def __init__(self, game, coords, size):
        super(Cell, self).__init__(game, coords, size)

    def update(self, evts):
        self.process_events(evts)

    def process_events(self, evts):
        pass