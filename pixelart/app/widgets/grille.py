import pygame
from widgets.cell import Cell
from rect import Rect
import random
from models.cell_model import Cell_model

class Grille(Rect):
    FRAME_RELOAD = 500

    def __init__(self, game, size_grille, size_cell, coords = (0, 0)):
        super(Grille, self).__init__(game, coords = coords, size = (size_grille[0] * size_cell[0], size_grille[1] * size_cell[1]))
        self.size_grille = size_grille
        self.size_cell = size_cell

        self.queues = []
        self.cells = []
        
        self.reload()

        self.current_frame = 0

    def update(self, evts):

        # print(self.current_reload)

        if(self.current_frame == Grille.FRAME_RELOAD):
            print("Reload")
            self.reload()
            self.current_frame = 0
        else:
            cells_data = None

        # Gestion des événements
        self.process_events(evts)

        # Mise à jour des éléments de la grille
        for cell in self.cells:

            # Mise à jour de la cellule
            cell.update(evts)

            # Affichage de la cellule
            pygame.draw.rect(
                self.screen,
                cell.color.value,
                # (random.randrange(256), random.randrange(256), random.randrange(256)),
                cell
            )

        self.current_frame += 1

    def reload(self):

        # Gestion de la queue
        for cell_model in self.queues:
            Cell_model.update(cell_model)
        self.queues = []

        self.cells = []
        for cell in Cell_model.all():
            self.cells.append(Cell(
                self.game,
                coords = (self.coords[0] + self.size_cell[0] * cell.x, self.coords[1] + self.size_cell[1] * cell.y),
                size = self.size_cell,
                loc = (cell.x, cell.y)
            ))

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

            if evt.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                cell_x = int(pos[0] / self.size_cell[0])
                cell_y = int(pos[1] / self.size_cell[1])

                new_cell = None
                for cell in self.cells:
                    if cell.loc == (cell_x, cell_y):
                        cell.color = Cell.COLOR_CHOOSEN
                    else:
                        new_cell = Cell(
                            self.game,
                            coords = (self.coords[0] + self.size_cell[0] * cell_x, self.coords[1] + self.size_cell[1] * cell_y),
                            size = self.size_cell,
                            loc = (cell_x, cell_y)
                        )
                        
                if new_cell:
                    self.cells.append(new_cell)

                self.queues.append(Cell_model(
                    x = cell_x,
                    y = cell_y,
                    color = cell.color_index
                ))