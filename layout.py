import pygame

class Lay:
    def __init__(self,surf):
        surf.fill((40,40,40))

    def bg_canvas(self,surf):
        #bg_game = pygame.draw.rect(surf, 'white', (150,100,340,280)) #size - 190
        bg_title = pygame.draw.rect(surf, (30,30,30), (250,25, 140, 50))


    def bg_lines(self,surf):
        l1_y = pygame.draw.line(surf, 'red', (263,100), (263,380), 10)
        l2_y = pygame.draw.line(surf, 'red', (376,100), (376,380), 10)
        
        l1_x = pygame.draw.line(surf, 'red', (150,193), (490,193), 10)
        l2_x = pygame.draw.line(surf, 'red', (150,286), (490,286), 10)
        
    
    def text(self, txt, size, color):
        font = pygame.font.SysFont('arial', size, False, False)
        msg = f'{txt}'
        final_text = font.render(msg, True, color)
        return final_text

    def put(self,surf,pos_x,pos_y):
        one = self.text('X', 80, (200,210,190))
        surf.blit(one, (pos_x,pos_y))

    def run(self,surface):
        self.bg_canvas(surface)
        self.bg_lines(surface)
        #self.put(surface)

