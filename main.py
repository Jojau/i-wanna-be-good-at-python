import sys
import pygame
from entities.perso import Perso
import data.map as map
import data.variables as var
from entities.persoInverse import PersoInverse

pygame.init()

# Initialiser mon personnage
monPerso = Perso(900, 800)
monPersoInverse = PersoInverse(monPerso)

# La boucle de jeu
loop=True
getTicksLastFrame = 0
while loop:
    # Obtenir le delta time
    t=pygame.time.get_ticks()
    deltaTime=(t-getTicksLastFrame) / 1000
    getTicksLastFrame = t

    # C'est tipar
    if not var.paused:
        map.niveaux[var.indexNiveau].Draw()
        map.niveaux[var.indexNiveau].Collisions([monPerso, monPersoInverse])
        monPerso.Draw()
        monPersoInverse.Draw()

        # Si le jeu lag et met beaucoup trop de temps à charger (genre au début), on freeze le perso pour éviter qu'il fasse des dingueries qu'on ne puisse pas voir
        if deltaTime<0.5:
            monPerso.Update(deltaTime, monPersoInverse)
            monPersoInverse.Update(monPerso)

    # Contrôles
    for event in pygame.event.get():        
        # Sauter
        if not var.paused:
            monPerso.Saut(event)

        # Retry
        if var.canRetry:
            monPerso.Respawn(event, monPersoInverse)

        # Quitter le jeu
        if event.type == pygame.QUIT:
            loop=False

    pygame.display.flip()
            
pygame.quit()
sys.exit()