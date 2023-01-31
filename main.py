import pygame
import sys
from pygame import mixer
from button import Button

pygame.init()

class Menu():
    def __init__(self) -> None:
        self.SCREEN = pygame.display.set_mode((1131, 707))
        pygame.display.set_caption("Menu")
        self.BG = pygame.image.load("Assets/Images/main_menu.jpg")

    def get_font(self,size):
        return pygame.font.Font("Assets/Font/Sonic Advanced 2.ttf", size)

    def world_select(self):

        pygame.display.set_caption("World Select")

        while True:

            MOUSE_POS = pygame.mouse.get_pos()

            self.SCREEN.fill("black")
            self.SCREEN.blit(self.BG, (0,0))

            MENU_TEXT = self.get_font(100).render("SELECT WORLD", True, "#1b368d")
            MENU_RECT = MENU_TEXT.get_rect(center=(837, 35))

            buttons = []

            y_pos = 175
            x_pos = 700

            for x in range (8):
                buttons.append(Button(image=pygame.image.load("Assets/Buttons/PNG/CGB02-blue_M_btn.png"), pos=(x_pos, y_pos), 
                                        text_input="W"+str(x+1), font=self.get_font(75), base_color="#d7fcd4", hovering_color="White"))
                
                buttons[x].changeColor(MOUSE_POS)
                buttons[x].update(self.SCREEN)

                if x%2 == 0:
                    x_pos += 275
                else:
                    x_pos -= 275
                    y_pos += 150

            self.SCREEN.blit(MENU_TEXT, MENU_RECT)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    def options(self):
        pass

    def main_menu(self):

        clock = pygame.time.Clock() 

        mixer.init()

        mixer.music.load('Assets/Music/Menu-Theme.mp3')

        mixer.music.set_volume(0.2)

        mixer.music.play()

        while True:
            self.SCREEN.blit(self.BG, (0,0))

            MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = self.get_font(100).render("Flash Sonic Reborn", True, "#1b368d")
            MENU_RECT = MENU_TEXT.get_rect(center=(750, 35))

            PLAY_BUTTON = Button(image=pygame.image.load("Assets/Buttons/PNG/CGB02-blue_L_btn.png"), pos=(775, 175), 
                                    text_input="PLAY", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            OPTIONS_BUTTON = Button(image=pygame.image.load("Assets/Buttons/PNG/CGB02-blue_L_btn.png"), pos=(775, 350), 
                                text_input="OPTIONS", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load("Assets/Buttons/PNG/CGB02-blue_L_btn.png"), pos=(775, 525), 
                                text_input="QUIT", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")

            self.SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.changeColor(MOUSE_POS)
                button.update(self.SCREEN)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MOUSE_POS):
                        self.world_select()
                    if OPTIONS_BUTTON.checkForInput(MOUSE_POS):
                        self.options()
                    if QUIT_BUTTON.checkForInput(MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            clock.tick(60)

            pygame.display.update()


if __name__ == "__main__":
    game = Menu()
    game.main_menu()
    