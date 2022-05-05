import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 300))
pygame.display.set_caption('Hello Atharva This is First Game!')
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
fontObj = pygame.font.Font('freesansbold.ttf', 32)
#   textSurfaceObj = fontObj.render('Hello Atharva Gaming world!', True, GREEN, BLUE)
textSurfaceObj = fontObj.render(input('Hello Atharva Gaming world! : '), True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (250, 150)
while True: # main game loop
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
