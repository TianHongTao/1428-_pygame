class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (192,192,192)
        self.ship_speed_factor = 2
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (240,65,85)
        self.bullets_count = 3
        self.alien_speed = 1
        self.alien_drop = 5
        #  1-> right
        # -1-> left
        self.f_d = 1
        self.a_score = 50
        self.ship_limit = 3

    def b_c_up(self):
        if self.bullets_count <= 15:
            self.bullets_count += 1

    def b_c_down(self):
        if self.bullets_count >= 4:
            self.bullets_count -= 2

    def b_w_up(self):
        if self.bullet_width <= 15:
            self.bullet_width += 5

    def b_w_down(self):
        if self.bullet_width >= 5 :
            self.bullet_width -= 5

    def a_s_down(self):
        """""""""""
        效果仅持续2s
        """""""""""
        if self.alien_speed > 0:
            self.alien_speed -= 1

    def a_s_down(self):
        """""""""""
        效果仅持续2s
        """""""""""
        if self.alien_speed <= 10:
            self.alien_speed += 1

    def a_d_down(self):
        """""""""""
        效果仅持续2s
        """""""""""
        if self.alien_drop > 0:
            self.alien_drop -= 2

        if(self.alien_drop < 0):
            self.alien_drop -= 0

    def a_d_up(self):
        """""""""""
        效果仅持续2s
        """""""""""
        if self.alien_drop <= 15:
            self.alien_drop += 1

    def get_live(self):
        self.ship_limit += 1

    def s_s_up(self):
        if self.ship_speed_factor <= 4:
            self.ship_speed_factor += 1

    def s_s_down(self):
        """""""""""
        效果仅持续2s
        """""""""""
        if self.ship_speed_factor > 0:
            self.ship_speed_factor -= 1

    def all_init(self):
        self.bullets_count = 3
        self.alien_speed = 1
        self.alien_drop = 5
        self.ship_speed_factor = 2
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.ship_limit = 3

    def ship_init(self):
        self.bullets_count = 3
        self.ship_speed_factor = 2
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15