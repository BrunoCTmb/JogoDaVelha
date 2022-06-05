import pygame 
from pygame.locals import *
from sys import exit 
from layout import Lay
from backend import Backend
from draw import Draw

pygame.init()

width = 640
height = 480
screen = pygame.display.set_mode((width, height))
game_title = pygame.display.set_caption('Jogo da velha')

layout = Lay(screen)
back = Backend()
draw = Draw()


#print(back.exec(screen))

while True:
    
    
    layout.run(screen)
    
    title = layout.text('Jogo da velha', 20, 'lightblue')
    screen.blit(title, (270,35))
    
    back.run(screen)
    #draw.draw_x(screen)

    pygame.display.flip()
