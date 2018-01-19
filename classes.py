import pygame 
from pygame.locals import * 
from constantes import *
"""Classes du jeu de Labyrinthe Donkey Kong"""


			
			
class Perso:
	"""Classe permettant de créer un personnage"""
	def __init__(self, droite, gauche, haut, bas):
		#Sprites du personnage
		self.droite = pygame.image.load(droite).convert_alpha()
		self.gauche = pygame.image.load(gauche).convert_alpha()
		self.haut = pygame.image.load(haut).convert_alpha()
		self.bas = pygame.image.load(bas).convert_alpha()
		#Position du personnage en cases et en pixels
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0
		#Direction par défaut
		self.direction = self.droite
	
	
	
	def deplacer(self, direction):
		
		if direction == 'droite':
		
			self.direction = self.droite
		
		if direction == 'gauche':
			if self.case_x > 0:
					self.case_x -= 1
					self.x = self.case_x * taille_sprite
			self.direction = self.gauche
		
		if direction == 'haut':
				
			self.direction = self.haut
		
		if direction == 'bas':
			if self.case_y < (nombre_sprite_cote - 1):
				
					self.case_y += 1
					self.y = self.case_y * taille_sprite
			self.direction = self.bas

