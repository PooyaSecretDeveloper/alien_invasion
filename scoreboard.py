import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_level()
        self.prep_ships()
        self.prep_ccg()

    def prep_score(self):
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

        if rounded_score == 10000:
            self.prep_love()

    
    def prep_ccg(self):
        ccg_str = "Cheshmehkhavar Computer Group"
        self.ccg_image = self.font.render(ccg_str, True, self.text_color, self.settings.bg_color)
        self.ccg_rect = self.ccg_image.get_rect()
        self.ccg_rect.centerx = self.screen_rect.centerx
        self.ccg_rect.top = 20  

    def prep_level(self):
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        self.ships = Group()
        
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.ccg_image, self.ccg_rect)
        self.ships.draw(self.screen)

        if not self.ai_game.game_active:
            self.ai_game.play_button.draw_button()
