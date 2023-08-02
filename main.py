#Import modules
import pygame
import os
import random

#Initialize pygame
pygame.init()


#Initialize screen
SCREEN_HEIGHT = 600
SCREEN_WIDTH  = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Import Game Images

JUMPING  = [pygame.image.load(os.path.join('Assets/Dino', 'DinoJump.png'))]
RUNNING  = [pygame.image.load(os.path.join('Assets/Dino', 'DinoRun1.png')),pygame.image.load(os.path.join('Assets/Dino', 'DinoRun2.png'))]
DUCKING = [pygame.image.load(os.path.join('Assets/Dino', 'DinoDuck1.png')),pygame.image.load(os.path.join('Assets/Dino', 'DinoDuck2.png'))]
START = [pygame.image.load(os.path.join('Assets/Dino', 'DinoStart.png'))]
DEAD = [pygame.image.load(os.path.join('Assets/Dino', 'DinoDead.png'))]

CLOUD = [pygame.image.load(os.path.join('Assets/Other', 'Cloud.png'))]

GROUND = [pygame.image.load(os.path.join('Assets/Other', 'Track.png'))]

BIG_CACTUS = [pygame.image.load(os.path.join('Assets/Cactus', 'LargeCactus1.png')), pygame.image.load(os.path.join('Assets/Cactus', 'LargeCactus2.png')),pygame.image.load(os.path.join('Assets/Cactus', 'LargeCactus3.png'))]

SMALL_CACTUS = [pygame.image.load(os.path.join('Assets/Cactus', 'SmallCactus1.png')), pygame.image.load(os.path.join('Assets/Cactus', 'SmallCactus2.png')), pygame.image.load(os.path.join('Assets/Cactus', 'SmallCactus3.png'))]

BIRD = [pygame.image.load(os.path.join('Assets/Bird', 'Bird1.png')), pygame.image.load(os.path.join('Assets/Bird', 'Bird2.png'))]

class Dinosaur :
    
    X_pos = 80
    Y_pos = 310
    Y_pos_duck = 340
    Y_jump_vel = 8.5
    
    def __init__ (self) :
        self.duck_img = DUCKING
        self.jump_img = JUMPING
        self.run_img = RUNNING

        self.run = True
        self.duck = False
        self.jump = False

        self.step = 0
        self.y_vel = self.Y_jump_vel
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_pos
        self.dino_rect.y = self.Y_pos

    def update(self, userInput) :
        if self.run :
            self.dino_run()
        if self.duck :
            self.dino_duck()
        if self.jump :
            self.dino_jump()

        if self.step >= 10 :
            self.step = 0

        if userInput[pygame.K_UP] and not self.jump :
            self.run = False
            self.duck = False
            self.jump = True
        elif userInput[pygame.K_DOWN] and not self.duck :
            self.run = False
            self.duck = True
            self.jump = False
        elif not(self.jump or userInput[pygame.K_DOWN]) :
            self.run = True
            self.duck = False
            self.jump = False
    
    def dino_duck(self) :
        self.image = self.duck_img[self.step//5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_pos
        self.dino_rect.y = self.Y_pos_duck
        self.step += 1
 

    def dino_run(self) :
        self.image = self.run_img[self.step//5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_pos
        self.dino_rect.y = self.Y_pos
        self.step += 1

    def dino_jump(self) :
        self.image = self.jump_img[0]
        if self.jump :
            self.dino_rect.y = self.dino_rect.y - (self.y_vel * 4.5)
            self.y_vel = self.y_vel-0.8
        if(self.y_vel< - self.Y_jump_vel) :
            self.dino_rect.y = self.Y_pos
            self.jump = False
            self.y_vel = self.Y_jump_vel

    def show(self, SCREEN) :
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
        
class Cloud :

    X_pos = 400
    Y_pos = 100
    x_vel = 4

    def __init__(self) :
        self.image = CLOUD[0]
        self.image_box = self.image.get_rect()
        self.image_box.x = self.X_pos
        self.image_box.y = self.Y_pos

    def update(self) :
        self.image_box.x = self.image_box.x - (self.x_vel * 3)
        if(self.image_box.x<-100) :
            self.image_box.x = random.randint(1320,1920)

    def show(self, SCREEN) :
        SCREEN.blit(self.image, (self.image_box.x, self.image_box.y))

class Ground :

    X_pos = 0 
    Y_pos = 385
    X_vel = 15

    def __init__(self) :
        self.x_vel = self.X_vel

        self.image1 = GROUND[0]
        self.image_box1 = self.image1.get_rect()
        self.image_box1.x = self.X_pos
        self.image_box1.y = self.Y_pos

        self.image2 = GROUND[0]
        self.image_box2 = self.image2.get_rect()
        self.image_box2.x = self.image1.get_size()[0]
        self.image_box2.y = self.Y_pos

    def update(self) :
        self.image_box1.x -= self.x_vel
        self.image_box2.x -= self.x_vel
        if(self.image_box1.x < -self.image1.get_size()[0]) :
            self.image_box1.x = self.image1.get_size()[0]
        if(self.image_box2.x < -self.image1.get_size()[0]) :
            self.image_box2.x = self.image1.get_size()[0]

    def show(self, SCREEN) :
        SCREEN.blit(self.image1, (self.image_box1.x, self.image_box1.y))
        SCREEN.blit(self.image2, (self.image_box2.x, self.image_box2.y))

def main() :
    run = True
    clock = pygame.time.Clock()
    player  = Dinosaur()
    cloud = Cloud()
    ground = Ground()
    
    while run :
        for event in  pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False
        
        userInput = pygame.key.get_pressed()
        
        SCREEN.fill((255,255,255))

        player.show(SCREEN)
        player.update(userInput)

        cloud.show(SCREEN)
        cloud.update()

        ground.show(SCREEN)
        ground.update()
        
        clock.tick(30)
        pygame.display.update()
    
main()