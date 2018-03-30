import pygame
from pygame.locals import *
from classes import *
from constantes import *
import time
from fonction import * 
from datetime import datetime
import random
pygame.init()

pygame.mixer.music.load('son.mp3')
pygame.mixer.music.play(0)

#Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
fenetre = pygame.display.set_mode((450, 450))

#Titre
pygame.display.set_caption(titre_fenetre)

#BOUCLE PRINCIPALE
continuer = 1

while continuer:

	#score
	score = {}
	nom = input('Votre pseudo : ')
	score[nom] = 1
	print("Bienvenue dans le jeu du labyrinthe", nom)
	for keys, i in score.items() : 
		print("Pseudo : " ,keys + ",score : ", i)
	#Chargement et affichage de l'écran d'accueil
	accueil = pygame.image.load(image_accueil).convert()
	fenetre.blit(accueil, (0,0))

	#Rafraichissement
	pygame.display.flip()

	#On remet ces variables à 1 à chaque tour de boucle
	continuer_jeu = 1
	continuer_accueil = 1

	#BOUCLE D'ACCUEIL
	while continuer_accueil:

		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)


		for event in pygame.event.get():

			#Si l'utilisateur quitte, on met les variables
			#de boucle à 0 pour n'en parcourir aucune et fermer
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:

				continuer_accueil = 0
				continuer_jeu = 0

				continuer = 0
				#Variable de choix du niveau
				choix = 0

			elif event.type == KEYDOWN:
				#Lancement du niveau 1
				if event.key == K_F1:
					continuer_accueil = 0	#On quitte l'accueil
					choix = 'n'+str(random.randint(1,2))		#On définit le niveau à charger
			
	#on vérifie que le joueur a bien fait un choix de niveau
	#pour ne pas charger s'il quitte
	if choix != 0:
		#Chargement du fond
		fond = pygame.image.load(image_fond).convert()
		#Génération d'un niveau à partir d'un fichier
		niveau = Niveau(choix)
		niveau.generer()
		niveau.afficher(fenetre)

		#Création de Donkey Kong
		dk = Perso("images/dk_droite.png","images/dk_gauche.png", "images/dk_haut.png", "images/dk_bas.png", niveau)

	#BOUCLE DE JEU
	while continuer_jeu:
		maintenant = datetime.now()

		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)

		for event in pygame.event.get():

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

		#Affichages aux nouvelles positions
		fenetre.blit(fond, (0,0))
		niveau.afficher(fenetre)
		fenetre.blit(dk.direction, (dk.x, dk.y)) #dk.direction = l'image dans la bonne direction
		pygame.display.flip()

		#Victoire -> Retour à l'accueil
		if niveau.structure[dk.case_y][dk.case_x] == 'a':
			maintenant2 = datetime.now()

			if abs(maintenant2.second - maintenant.second) < 10 : 

				score[nom] +=5
			print(score)
			continuer_jeu = 0

	time.sleep(1)

	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                     
	playAgain = "oui"
	while playAgain == "oui" or playAgain == "o":
	    displayIntro()
	    choice = choosePath()
	    checkPath(choice) 
	    if choice == 'gauche' : 
	        if playAgain == 'oui' :
	            continue
	    choice = chooseriviere()
	    checkriviere(choice)
	    if choice == 'bois' : 
	        if playAgain == 'oui' :
	            continue
	    choice = choosearme()
	    checkarme(choice)
	    if choice == 'couteau' or choice == 'epee' : 
	        if playAgain == 'oui' :
	            continue
	    choice = chooseboss()
	    checkboss(choice)
	    if choice == 'haut' : 
	        if playAgain == 'oui' :
	            continue
	    choice = choosefin()
	    checkfin(choice)
	    if choice == 'coeur' : 
	        if playAgain == 'oui' :
	            continue
	    playAgain = input("Voulez vous rejouer ?(Oui ou o pour rejouer): ")

	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

	continuer_jeu = 1
