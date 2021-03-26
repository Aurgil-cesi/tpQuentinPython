import pygame
from widgets.cell import Cell
from rect import Rect
import random

class Grille:

    def __init__(self, game, size_grille, size_cell, coords = (0, 0)):
        self.game = game
        self.screen = self.game.screen

        self.cells = []
        for x in range(size_grille[0]):

            rows = []

            for y in range(size_grille[1]):
                
                rows.append(Cell(self.game, (
                    coords[0] + size_cell[0] * x, coords[1] + size_cell[1] * y
                ), size_cell))

            self.cells.append(rows)

    def update(self, evts):

        # Gestion des événements
        self.process_events(evts)

        # Mise à jour des éléments de la grille
        for rows in self.cells:
            for cell in rows:

                # Mise à jour de la cellule
                cell.update(evts)

                # Affichage de la cellule
                pygame.draw.rect(
                    self.screen,
                    cell.color.value,
                    # (random.randrange(256), random.randrange(256), random.randrange(256)),
                    cell
                )

    def process_events(self, evts):
        pass