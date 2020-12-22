import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("One small step")
clock = pygame.time.Clock()

stickmanimg = pygame.image.load('stickMan.png')
smwidth = 83
smheight = 126

def block(x,y,width,height,colour):
    pygame.draw.rect(gameDisplay,colour, [x,y,width,height])

def stickman(x,y):
    gameDisplay.blit(stickmanimg,(x,y))

def text_objects(text, font, colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()

def displayText(text, fontsize, colour):
    ourFont = pygame.font.Font('freesansbold.ttf',fontsize)
    TextSurf, TextRect = text_objects(text, ourFont, colour)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    gameloop()

def gameOverScreen():
    gameDisplay.fill(black)
    displayText("YOU DIED", 130, red)

def gameloop():
    x =  (display_width * 0.45)
    y = (display_height * 0.8)

    xchange = 0

    runningspeed = 7

    blockstarty = -600
    blockstartx = random.randrange(0,display_height)
    blockwidth = 100
    blockheight = 100

    gameExit = False
    gameOver = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #gameExit = True
                pygame.quit()
                quit()  

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xchange = -5
                elif event.key == pygame.K_RIGHT:
                    xchange = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xchange = 0            
            #print(event)

        x += xchange

        gameDisplay.fill(white)

        block(blockstartx,blockstarty,blockwidth,blockheight,black)
        blockstarty += runningspeed
        stickman(x,y)

        pygame.display.flip()
        clock.tick(60)

        if x < 0 or x > display_width - smwidth:
            gameOver = True

        if blockstarty > display_height:
            blockstarty = 0 - blockheight
            blockstartx = random.randrange(0,display_width)

        if gameOver == True:
            gameOverScreen()

gameloop()
pygame.quit()
quit()
