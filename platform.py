import pygame, sys

class Platform(object):
	def __init__(self,image:):
		self.image = pygame.image.load(image)
		self.rect = self.image.get_rect()
