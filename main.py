
import sys, pygame

pygame.init()

def main():
	size = width, height = 800, 600
	black = 0, 0, 0

	screen = pygame.display.set_mode(size)

	ball = pygame.image.load("images/ball.bmp")
	ballrect = ball.get_rect()
	clock = pygame.time.Clock()

	while 1:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			elif event.type == pygame.KEYDOWN :
				if event.key == pygame.K_UP:
					ballrect = ballrect.move(0,-2)
				if event.key == pygame.K_DOWN:
					ballrect = ballrect.move(0,2)
				if event.key == pygame.K_RIGHT:
					ballrect = ballrect.move(2,0)
				if event.key == pygame.K_LEFT:
					ballrect = ballrect.move(-2,0)
     
        	screen.fill(black)
	        screen.blit(ball, ballrect)
	        pygame.display.flip()

if __name__ == '__main__': main()
