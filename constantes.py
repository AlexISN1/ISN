import pygame
from pygame.locals import *

"""Constantes du jeu de Labyrinthe Donkey Kong"""

#Paramètres de la fenêtre
nombre_sprite_cote = 15
taille_sprite = 30

PosX=60
PosY=10
PosX2=200
PosY2=480
dx=5
dy=2
score = 0
scorebis = 1
nbjeu=0


#Personnalisation de la fenêtre
titre_fenetre = "DK Labyrinthe"
image_accueil = "images/pageaccueil.png"
image_mur = "images/arbre-final.png"
image_depart = "images/depart.png"
image_arrivee = "images/arrivee.png"
image_fond = "images/fond1.jpg"