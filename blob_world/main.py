import pygame

WIDTH = 800
HEIGHT = 600

WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (255,0,0)
GREEN = (0,255,0)
BLUE  = (0,0,255)

game_display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Blob World')
clock = pygame.time.Clock()

def draw_environment():
    game_display.fill(BLACK)
    pygame.display.update()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_environment()
        clock.tick(60)

if __name__=='__main__':
    main()
