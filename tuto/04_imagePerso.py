import pygame

# Initialisation de la bibliotheque pygame
pygame.init()

#creation de la fenetre
largeur = 640
hauteur = 480
fenetre=pygame.display.set_mode((largeur,hauteur))


# lecture de l'image du perso
imagePerso = pygame.image.load("perso.png").convert_alpha()

# creation d'un rectangle pour positioner l'image du personnage
rectPerso = imagePerso.get_rect()
print(rectPerso)
rectPerso.x = 100
rectPerso.y = 200
print(rectPerso)

rectPerso2 = imagePerso.get_rect()

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
    #print (i)

    # on recupere l'etat du clavier
    touches = pygame.key.get_pressed();

    # si la touche ESC est enfoncee, on sortira
    # au debut du prochain tour de boucle
    if touches[pygame.K_ESCAPE] :
        continuer=0

    if touches[pygame.K_RIGHT] :
        rectPerso.x += 5

    if touches[pygame.K_LEFT] :
        rectPerso.x += -5

    if touches[pygame.K_UP] :
        rectPerso.y += -5

    rectPerso2.x += 2
    rectPerso2.y += 5

    # Affichage Perso
    fenetre.blit(imagePerso, rectPerso)

    fenetre.blit(imagePerso, rectPerso2)

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
