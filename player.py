import pygame

class Player():
    def __init__(self, coordinate):
        self.model = pygame.image.load("Assets/Images/P1/R-L-1.png")
        self.model = pygame.transform.scale(self.model, (70,100))
        self.move_r = False
        self.move_l = False
        self.coord = coordinate
        self.momentum = 0
        self.hitbox = pygame.Rect(self.coord[0],self.coord[1],70,100)

    def update(self):

        # if not(self.move_r or self.move_l):
        #     self.momentum = 0
        
        # if self.move_r:
        #     self.momentum += 0.005
        #     move = 0.1 + self.momentum
        #     if move >= 3:
        #         move = 3
        #     self.coord[0] += move
        # if self.move_l:
        #     self.momentum -= 0.005
        #     move = -0.1 - self.momentum
        #     if move >= 3:
        #         move = 3
        #     self.coord[0] -= move
        #     print(self.coord[0])

        # if not (self.move_r or self.move_l):
        #     self.momentum *= 0.9  # reduce momentum when not moving
        #     self.momentum = max(0, self.momentum)  # ensure momentum is positive

        # if self.move_r:
        #     self.momentum += 0.01 + (self.momentum * 0.05)  # increase momentum gradually
        #     self.momentum = min(self.momentum, 2)  # limit maximum momentum
        #     move = 0.1 + self.momentum
        #     self.coord[0] += move
        # if self.move_l:
        #     self.momentum -= 0.01 + (self.momentum * 0.05)  # decrease momentum gradually
        #     self.momentum = max(-2, self.momentum)  # limit maximum momentum
        #     move = -0.1 - self.momentum
        #     self.coord[0] -= move

        if not (self.move_r or self.move_l):
            self.momentum *= 0.9  # reduce momentum when not moving
            self.momentum = max(0, self.momentum)  # ensure momentum is positive

        if self.move_r:
            self.momentum += 0.01
            self.momentum = min(self.momentum, 2)  # limit maximum momentum
            move = 0.1 + self.momentum
            self.coord[0] += move
        if self.move_l:
            self.momentum -= 0.01
            self.momentum = max(-2, self.momentum)  # limit maximum momentum
            move = -0.1 - self.momentum
            self.coord[0] -= move
    
    def check(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.move_l = True
            if event.key == pygame.K_d:
                self.move_r = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.move_l = False
            if event.key == pygame.K_d:
                self.move_r = False