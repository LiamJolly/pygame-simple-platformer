import pygame, sys

class Player(object):
	
	movement = [0,0]

	def __init__(self, image):
		self.playerImage = pygame.image.load(image)
        	self.playerRect = self.playerImage.get_rect()

	def printargs(self):
		print self.playerImage
		print self.playerRect
	
	def move(self, event):
		if (event.type == pygame.KEYDOWN):
			if event.key == pygame.K_UP:
                		self.movement[1] -=1
               	 	if event.key == pygame.K_DOWN:
                		self.movement[1] +=1
                	if event.key == pygame.K_RIGHT:
                		self.movement[0] +=1
                	if event.key == pygame.K_LEFT:
                        	self.movement[0] -=1
		elif (event.type == pygame.KEYUP):
                        if event.key == pygame.K_UP:
                                self.movement[1] +=1
                        if event.key == pygame.K_DOWN:
                                self.movement[1] -=1
                        if event.key == pygame.K_RIGHT:
                                self.movement[0] -=1
                        if event.key == pygame.K_LEFT:
                                self.movement[0] +=1

	def update(self):
	        self.playerRect = self.playerRect.move(self.movement)
