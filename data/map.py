from entities.level_design.blocInversion import BlocInversion
from entities.level_design.checkpoint import Checkpoint
from entities.level_design.drapeau import Drapeau
from entities.level_design.niveau import Niveau
from entities.level_design.pic import Pic
from entities.level_design.plateforme import Plateforme

niveaux = [
    # ANCHOR Tuto
    Niveau(
        '#473d8a',
        [
            # Contour
            Plateforme(0, 0, 40, 1000),
            Plateforme(960, 0, 1000, 950),
            Plateforme(0, 0, 880, 50),
            Plateforme(120, 900, 1000, 950),

            # Le F à l'endroit
            Plateforme(360, 550, 400, 900),
            Plateforme(400, 550, 560, 600),
            Plateforme(400, 700, 520, 750),

            # Le F à l'envers
            Plateforme(600, 50, 640, 400),
            Plateforme(480, 200, 600, 250),
            Plateforme(440, 350, 640, 400),

            # Pics
            Pic(360, 50),
            Pic(680, 50),
            Pic(760, 50),
            Pic(840, 50),
            Pic(160, 850),
            Pic(240, 850),
            Pic(320, 850),
            Pic(760, 850),

            Checkpoint(400, 500)
        ]
    ),

    # ANCHOR 1er écran : symétrie centrale
    Niveau(
        "#372f6a",
        [
            # Layout global
            Plateforme(0, 0, 40, 1000),
            Plateforme(40, 150, 120, 200),
            Plateforme(40, 750, 120, 800),
            Plateforme(120, 100, 160, 850),
            Plateforme(120, 0, 880, 50),
            Plateforme(120, 900, 880, 950),
            Plateforme(840, 100, 880, 850),
            Plateforme(880, 150, 960, 200),
            Plateforme(880, 750, 960, 800),
            Plateforme(960, 0, 1000, 950),

            # Autres plateformes
            Plateforme(200, 200, 360, 250),
            Plateforme(200, 350, 320, 400),
            Plateforme(200, 550, 320, 600),
            Plateforme(200, 700, 360, 750),
            Plateforme(400, 200, 600, 250),
            Plateforme(400, 350, 600, 400),
            Plateforme(400, 550, 600, 600),
            Plateforme(400, 700, 600, 750),
            Plateforme(640, 200, 800, 250),
            Plateforme(680, 350, 800, 400),
            Plateforme(680, 550, 800, 600),
            Plateforme(640, 700, 800, 750),
            Plateforme(480, 100, 520, 200),
            Plateforme(480, 750, 520, 850),
            Plateforme(480, 400, 520, 450),
            Plateforme(480, 500, 520, 550),

            # Pics
            Pic(880, 0),
            Pic(920, 0),
            Pic(320, 50),
            Pic(480, 50),
            Pic(760, 50),
            Pic(200, 150),
            Pic(240, 150),
            Pic(640, 150),
            Pic(680, 150),
            Pic(280, 250),
            Pic(440, 250),
            Pic(480, 250),
            Pic(520, 250),
            Pic(680, 250),
            Pic(200, 300),
            Pic(750, 300),
            Pic(200, 400),
            Pic(280, 400),
            Pic(680, 400),
            Pic(760, 400),
            Pic(240, 500),
            Pic(720, 500),
            Pic(200, 650),
            Pic(280, 650),
            Pic(320, 650),
            Pic(440, 650),
            Pic(480, 650),
            Pic(520, 650),
            Pic(640, 650),
            Pic(680, 650),
            Pic(760, 650),
            Pic(280, 750),
            Pic(760, 750),
            Pic(400, 850),
            Pic(560, 850),
            Pic(40, 900),
            Pic(80, 900),

            # Sauvegarde
            Checkpoint(80, 100)
        ]
    ),

    # ANCHOR 2ème niveau : Symétrie verticale
    Niveau(
        "#241f47",
        [
            # Layout global
            Plateforme(0, 0, 40, 1000),
            Plateforme(40, 150, 120, 200),
            Plateforme(40, 750, 120, 800),
            Plateforme(120, 100, 160, 850),
            Plateforme(120, 0, 880, 50),
            Plateforme(120, 900, 880, 950),
            Plateforme(840, 100, 880, 850),
            Plateforme(880, 150, 960, 200),
            Plateforme(880, 750, 960, 800),
            Plateforme(960, 0, 1000, 950),

            # Plateformes
            # La croix
            Plateforme(560, 100, 600, 350),
            Plateforme(600, 350, 800, 400),
            Plateforme(600, 550, 800, 600),
            Plateforme(560, 600, 600, 850),
            Plateforme(400, 600, 440, 850),
            Plateforme(200, 550, 400, 600),
            Plateforme(200, 350, 400, 400),
            Plateforme(400, 100, 440, 350),
            # Carrés horizontaux
            Plateforme(160, 450, 200, 500),
            Plateforme(240, 450, 280, 500),
            Plateforme(320, 450, 360, 500),
            Plateforme(400, 450, 440, 500),
            Plateforme(480, 450, 520, 500),
            Plateforme(560, 450, 600, 500),
            Plateforme(640, 450, 680, 500),
            Plateforme(720, 450, 760, 500),
            Plateforme(800, 450, 840, 500),
            # Carrés verticaux
            Plateforme(480, 150, 520, 200),
            Plateforme(480, 300, 520, 350),
            Plateforme(480, 450, 520, 500),
            Plateforme(480, 600, 520, 650),
            Plateforme(480, 750, 520, 800),

            # Pics
            Pic(40, 0),
            Pic(80, 0),
            Pic(640, 50),
            Pic(200, 300),
            Pic(160, 550),
            Pic(520, 600),
            Pic(480, 800),
            Pic(880, 900),
            Pic(920, 900),

            # Symétries
            BlocInversion(600, 300, "verticale"),
            BlocInversion(360, 300, "centrale"),

            # Sauvegarde
            Checkpoint(880, 100)
        ]
    ),

    # ANCHOR 3ème niveau : symétrie horizontale
    Niveau(
        "#121023",
        [
            # Layout global
            Plateforme(0, 0, 40, 1000),
            Plateforme(40, 150, 120, 200),
            Plateforme(40, 750, 120, 800),
            Plateforme(120, 150, 160, 800),
            Plateforme(120, 0, 880, 50),
            Plateforme(120, 900, 880, 950),
            Plateforme(840, 150, 880, 800),
            Plateforme(880, 150, 960, 200),
            Plateforme(880, 750, 960, 800),
            Plateforme(960, 0, 1000, 950),

            # Autre plateformes
            Plateforme(240, 150, 280, 200),
            Plateforme(320, 150, 680, 200),
            Plateforme(720, 150, 760, 200),
            Plateforme(720, 250, 760, 700),
            Plateforme(720, 750, 760, 800),
            Plateforme(320, 750, 680, 800),
            Plateforme(240, 750, 280, 800),
            Plateforme(240, 250, 280, 700),

            Plateforme(360, 300, 400, 350),
            Plateforme(440, 300, 560, 350),
            Plateforme(600, 300, 640, 350),
            Plateforme(600, 400, 640, 550),
            Plateforme(600, 600, 640, 650),
            Plateforme(440, 600, 560, 650),
            Plateforme(360, 600, 400, 650),
            Plateforme(360, 400, 400, 550),
            Plateforme(480, 450, 520, 500),

            # Pics
            Pic(880, 0),
            Pic(920, 0),
            Pic(280, 50),
            Pic(320, 50),
            Pic(360, 50),
            Pic(440, 50),
            Pic(720, 50),
            Pic(560, 100),
            Pic(600, 100),
            Pic(720, 100),
            Pic(320, 200),
            Pic(480, 200),
            Pic(320, 400),
            Pic(480, 400),
            Pic(160, 450),
            Pic(200, 450),
            Pic(400, 450),
            Pic(520, 450),
            Pic(680, 550),
            Pic(360, 650),
            Pic(360, 700),
            Pic(760, 750),
            Pic(800, 750),
            Pic(600, 850),
            Pic(40, 900),
            Pic(80, 900),

            Checkpoint(80, 100),
            Checkpoint(920, 100),
            Checkpoint(120,850),

            BlocInversion(880, 100, "horizontale"),
            BlocInversion(480, 550, "verticale"),
            BlocInversion(40, 800, "centrale"),

            Drapeau(880, 900),
            Drapeau(920, 900)
        ]
    )
]