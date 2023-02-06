from PIL import Image
from player import Player
import pygame
import sys

class World():
    def __init__(self, world_num, screen):
        self.screen = screen
        self.world_num = world_num
        self.BG = pygame.image.load("Assets/Images/"+world_num+"/background.png")
        self.BG = pygame.transform.scale(self.BG, (1131, 700))
        self.floor = pygame.transform.scale(pygame.image.load("Assets/Images/"+world_num+"/floor.png"), (60, 58))
        self.ground = pygame.transform.scale(pygame.image.load("Assets/Images/"+world_num+"/ground.png"), (60, 58))
        self.map = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                    ['0','0','0','0','0','0','0','f','f','f','f','f','0','0','0','0','0','0','0'],
                    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                    ['f','f','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','f','f'],
                    ['g','g','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','g','g'],
                    ['g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
                    ['g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
                    ['g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
                    ['g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
                    ['g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g']]
        self.run_act1()

    def render_map(self):
        tile_rects = []
        y = 0
        for row in self.map:
            x = 0
            for tile in row:
                if tile == 'g':
                    self.screen.blit(self.ground, (x * 60, y * 58))
                if tile == 'f':
                    self.screen.blit(self.floor, (x * 60, y * 58))
                if tile != '0':
                    tile_rects.append(pygame.Rect(x * 60, y * 58, 60, 58))
                x += 1
            y += 1

    def run_act1(self):
        
        pygame.display.set_caption("Not Moo Moo Meadows")
        self.screen = pygame.display.set_mode((1131, 700))
        
        p1 = Player([50,300])

        while True:

            self.screen.blit(self.BG,(0,0))
            self.screen.blit(p1.model, p1.coord)

            self.render_map()
            p1.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                p1.check(event)

            pygame.display.update()
