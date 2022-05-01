import pygame
from entities.perso import Perso


class Checkpoint:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.width=40
        self.height=50

    def Draw(self):
        import data.variables as var
        pygame.draw.rect(var.ecran, "#FEDF00", (self.x, self.y, self.width, self.height))

    def Collision(self, player):
        import data.variables as var
        if type(player) is Perso and self.y <= player.y and player.x >= self.x and player.x <= self.x+self.width and player.y <= self.y+self.height:
            player.xSaved=player.x
            player.ySaved=player.y
            player.indexScreenSaved=var.indexNiveau