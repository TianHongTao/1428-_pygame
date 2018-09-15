import pygame.ftfont
import pygame.sysfont

class Scoreboard():

    def __init__(self,a_s,screen,stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.a_s = a_s
        self.stats = stats
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None,48)

        self.prep_score()

    def prep_score(self):
        c = int(self.stats.score)
        score_str = "{:,}".format(c)
        self.score_image = self.font.render(score_str, True, self.text_color, self.a_s.bg_color)

        self.rect = self.score_image.get_rect()
        self.rect.right = self.screen_rect.right - 20
        self.rect.top = 20

    def show(self):
        self.screen.blit(self.score_image, self.rect)