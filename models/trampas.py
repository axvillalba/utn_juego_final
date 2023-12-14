import pygame as py
from auxiliar.constantes import *
import math

class Trampas (py.sprite.Sprite):
    
    def __init__(self,pos, stage_dict_configs: dict) -> None:
        super().__init__()
        #me traigo el diccionario de plataforma 
        self.__trampas_configs = stage_dict_configs.get('trampas')
        #cargo la imagen de la plataforma
        self.image = py.image.load(self.__trampas_configs["trampas_img"])
        self.image = py.transform.scale(self.image, (16, 50))
        self.rect = self.image.get_rect(midbottom=pos)
        

    def movimiento(self):
        self.rect.y += 2
    
    def update(self, screen: py.surface.Surface):    
        self.draw(screen)
    
    def draw(self, screen: py.surface.Surface):
        self.movimiento()

        if (DEBUG):
            py.draw.rect(screen,ROJO,self.rect)
        screen.blit(self.image, self.rect)