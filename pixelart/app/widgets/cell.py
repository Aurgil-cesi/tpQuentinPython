import pygame
from rect import Rect
from colors import Colors
from models.cell_model import Cell_model

class Cell(Rect):

    COLOR_CHOOSEN = 0
    COLORS_LIST = [
        Colors.WHITE,
        Colors.BLACK
    ]

    def __init__(self, game, coords, size, loc):
        super(Cell, self).__init__(game, coords, size)

        self._color = Colors.BLACK
        self._color_index = 1
        self.loc = loc

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        if(isinstance(color, int)):
            self._color = Cell.COLORS_LIST[color]
            self._color_index = color
        elif(isinstance(color, Colors)):
            self._color = color

            for idx in range(Cell.COLORS_LIST):
                if(Cell.COLORS_LIST[idx] == color):
                    self._color_index = idx

    @property
    def color_index(self):
        return self._color_index

    def update(self, evts):
        self.process_events(evts)

    def process_events(self, evts):
        pass
        # for evt in evts:
        #     if evt.type == pygame.MOUSEBUTTONDOWN:
        #         pos = pygame.mouse.get_pos()

        #         print(self.loc)
        #         print(int(pos[0] / self.size_cell[0]), int(pos[1] / self.size_cell[1]))
        #         if(self.collidepoint(pos)):
        #             print("test")
        #             self.color = Cell.COLOR_CHOOSEN
