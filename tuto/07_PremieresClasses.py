import pygame

class ElementGraphique():
    def __init__(self, img, fen, x=0, y=0):
        self.image = img
        self.rect= self.image.get_rect()
        self.fenetre = fen

        # creation d'un rectangle pour positioner l'image du personnage
        self.rect.x = x
        self.rect.y = y

    def afficher(self):
        self.fenetre.blit(self.image, self.rect)

# Initialisation de la bibliotheque pygame
pygame.init()

#creation de la fenetre
largeur = 640
hauteur = 480
fenetre=pygame.display.set_mode((largeur,hauteur))


# lecture de l'image du perso

perso = ElementGraphique(pygame.image.load("perso.png").convert_alpha(), fenetre, x=60, y=80)


perso2 = ElementGraphique(pygame.image.load("perso.png").convert_alpha(), fenetre)

# lecture de l'image du fond
fond = ElementGraphique(pygame.image.load("background.jpg").convert_alpha(),fenetre)

## Ajoutons un texte fixe dans la fenetre :
# Choix de la police pour le texte
font = pygame.font.Font(None, 34)

# Creation de l'image correspondant au texte
texte = ElementGraphique(font.render('dot biten', True, (3, 45, 49)), fenetre, x=10, y=10)


# servira a regler l'horloge du jeu
horloge = pygame.time.Clock()

# la boucle dont on veut sortir :
#   - en appuyant sur ESCAPE
#   - en cliquant sur le bouton de fermeture
i=1;
continuer=1
while continuer:

    # fixons le nombre max de frames / secondes
    horloge.tick(30)

    i=i+1
    print (i)

    # on recupere l'etat du clavier
    touches = pygame.key.get_pressed();

    # si la touche ESC est enfoncee, on sortira
    # au debut du prochain tour de boucle
    if touches[pygame.K_ESCAPE] :
        continuer=0

    perso2.rect.x += 5
    perso2.rect.y += 5

    if touches[pygame.K_RIGHT] :
        perso.rect.x += 5


    # Affichage du fond
    fond.afficher()

    # Affichage Perso
    perso.afficher()

    perso2.afficher()

    # Affichage du Texte
    texte.afficher()

    # rafraichissement
    pygame.display.flip()

    # Si on a clique sur le bouton de fermeture on sortira
    # au debut du prochain tour de boucle
    # Pour cela, on parcours la liste des evenements
    # et on cherche un QUIT...
    for event in pygame.event.get():   # parcours de la liste des evenements recus
        if event.type == pygame.QUIT:     #Si un de ces evenements est de type QUIT
            continuer = 0	   # On arrete la boucle

# fin du programme principal...
pygame.quit()
