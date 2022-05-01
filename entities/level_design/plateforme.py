import pygame
from entities.perso import Perso

class Plateforme:
    def __init__(self, xLeft, yTop, xRight, yBottom):
        self.x=xLeft
        self.y=yTop
        self.width=xRight-xLeft
        self.height=yBottom-yTop

    def Draw(self):
        import data.variables as var
        pygame.draw.rect(var.ecran, "#88540B", (self.x, self.y, self.width, self.height))

    def checkCollisionWithPlayer(self, player):
        Xn = max(self.x, min(player.x, self.x+self.width))
        Yn = max(self.y, min(player.y, self.y+self.height))
        Dx = Xn - player.x
        Dy = Yn - player.y
        return (Dx**2 + Dy**2) <= player.rayon**2

    def Collision(self, entite):
        # Si on est en collision
        if type(entite) is Perso and self.checkCollisionWithPlayer(entite):
            # On regarde notre position par rapport au point central
            xC=self.x+self.width/2
            yC=self.y+self.height/2

            if entite.y>self.y and entite.y<self.y+self.height:
                # Gauche
                if entite.x<xC:
                    entite.x=self.x-entite.rayon

                # Droite
                if entite.x>xC:
                    entite.x=self.x+self.width+entite.rayon

            if entite.x>self.x and entite.x<self.x+self.width:
                # Haut
                if entite.y<yC:
                    entite.y=self.y-entite.rayon
                    entite.remainingJumps = 1
                        
                # Bas
                if entite.y>yC:
                    entite.y=self.y+self.height+entite.rayon
                    entite.currentJumpForce = entite.currentJumpForce/2