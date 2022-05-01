from entities.level_design.blocInversion import BlocInversion

class Niveau:
    def __init__(self, couleurFond = (0, 0, 0), levelDesignElements = []):
        self.couleurFond=couleurFond
        self.levelDesignElements=levelDesignElements

    def Draw(self):
        import data.variables as var
        var.ecran.fill(self.couleurFond)
        for levelDesignElement in self.levelDesignElements:
            levelDesignElement.Draw()

    def Collisions(self, players):
        for levelDesignElement in self.levelDesignElements:
            if type(levelDesignElement) is BlocInversion:
                levelDesignElement.Collision(players[0], players[1])
            else:
                for player in players:
                    levelDesignElement.Collision(player)