import pygame
from auxiliar.constantes import * 



class Barra_vida(pygame.sprite.Sprite):
    def __init__(self, vida_maxima, ancho,largo) :
        super().__init__()
    
        self.vida_momento = self.vida
        self.vida_maxima = vida_maxima
        self.ancho = ancho
        self.largo = largo
        self.image = pygame.Surface((self.ancho, self.largo))
        self.rect = self.image.get_rect()


    def update(self):
        
        self.rect.width = int((self.vida_momento / self.vida_maxima) * self.ancho)
        if self.vida_momento > self.vida_maxima / 2:
            self.image.fill(VERDE)
        elif self.vida_momento > self.vida_maxima / 4:
            self.image.fill(AMARILLO)
        else:
            self.image.fill(ROJO)
            
        self.draw()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
