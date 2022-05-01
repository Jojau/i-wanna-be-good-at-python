import pygame
from screens.gameover import GameOverScreen

class Pic:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.width=40
        self.height=50

    def Draw(self):
        import data.variables as var
        pygame.draw.rect(var.ecran, "#676767", (self.x, self.y, self.width, self.height))

    def checkCollisionWithPlayer(self, player):
        Xn = max(self.x, min(player.x, self.x+self.width))
        Yn = max(self.y, min(player.y, self.y+self.height))
        Dx = Xn - player.x
        Dy = Yn - player.y
        return (Dx**2 + Dy**2) <= player.rayon**2

    def Collision(self, player):
        import data.variables as var
        if self.checkCollisionWithPlayer(player):
            print(str(type(player))+" est mort sur un pic. X:"+str(player.x)+" Y:"+str(player.y))
            a=GameOverScreen()
            a.Display()
            var.paused=True
            var.morts += 1