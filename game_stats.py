class GameStats():
    """track the statistic of the game"""

    def __init__(self, ai_settings):
        """initialize the statistic"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # the game is active when it is lanched
        self.game_active = True

    def reset_stats(self):
        """initialize the possible change statistic during running the game """
        self.ships_left = self.ai_settings.ship_limit