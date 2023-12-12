import pygame as py
from auxiliar.constantes import *
import math

class Fruta (py.sprite.Sprite):
    
    def __init__(self,pos, stage_dict_configs: dict) -> None:
        super().__init__()
        #me traigo el diccionario de plataforma 
        self.__plataform_configs = stage_dict_configs.get('frutas')
        #cargo la imagen de la plataforma
        self.image = py.image.load(self.__plataform_configs["frutas_img"])
        self.image = py.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect(midbottom=pos)
        

    def update(self, screen: py.surface.Surface):
        self.draw(screen)
    
    def draw(self, screen: py.surface.Surface):
        
        if (DEBUG):
            py.draw.rect(screen,ROJO,self.rect)
        screen.blit(self.image, self.rect)
