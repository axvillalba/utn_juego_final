import pygame
import random as rd
from models.Bullet import Bullet
from auxiliar.constantes import *
from auxiliar.auxiliar import SurfaceManager as sf

class Timcanpy(pygame.sprite.Sprite):
    def __init__(self, pos,stage_dict_configs: dict):
        super().__init__()
        #Abrimos el archivo json y lo convertimos en diccionario 
        self.__timcanpy_configs = stage_dict_configs.get('player')
        #Mostrar sprite del jugador

        self.__iddle_l = sf.get_surface_from_spritesheet(self.__timcanpy_configs.get('timcanpy_img'),4,1, flip=True)      

        self.__actual_frame_index = 0
        self.__timcanpy_animation_time = 0

        self.__actual_animation = self.__iddle_l
        self.__actual_img_animation = self.__actual_animation[self.__actual_frame_index]

        self.rect = self.__actual_img_animation.get_rect(midbottom=(pos))
        self.rect_ground_collition_floor = pygame.Rect(self.rect.x, self.rect.y + self.rect.h - altura_rect, self.rect.w, altura_rect)
        self.rect_ground_collition_top = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, altura_rect)

        # Atributos de movimiento
        self.move = 2.5
        self.frame_rate = 120
        self.time_move = 0



    def set_x_animations_preset (self,animation_list: list[pygame.surface.Surface], look_r: bool):
        self.__actual_animation = animation_list
        self.move_right = look_r
        
        
    def do_animation(self, delta_ms):
        self.__timcanpy_animation_time += delta_ms
        if self.__timcanpy_animation_time >= self.frame_rate:
            self.__timcanpy_animation_time = 0
            if self.__actual_frame_index < len(self.__actual_animation) - 1:
                self.__actual_frame_index += 1
            else:
                self.__actual_frame_index = 0

    def update(self,screen: pygame.surface.Surface, delta_ms):
        #self.do_movement(delta_ms)
        self.do_animation(delta_ms)
        self.draw(screen)
    
    def draw(self, screen: pygame.surface.Surface):
        if (DEBUG):
            pygame.draw.rect(screen,AMARILLO,self.rect)
        self.__actual_img_animation = self.__actual_animation[self.__actual_frame_index]
        screen.blit(self.__actual_img_animation, self.rect)