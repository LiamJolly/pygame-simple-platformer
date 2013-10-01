import pygame, sys

class Player(object):
	isFalling = 0
	isJumping = 0
	movingLeft = 0
	movingRight = 0

	def __init__(self, image):
		self.playerImage = pygame.image.load(image)
        	self.playerRect = self.playerImage.get_rect()

	def move(self, event):
		if (event.type == pygame.KEYDOWN):
			if event.key == pygame.K_UP:
                		self.isJumping = 1
			if event.key == pygame.K_RIGHT:
                		self.movingRight = 1
                	if event.key == pygame.K_LEFT:
                        	self.movingLeft = 1
		if (event.type == pygame.KEYUP):
			if event.key == pygame.K_RIGHT:
				self.movingRight = 0
			if event.key == pygame.K_LEFT:
				self.movingLeft = 0

	def update(self):
		movement = [0,0]
		if (self.movingLeft == 1):
			movement[0] = -2
		if (self.movingRight == 1):
			movement[0] = 2
		if (self.isJumping == 1):
			movement[1] = -100
			self.isJumping = 0
		if (self.isFalling ==1):
			movement[1] = 2

	        self.playerRect = self.playerRect.move(movement)
