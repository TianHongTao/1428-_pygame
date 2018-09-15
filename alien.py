import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, a_s, screen,image):
        super().__init__()
        self.screen = screen
        self.a_s = a_s

        self.image = image
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += (self.a_s.alien_speed * self.a_s.f_d)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left < 0:
            return True
        else:
            return False


class A_1(Alien):

    def __init__(self, a_s, screen):
        self.image = pygame.image.load('images/3.bmp')
        Alien.__init__(self, a_s, screen,self.image)


class A_2(Alien):
    def __init__(self, a_s, screen):
        self.image = pygame.image.load('images/4.bmp')
        Alien.__init__(self,a_s,screen,self.image)
