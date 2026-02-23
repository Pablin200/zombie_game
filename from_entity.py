#------------COIN CLASS------------
class Coin:
    def __init__(self, enemy):
        self.sprite = config.COIN_IMAGE
        self.rect = self.sprite.get_rect()
        self.rect.center = enemy.rect.center

    #------COIN DRAW FUNCTION------
    def draw(self, target_surface):
        target_surface.blit(self.sprite, self.rect)
#------------COIN CLASS------------
