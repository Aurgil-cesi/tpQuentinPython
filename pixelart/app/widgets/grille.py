import pygame
from widgets.cell import Cell
from rect import Rect
import random
from models.cell_model import Cell_model

class Grille:
    RELOAD = 200

    def __init__(self, game, size_grille, size_cell, coords = (0, 0)):
        self.game = game
        self.screen = self.game.screen

        self.cells = []
        for x in range(size_grille[0]):

            rows = []

            for y in range(size_grille[1]):
                
                cell = Cell(self.game, 
                    coords = (
                        coords[0] + size_cell[0] * x, coords[1] + size_cell[1] * y
                    ), 
                    size = size_cell,
                    loc = (x, y)
                )

                rows.append(cell)

            self.cells.append(rows)

        self.current_reload = 0

    def update(self, evts):

        if(self.current_reload == Grille.RELOAD):
            print("Reload")
            cells_data = Cell_model.all()
            print(cells_data)
            self.current_reload = 0
        else:
            cells_data = None

        # Gestion des événements
        self.process_events(evts)

        # Mise à jour des éléments de la grille
        for rows in self.cells:
            for cell in rows:

                if cells_data:
                    cell_data = list(filter(lambda c: c.x == cell.loc[0] and c.y == cell.loc[1], cells_data))

                    if(cell_data):
                        cell.color = cell_data[0].color

                # Mise à jour de la cellule
                cell.update(evts)

                # Affichage de la cellule
                pygame.draw.rect(
                    self.screen,
                    cell.color.value,
                    # (random.randrange(256), random.randrange(256), random.randrange(256)),
                    cell
                )

        self.current_reload += 1

    def process_events(self, evts):
        
        for evt in evts:
            if evt.type == pygame.KEYDOWN:
                if evt.key == 49:
                    Cell.COLOR_CHOOSEN = 0
                elif evt.key == 50:
                    Cell.COLOR_CHOOSEN = 1
                elif evt.key == 51:
                    Cell.COLOR_CHOOSEN = 1
                elif evt.key == 52:
                    Cell.COLOR_CHOOSEN = 1
                elif evt.key == 53:
                    Cell.COLOR_CHOOSEN = 1
                elif evt.key == 54:
                    Cell.COLOR_CHOOSEN = 1
                elif evt.key == 55:
                    Cell.COLOR_CHOOSEN = 1
                elif evt.key == 56:
                    Cell.COLOR_CHOOSEN = 1
                elif evt.key == 57:
                    Cell.COLOR_CHOOSEN = 1