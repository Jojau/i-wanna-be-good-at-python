import pygame
from entities.perso import Perso

color = {
  "centrale": '#00B7EB', #Cyan
  "verticale": '#D9381E', #Vermillion
  "horizontale": "#DF73FF" #Heliotrope
}

class BlocInversion:
    def __init__(self, x, y, typeInversion):
        self.x=x
        self.y=y
        self.width=40
        self.height=50

        self.typeInversion = typeInversion

    def Draw(self):
        import data.variables as var
        pygame.draw.rect(var.ecran, color[self.typeInversion], (self.x, self.y, self.width, self.height))

    def Collision(self, player, playerInverse):
        import data.variables as var
        if type(player) is Perso and self.y <= player.y+player.rayon and player.x+player.rayon >= self.x and player.x-player.rayon <= self.x+self.width and player.y-player.rayon <= self.y+self.height:
            playerInverse.typeInversion=self.typeInversion