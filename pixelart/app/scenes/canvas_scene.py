from .scene import Scene
from widgets.grille import Grille
import pygame
from constants import GRILLE_SIZE, CELL_SIZE

class Canvas_scene(Scene):

    def __init__(self, game):
        super(Canvas_scene, self).__init__(game)

        self.grille = Grille(self.game, GRILLE_SIZE, CELL_SIZE)

    def update(self, evts):

        # Gestion des événements
        self.process_events(evts)

        # Mise à jour des éléments de la scéne
        self.grille.update(evts)

    def process_events(self, evts):
        pass