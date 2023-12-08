import pygame
import random as rd
from models.Bullet import Bullet
from auxiliar.constantes import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, constraint_x, constraint_y, stage_dict_configs: dict):
        super().__init__()
        #Abrimos el archivo json y lo convertimos en diccionario 
        self.__enemy_configs = stage_dict_configs.get('enemy')
        #Mostrar sprite del jugador
        self.image = pygame.image.load(self.__enemy_configs["enemy_img"]).convert_alpha()
        #En este caso lo que hago es darle el rectangulo al sprite de la linea anterior. ahora self.rect tendrá los metodos de rectangulos. 
        self.rect = self.image.get_rect(midbottom=pos)

        # Atributos de movimiento
        self.__setear_velocidad()
        self.max_x_constraint = constraint_x
        self.max_y_constraint = constraint_y
        self.frame_rate = 120
        self.time_move = 0
        self.move_right = True

    def constraint(self):  # Ajusta al jugador a los limites de la pantalla
        if self.move_right:
            if (self.rect.right + self.speed ) < self.max_x_constraint:
                self.rect.x += self.speed
            else:
                if self.rect.bottom + self.speed * 2 < self.max_y_constraint:
                    self.rect.y += self.speed * 2
                self.move_right = False
        else:
            if self.rect.left - self.speed > 0:
                self.rect.x -= self.speed
            else:
                if (self.rect.bottom + self.speed * 2) < self.max_y_constraint:
                    self.rect.y += self.speed * 2
                self.move_right = True
    
    #Seteo una velocidad aleatoria a los enemigos
    def __setear_velocidad(self):
        self.speed = rd.randint(self.__enemy_configs["min_enemy_speed"], self.__enemy_configs["max_enemy_speed"])

    def do_movement(self, delta_ms):
        self.time_move += delta_ms
        if self.time_move >= self.frame_rate:
            self.constraint()

    def update(self, delta_ms, screen: pygame.surface.Surface):
        self.do_movement(delta_ms)
        self.draw(screen)
        self.constraint()
    
    def draw(self, screen: pygame.surface.Surface):
        if (DEBUG):
            pygame.draw.rect(screen,AMARILLO,self.rect)

        screen.blit(self.image, self.rect)