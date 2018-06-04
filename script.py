import pygame
from pygame.locals import *
from classes import *
from constantes import *
import time
from fonction import * 
from datetime import datetime
import random
from tkinter import * 
import sys


perso = ""
#score
score = {}
nom = input('Votre pseudo : ')
score[nom] = 1
print("Bienvenue dans le jeu du labyrinthe", nom)
for keys, i in score.items() : 
	print("Pseudo : " ,keys + ", score : ", i)
menu = Tk()

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

	score[nom] = 0
	
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


		perso = input("Voulez vous être un prince ou DK ? (prince / dk) : ")


		if perso == 'dk' :
			#Création de Donkey Kong
			dk = Perso("images/dk_droite.png","images/dk_gauche.png", "images/dk_haut.png", "images/dk_bas.png", niveau)
		elif perso == 'prince' : 
			dk = Perso("images/DROITEF.png", "images/GAUCHEF.png", "images/HAUTF.png", "images/BASF.png", niveau)

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
			continuer_jeu = 0
			if abs(maintenant2.second - maintenant.second) < 10 : 
				score[nom] +=5


			for keys, i in score.items() : 
				print("Pseudo : " ,keys + ", score : ", i)

			pygame.quit()

			menu.title("[Pong Game]")
			menu.geometry("260x90")

			ButtonJouer = Button(menu, text ="   PLAY   ", command = jouer)
			ButtonJouer.pack(padx = 5, pady = 5)
     
			ButtonQuitter = Button(menu, text ="   Exit    ", command = menu.destroy)
			ButtonQuitter.pack(padx = 5, pady = 5)

			menu.mainloop()


			vie = 100 

			path = ""
			riviere  = ""
			boss = ""
			arme = ""
			banane = ""
			pente = ""
			acheve = ""

			score[nom] += 5 

			for keys, i in score.items() : 
				print("Pseudo : " ,keys + ", score : ", i)

			continuer = 1

			print("Vous venez de recupérer une banane ! ")
			print ("Il semblerait qu'elle se trouve là depuis longtemps")
			print ("Elle ne semble pas tès appétissante, vous décidez de ne pas la manger")
			print ('Et vous continuez votre chemin dans cette jungle hostile')
			print ("En avnçant votre premier adversaire vous bloque le passage")
			print ("C'est un gorille immense qui est prêt à vous asséner un coup")
			print ("Il lève sa main gauche... Fuyez !")

			while continuer : 
				while path != "droite" and path != "gauche" : 
					path = input("Quel chemin allez vous choisir (Droite ou Gauche) : ")
					if path == "gauche" : 
						print("Le singe vous assène un coup")
						print("Vous vous le prenez de plein fouet")
						print("\n")
						vie -= 20
						print("Vie :")
						print(vie)
						print("\n")            
						print("Vous perdez votre esprit et le premier chemin que vous voyez")
						print("vous vous retrouvez alors devant une rivère à courant fort")
					elif path == 'droite' : 
						print("Le singe vous asseme le coup")
						print("Vous arrivez à l'évitez")
						print("Etvous prenez la fuite !")
						print("Deux chemins s'offrent à vous")			
						print("Vous vous retrouvez alors devant une rivère à courant fort")
						print("Mais vous avez aussi la possibilté de poursuivre votre chemin en prenant la pente à côté")
						print("ou sinon prendre la pente")
			            
				while riviere != 'nage' and riviere != 'pied' : 
					riviere = input("Voulez vous traverser à la nage ou prendre la pente raide à pied ? : ")

					if riviere == "nage" : 
						print("Vous mettez les pieds dans l'eau glaciale")
						print("Mais le sol vous dérobent sous vos pieds")
						print("vous êtes à deux doigts de la noyade !")
						print("Votre tête a heurté un caillou")
						print("\n")            
						vie -= 30
						print("Vie :")
						print(vie)
						print("\n")                        
						print("Vous vous réveillez après quelques heures")
						print(" vous êtes face à une grotte lugubre que vous penetrez")
						print("Dans cette grotte vous trouvez une couronne ")
						print("La seule sortie de cette grotte est bloqué par un serpent géant")
						print("Deux options s'offrent à vous :")
						print("1 - Faire diversion avec la banane")
						print("2 - Vous deguisez en roi")
						print("3 - Vous battre contre la bête")

						while arme != '1' and arme != '2' and arme != '3' : 
							arme = input("1, 2 ou 3 : ")

							if arme == '1' : 
								print("Vous lancez la banane ")
								print("Permettant de faire la diversion")
								print("Mais il vous remarque à la dernière minute et vous attrape la jambe !")
								print("\n")                    
								vie -= 20
								print("Vie :")
								print(vie)
								print("\n")                                        
								print("vous vous retrouvez blessé mais vous arivez à fuir")
								print("Vous arrivez à sortir de la grotte")
								print("L'air pur revient dans vos poumons !")
								print("Maintenant votre but premier est de trouver la sortie de cette maudite jungle")
								print("Mais vous manquez de force...")
								print("Allez vous prendre le rique de manger votre banane?")
			                    
								while banane != 'manger' and banane != 'jeter' : 
									banane = input("manger ou jeter : ")

									if banane == 'manger' : 
										print("Vous enlevez la peau de la banane")
										print("Il setrouve que malgre cette couleur noirâtre...")
										print("La banane a un excellent goût et vous redonne des forces !")
										print("\n")                            
										vie += 10
										print("Vie :")
										print(vie)
										print("\n")                                                        
										print("Apres ce petit encas, vous reprenez votre marche")
										print("Vous voyez enfin le fin de ce calvaire : La sortie de la jungle")
										print("Mais il semblerait que quelqu'un vous y attende")
										print("C'est le gorille qui a essayé de vous tuer tout à l'heure")
										print("Le moment de vérité est arrivé... Battez-le !")                            

									elif banane == 'jeter' : 
										print("Vous décidez de ne pas manger cette banane ne vous servant pas à grand chose...")
										print("Mais bon vos douleurs vous font encore mals...")
										print("\n")                                                        
										vie -= 10
										print("Vie :")
										print(vie)
										print("\n")                                                        
										print("Mais bon il faut faire avec et vous reprenez votre marche")
										print("Vous voyez enfin le fin de ce calvaire : La sortie de la jungle")
										print("Mais il semblerait que quelqu'un vous y attende")
										print("C'est le gorille qui a essayé de vous tuer tout à l'heure")         
										print("Le moment de vérité est arrivé... Battez-le !")
			                            
							elif arme == '2' : 
								print("Vous mettez la couronne sur votre tête")
								print("On pourrait vous confondre pour un roi !")
								print("Vous passez devant le singe")
								print("Votre ruse était de rigueur !")
								print("Le serpent n'y voit que du feu et ne peut que s'incliner devant un roi !")
								print("Vous pouvez alors sortir de la grotte sans encombre")			     
								print("L'air pur revient dans vos poumons !")
								print("Maintenant votre but premier est de trouver la sortie de cette maudite jungle")
								print("Mais vous manquez de force...")
								print("Allez vous prendre le rique de manger votre banane?")
			                    
								while banane != 'manger' and banane != 'jeter' : 
									banane = input("manger ou jeter : ")

									if banane == 'manger' : 
										print("Vous enlevez la peau de la banane")
										print("Il setrouve que malgre cette couleur noirâtre...")
										print("La banane a un excellent goût et vous redonne des forces !")
										print("\n")                            
										vie += 10
										print("Vie :")
										print(vie)
										print("\n")                                                        
										print("Apres ce petit encas, vous reprenez votre marche")
										print("Vous voyez enfin le fin de ce calvaire : La sortie de la jungle")
										print("Mais il semblerait que quelqu'un vous y attende")
										print("C'est le gorille qui a essayé de vous tuer tout à l'heure")
										print("Le moment de vérité est arrivé... Battez-le !")                            

									elif banane == 'jeter' : 
										print("Vous décidez de ne pas manger cette banane ne vous servant pas à grand chose...")
										print("Mais bon vos douleurs vous font encore mals...")
										print("\n")                            
										vie -= 10
										print("Vie :")
										print(vie)
										print("\n")                                                        
										print("Mais bon il faut faire avec et vous reprenez votre marche")
										print("Vous voyez enfin le fin de ce calvaire : La sortie de la jungle")
										print("Mais il semblerait que quelqu'un vous y attende")
										print("C'est le gorille qui a essayé de vous tuer tout à l'heure")         
										print("Le moment de vérité est arrivé... Battez-le !")                             
			                    
							elif arme == '3' : 
								print("Il faudrait être un fou pour attaquer ce serpent !")
								print("Mais bon... Il semblerait que vous aimiez les risques...")
								print("Vous decidez de penser à une manière de l'apporcher")
								print("Analysez la situation...")
								print("Et attaquez !!")
								print("Mais en un coup de queu le serpent vous rappelle qui a le dessus")
								print("\n")                                        
								vie -= 40
								print("Vie :")
								print(vie)
								print("\n")                                                            
								print("Etourdi vous sortez de la grotte")
								print("L'air pur revient dans vos poumons !")
								print("Maintenant votre but premier est de trouver la sortie de cette maudite jungle")
								print("Mais vous manquez de force...")
								print("Allez vous prendre le rique de manger votre banane?")
			                
								while banane != 'manger' and banane != 'jeter' : 
									banane = input("manger ou jeter : ")

									if banane == 'manger' : 
										print("Vous enlevez la peau de la banane")
										print("Il setrouve que malgre cette couleur noirâtre...")
										print("La banane a un excellent goût et vous redonne des forces !")
										print("\n")                            
										vie += 10
										print("Vie :")
										print(vie)
										print("\n")                                                        
										print("Apres ce petit encas, vous reprenez votre marche")
										print("Vous voyez enfin le fin de ce calvaire : La sortie de la jungle")
										print("Mais il semblerait que quelqu'un vous y attende")
										print("C'est le gorille qui a essayé de vous tuer tout à l'heure")
										print("Le moment de vérité est arrivé... Battez-le !")                            

									elif banane == 'jeter' : 
										print("Vous décidez de ne pas manger cette banane ne vous servant pas à grand chose...")
										print("Mais bon vos douleurs vous font encore mals...")
										print("\n")                                                        
										vie -= 10
										print("Vie :")
										print(vie)
										print("\n")                                                          
										print("Mais bon il faut faire avec et vous reprenez votre marche")
										print("Vous voyez enfin le fin de ce calvaire : La sortie de la jungle")
										print("Mais il semblerait que quelqu'un vous y attende")
										print("C'est le gorille qui a essayé de vous tuer tout à l'heure")         
										print("Le moment de vérité est arrivé... Battez-le !")                            


					elif riviere == "pied" : 
						print("Vous descendez la pente")
						print("Elle ne semble pas si dangereuse...")
						print("Mais à ce moment vous vous prenez les pieds dans une racine vous faisant déballer la pente !")
						print("Votre corps se retrouve sans dessus-dessous")
						print("\n")
						vie -= 30
						print("Vie :")
						print(vie)
						print("\n")            
						print("Vous vous relevez")
						print("Et avancez tant bien que mal jusqu'à un arbre où vous décidez de vous reposez à l'ombre")
						print("Vous êtes exténué, voulez vous prendre le risque de rester sous cette arbre ou continuez de marcher ?")
						
						while pente != 'rester' and pente != 'partir' : 
								pente = input("Voulez vous restez ou partir ? (rester ou partir)")

								if pente == 'rester' : 
									print("Un peu de repos ne devrait pas faire de mal...")
									print("Mais c'est dans un jungle sauvage que vous essayez de vous reposer !")
									print("Des fourmis rouges, cachées sous l'arbre, sont prêt à vous dévorer !")
									print("\n")                        
									vie -= 20
									print("Vie :")                        
									print(vie)
									print("\n")                                                
									print("Pas de repos ! Vous fuyez de cet endroit maudit")
									print("Vous voyez enfin le fin de ce calvaire : La sortie de la jungle")
									print("Mais il semblerait que quelqu'un vous y attende...")
									print("C'est le gorille qui a essayé de vous tuer tout à l'heure !")
									print("Le moment de vérité est arrivé... Battez-le !")
			                
								elif pente == 'partir': 
									print("Rester dans une jungle si dangereuse quelques secondes sans rien faire pourrait vous coûter la vie...")
									print("Vous prenez vos dernières forces et décidez de quitter cette jungle une bonne fois pour toute..." )    
									print("Vous voyez enfin le fin de ce calvaire : La sortie de la jungle")
									print("Mais il semblerait que quelqu'un vous y attende...")
									print("C'est le gorille qui a essayé de vous tuer tout à l'heure !")
									print("Le moment de vérité est arrivé... Battez-le !")
			                
			                
					while boss != 'haut' and boss!= 'bas' : 
						boss =  input("Comment voulez vous attaquez ? Par le haut ou le bas ? (haut ou bas) : ")

						if boss == 'haut' : 
							print("Vous decidez de l'attaquer directement à la tête")
							print("Cela désequilibre le singe mais malgré tout il arrive à vous asséner un coup! ")
							print("\n")                
							vie -= 30
							print("Vie :")
							print(vie)
							print("\n")                                
							print("Le moment final est arrivé... Vous devez l'achever !")
						
						elif boss == 'bas' : 
							print('VOus decidez de lui placer un coup bien placé entre les deux jambes...')
							print("Ce coup ... 'bas' fait perdre les moyens au gorille ne sachant comment rétorquer")
							print("LE moment final est arrivé... Vous devez l'achever !")
			             
					while acheve != 'coeur' and acheve!= 'tete' : 
						acheve =  input("Comment allez vous l'achever ? En lui donnant un dernier coup au coeur ou bien reessayez la tête ? (coeur ou tete) : ")

						if acheve == 'coeur' : 
							print("C'est l'endroit le plus sensible de n'importe quelle personne")
							print("D'un dernier coup vous touchez le singe en plein coeur !")
							print(vie)
							print("Le combat est fini, vous avez gagné et pouvait sortir de la jungle !")
						
						elif acheve == 'tete' : 
							print('Une tête aussi dur est difficilement brisable...')
							print("Vous lui donnez ce dernier coup mais avant de perdre ses esprits, il vous assème un coup")
							print("\n")                                
							vie -= 40
							print("Vie :")                
							print(vie)
							print("\n")                                
							print("Le combat est fini, vous avez gagné et pouvait sortir de la jungle !")

					score[nom] += 5


					

					for keys, i in score.items() : 
						print("Bravo" ,keys + " vous finissez le parcours avec un score de : ", i)

					print("En espérant vous revoir bientôt !! ")

					continuer_jeu = 0 
					continuer_accueil = 0 
					continuer = 0
			                
			                
			                


						

				

