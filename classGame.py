import pygame
import math
     


class Game:
    def __init__(self, screen):
        

        #autre variables
        self.screen = screen
        self.pressed = {pygame.K_LEFT : False,pygame.K_RIGHT : False, pygame.K_UP : False,pygame.K_DOWN : False}
        self.px = self.screen.get_height()/1080


        #background
        self.background=pygame.transform.scale(pygame.image.load("assets/background.png"),(self.screen.get_width(),self.screen.get_height()))
                  
    def update(self):
        """Cette fonction met a jour les evenement divers pouvant avoir lieux"""
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(0,0,self.screen.get_width(), self.screen.get_height()))

        """
        self.screen.blit(self.background,(0,0))
        if self.pressed[pygame.K_LEFT]:
            self.player.left()
        if(self.pressed[pygame.K_RIGHT]):
            self.player.right()
        if(self.pressed[pygame.K_UP]):
            self.player.accelerate()
        if(self.pressed[pygame.K_DOWN]):
            self.player.brake()
        """

        self.screen.blit(self.background, (0,0))
                    