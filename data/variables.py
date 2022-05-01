# Des variables globales utilisées dans tous les fichiers
import pygame

# Pygame
vw=1000
vh=950
ecran=pygame.display.set_mode((vw,vh))
pygame.display.set_caption("I wanna be good at python")

# Map
indexNiveau=0

# Contrôles
paused=False
canRetry=True

gravity=400

# Lol
morts=0