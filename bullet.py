import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self,a_s,screen,ship):
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0,0,a_s.bullet_width,a_s.bullet_height)
        self.rect.centerx = ship.rect.centerx
        #self.rect.centerxy = ship.rect.centery
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = a_s.bullet_color
        self.speed = a_s.bullet_speed
    def update(self):
        self.y = self.y - self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)