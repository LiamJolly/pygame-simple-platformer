
import sys, pygame

from player import Player

pygame.init()

def main():
	size = width, height = 800, 600
	black = 0, 0, 0

	screen = pygame.display.set_mode(size)
	
	player = Player("images/player.png")
	clock = pygame.time.Clock()

	while 1:
		screen.fill(black)
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			else:
				player.move(event)
		if (player.playerRect.bottom < 500):
			player.isFalling = 1
		else:
			player.isFalling = 0
		
	        player.update()
		screen.blit(player.playerImage, player.playerRect)
	        pygame.display.flip()

if __name__ == '__main__': main()
