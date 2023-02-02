from PIL import Image
from player import Player
import pygame
import sys

class World():
    def __init__(self, world_num, screen):
        self.world_num = world_num
        self.BG = pygame.image.load("Assets/Images/"+world_num+"/background.png")
        self.BG = pygame.transform.scale(self.BG, (1131, 707))
        # img = Image.open("Assets/Images/Backgrounds/"+world_num+".jpg")
        # self.width, self.height = img.size
        self.run_act1(screen)

    def run_act1(self,screen):
        
        pygame.display.set_caption("City Nightfall")
        screen = pygame.display.set_mode((1131, 707))
        
        p1 = Player([50,300])

        while True:

            screen.blit(self.BG,(0,0))
            screen.blit(p1.model, p1.coord)

            p1.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                p1.check(event)


            pygame.display.update()
