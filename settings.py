class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 230, 230)

        self.ship_limit = 3

        
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230, 0, 0)
        self.bullets_allowed = 20

        
        self.fleet_drop_speed = 10
        
        self.speedup_scale = 1.1

        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)

    def initialize_dynamic_settings(self):
        self.ship_speed = 5.0
        self.bullet_speed = 2.5
        self.alien_speed = 5.0

        self.fleet_direction = 1

        self.alien_points = 50