import pygame
from pygame.locals import *
from sys import exit

class Backend:
    def __init__(self):
        pass

    def exec(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                print(mx, my)
                
                if mx > 150 and my > 100 and mx < 255 and my < 180:
                    print('1º')

                if mx > 270 and my > 100 and mx < 370 and my < 180:
                    print('2º')
                
                if mx > 385 and my > 100 and mx < 480 and my < 180:
                    print('3º')
                
                if mx > 150 and my > 200 and mx < 255 and my < 280:
                    print('4º')

                if mx > 270 and my > 200 and mx < 370 and my < 280:
                    print('5º')

                if mx > 385 and my > 200 and mx < 480 and my < 280:
                    print('6º')

                if mx > 150 and my > 292 and mx < 255 and my < 378:
                    print('7º')
                    
                if mx > 270 and my > 292 and mx < 370 and my < 378:
                    0

                if mx > 385 and my > 292 and mx < 480 and my < 378:
                    print('9º')