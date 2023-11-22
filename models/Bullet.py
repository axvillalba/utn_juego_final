import pygame
from auxiliar.constantes import screen_w

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, direction, img_path = False):
        super().__init__()

        self.__load_img(img_path)
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
        self.direction = direction

    def __load_img(self, img_path: bool):
        if img_path:
            self.image = pygame.image.load('./assets/graphics/player_allen/shoot.png')
        else: 
            self.image = pygame.Surface((4, 20))
            self.image.fill('white')

    def update(self):
        match self.direction:
            case 'left':
                self.rect.x += 4
                if self.rect.x >= screen_w:
                    self.kill()
            case 'right':
                self.rect.x -= 4
                if self.rect.x <= 0:
                    self.kill()