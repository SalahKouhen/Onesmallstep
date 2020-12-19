import pygame

pygame.init()

white = (255,255,255)

display_width = 800
dispaly_height = 600
gameDispaly = pygame.display.set_mode((display_width,dispaly_height))
pygame.display.set_caption("One small step")
clock = pygame.time.Clock()

stickman = pygame.image.load()

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True       
        print(event)

    pygame.display.flip
    clock.tick(60)

pygame.quit()
quit()
