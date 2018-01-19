import pygame
from pygame.locals import *
from classes import * 
from constantes import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))



#Rafraîchissement de l'écran
pygame.display.flip()

dk = Perso("personnage/dk_droite.png", "personnage/dk_gauche.png", "personnage/dk_haut.png", "personnage/dk_bas.png")

#BOUCLE INFINIE
continuer = 1
while continuer:

	accueil = pygame.image.load(image_accueil).convert()
	fenetre.blit(accueil,(0,0))
	pygame.display.flip()


	continuer_jeu = 1
	continuer_accueil = 1


	while continuer_accueil : 

		pygame.time.Clock().tick(30)

		for event in pygame.event.get():
		
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				continuer_accueil = 0
				continuer_jeu = 0
				continuer = 0
				#Variable de choix du niveau
			elif event.type == KEYDOWN:				
				#Lancement du niveau 1
				if event.key == K_F1:
					continuer_accueil = 0	#On quitte l'accueil
				#Lancement du niveau 2
				elif event.key == K_F2:
					continuer_accueil = 0
	while continuer_jeu : 
		pygame.time.Clock().tick(30)

		for event in pygame.event.get() : 

			#Si l'utilisateur quitte, on met la variable qui continue le jeu
				#ET la variable générale à 0 pour fermer la fenêtre
			if event.type == QUIT:
					continuer_jeu = 0
					continuer = 0
			
			elif event.type == KEYDOWN:
					#Si l'utilisateur presse Echap ici, on revient seulement au menu
				if event.key == K_ESCAPE:
						continuer_jeu = 0
						
					#Touches de déplacement de Donkey Kong
				elif event.key == K_RIGHT:
						dk.deplacer('droite')
				elif event.key == K_LEFT:
						dk.deplacer('gauche')
				elif event.key == K_UP:
						dk.deplacer('haut')
				elif event.key == K_DOWN:
						dk.deplacer('bas')
		fond = pygame.image.load("images/latest.png").convert()	
		fenetre.blit(fond, (0,0))
		fenetre.blit(dk.direction, (dk.x, dk.y)) #dk.direction = l'image dans la bonne direction
		pygame.display.flip()		
			