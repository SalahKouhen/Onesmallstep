import pygame

pygame.init()

white = (255,255,255)

display_width = 800
dispaly_height = 600
gameDispaly = pygame.display.set_mode((display_width,dispaly_height))
pygame.display.set_caption("One small step")
clock = pygame.time.Clock()

stickmanimg = pygame.image.load("stickMan.png")

def stickman(x,y):
    gameDispaly.blit(stickmanimg,(x,y))

x =  (display_width * 0.45)
y = (display_height * 0.8)

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True       
        print(event)

    gameDispaly.fill(white)
    stickman(x,y)

    pygame.display.flip
    clock.tick(60)

pygame.quit()
quit()
