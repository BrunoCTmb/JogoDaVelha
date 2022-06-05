import pygame
from pygame.locals import *
from sys import exit
from layout import Lay

class Backend:
    def __init__(self):
        self.lista = [0 for c in range(9)]

    def players(self):
        self.player1 = 'X'
        self.player2 = 'O'
        return self.player1, self.player2

    def exec(self, surf):
        for event  in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                print(mx,my)
                if mx > 150 and my > 100 and mx < 255 and my < 180:
                    print('1º')
                    self.lista[0] = 1
                    
                if mx > 270 and my > 100 and mx < 370 and my < 180:
                    print('2º')
                    self.lista[1] = 1
                    
                if mx > 385 and my > 100 and mx < 480 and my < 180:
                    print('3º')
                    self.lista[2] = 1
                    
                if mx > 150 and my > 200 and mx < 255 and my < 280:
                    print('4º')                    
                    self.lista[3] = 1
                    
                if mx > 270 and my > 200 and mx < 370 and my < 280:
                    print('5º')
                    self.lista[4] = 1
                    
                if mx > 385 and my > 200 and mx < 480 and my < 280:
                    print('6º')
                    self.lista[5] = 1
                    
                if mx > 150 and my > 292 and mx < 255 and my < 378:
                    print('7º')
                    self.lista[6] = 1
                    
                if mx > 270 and my > 292 and mx < 370 and my < 378:
                    print('8º')
                    self.lista[7] = 1
                   
                if mx > 385 and my > 292 and mx < 480 and my < 378:
                    print('9º')
                    self.lista[8] = 1
                    
                print(self.lista)
        
        return self.lista

    def draw_x(self,surf):
        pass

        '''if self.lista[0] == 1:
            p1 = Lay(surf).put(surf,185,95)
        if self.lista[1] == 1:
            p2 = Lay(surf).put(surf,295,95)
        if self.lista[2] == 1:
            p3 = Lay(surf).put(surf,415,95)
        if self.lista[3] == 1:
            p4 = Lay(surf).put(surf,185,195)
        if self.lista[4] == 1:
            p5 = Lay(surf).put(surf,295,195)
        if self.lista[5] == 1:
            p6 = Lay(surf).put(surf,415,195)
        if self.lista[6] == 1:
            p7 = Lay(surf).put(surf,185,295)
        if self.lista[7] == 1:
            p8 = Lay(surf).put(surf,295,295)
        if self.lista[8] == 1:
            p9 = Lay(surf).put(surf,415,295)'''

    def run(self,surface):
        self.exec(surface)
        self.draw_x(surface)
    