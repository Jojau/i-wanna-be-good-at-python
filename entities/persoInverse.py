import pygame

class PersoInverse:
    def __init__(self, player):
        import data.variables as var
        self.x=var.vw-player.x
        self.y=var.vh-player.y

        self.rayon = 15

        self.typeInversion = "centrale"

    def Draw(self):
        import data.variables as var
        pygame.draw.circle(var.ecran, '#e1c699', (self.x, self.y), self.rayon)

    def Update(self, player):
        import data.variables as var
        # Déplacements
        if self.typeInversion == "centrale":
            self.x = var.vw-player.x
            self.y = var.vh-player.y
        elif self.typeInversion == "verticale":
            self.x = player.x
            self.y = var.vh-player.y
        elif self.typeInversion == "horizontale":
            self.x = var.vw-player.x
            self.y = player.y