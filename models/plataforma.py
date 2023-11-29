import pygame as py
from auxiliar.constantes import *

class Plataforma (py.sprite.Sprite):
    
    def __init__(self,pos, stage_dict_configs: dict) -> None:
        super().__init__()
        #me traigo el diccionario de plataforma 
        self.__plataform_configs = stage_dict_configs.get('plataforma')
        #cargo la imagen de la plataforma
        self.image = py.image.load(self.__plataform_configs["plataforma_img"]).convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        self.plataform_group = py.sprite.Group()
        
        self.rect_ground_collition_top = py.Rect(self.rect.x, self.rect.y, self.rect.w, altura_rect)
        self.rect_ground_collition_bottom = py.Rect(self.rect.x, self.rect.y + self.rect.h - altura_rect, self.rect.w, altura_rect)
        
    def update(self, screen: py.surface.Surface):
        
        self.draw(screen)  
    
    def draw(self, screen: py.surface.Surface):
        if (DEBUG):
            py.draw.rect(screen,ROJO,self.rect)
            
        screen.blit(self.image, self.rect)
        
        if (DEBUG):
            py.draw.rect(screen,VERDE,self.rect_ground_collition_top)
            py.draw.rect(screen,VERDE,self.rect_ground_collition_bottom)