class GameState():
    def __init__(self,a_s):
        self.a_s = a_s
        self.score = 0
        self.game_active = False
        self.reset_state()

    def reset_state(self):
        self.ships_left = self.a_s.ship_limit
        self.score = 0