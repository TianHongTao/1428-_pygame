import pygame


class Ship():
    def __init__(self, a_s, screen):
        self.screen = screen
        self.a_s = a_s

        self.image = pygame.image.load('images/2.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.height = self.rect.height
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom

        self.centerx1 = float(self.screen_rect.centerx)
        self.centery2 = float(self.screen_rect.bottom)
        self.moving_right = False
        self.moving_left = False
        self.moving_front = False
        self.moving_back = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx1 += self.a_s.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.centerx1 -= self.a_s.ship_speed_factor

        if self.moving_front:
            self.centery2 -= self.a_s.ship_speed_factor
            if self.rect.centery < self.screen_rect.top:
                self.centery2 = self.screen_rect.bottom

        if self.moving_back:
            self.centery2 += self.a_s.ship_speed_factor
            if self.rect.centery > self.screen_rect.bottom:
                self.centery2 = self.screen_rect.top

        self.rect.centerx = self.centerx1
        self.rect.centery = self.centery2

    def center_ship(self):
        self.centerx1 = float(self.screen_rect.centerx)
        self.centery2 = float(self.screen_rect.bottom)

