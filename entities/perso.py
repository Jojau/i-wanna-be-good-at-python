import math
import pygame

from screens.gameover import GameOverScreen

class Perso:
    def __init__(self, xInit = 100, yInit = 800):
        self.x=xInit
        self.y=yInit

        self.rayon=15

        self.xSaved=xInit
        self.ySaved=yInit
        self.indexScreenSaved=0

        self.vit=300

        self.remainingJumps=1
        self.currentJumpForce=0
        self.maxJumpForce=850

    def Draw(self):
        import data.variables as var
        pygame.draw.circle(var.ecran, '#e1c699', (self.x, self.y), self.rayon)

    def Update(self, deltaTime, playerInverse):
        import data.variables as var
        from data.map import niveaux

        # Déplacement latéraux
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.x = (self.x + deltaTime * self.vit)
            
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.x = (self.x - deltaTime * self.vit)
        
        # Saut
        self.y -= deltaTime * self.currentJumpForce
        self.currentJumpForce -= deltaTime*900
        if self.currentJumpForce<0: self.currentJumpForce=0

        # Gravité
        self.y += deltaTime * var.gravity

        # Sortie de niveau
        # Mort sur les côtés
        if self.x>var.vw or self.x<0:
            print("player est mort dans le vide. X:"+str(self.x))
            a=GameOverScreen()
            a.Display()
            var.paused=True
            var.morts += 1
        # Changement de niveaux
        if self.y>var.vh:
                if var.indexNiveau < len(niveaux)-1:
                    self.y=0
                    var.indexNiveau+=1
                else:
                    self.y=var.vh
        if self.y<0:
                if var.indexNiveau > 0:
                    self.y=var.vh
                    var.indexNiveau-=1
                else:
                    self.y=0

        # Mort si en collision avec playerInverse
        if math.sqrt((playerInverse.x-self.x)**2+(playerInverse.y-self.y)**2) <= self.rayon:
            print("Les deux players se sont fait un câlin fatal")
            a=GameOverScreen()
            a.Display()
            var.paused=True
            var.morts += 1
        

    def Saut(self, event):     
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if self.remainingJumps > 0:
                    self.currentJumpForce = self.maxJumpForce
                    self.remainingJumps -=1

    def Respawn(self, event, playerInverse):
        import data.variables as var
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                self.x=self.xSaved
                self.y=self.ySaved
                self.remainingJumps=0
                self.currentJumpForce=0
                
                playerInverse.typeInversion="centrale"
                playerInverse.Update(self)

                var.indexNiveau=self.indexScreenSaved
                var.paused=False