import pygame

class GameOverScreen:
    def __init__(self):
        self.font = pygame.font.SysFont('GILSANUB.TTF', 100)
        self.text = self.font.render('Game Over', True, "#ffffff")

        self.font2 = pygame.font.SysFont('GILSANUB.TTF', 30)
        self.text2 = self.font2.render('Press R to try again', True, "#ffffff")

    def Display(self):
        import data.variables as var

        pygame.draw.rect(var.ecran, "#000000", (300, 450, 400, 125))

        text_rect = self.text.get_rect(center=(500, 500))
        var.ecran.blit(self.text, text_rect)

        text_rect2 = self.text2.get_rect(center=(500, 550))
        var.ecran.blit(self.text2, text_rect2)

        pygame.display.update()