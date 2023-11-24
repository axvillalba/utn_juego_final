import pygame as py

class Plataforma (py.sprite.Sprite):
    
    def __init__(self,pos, stage_dict_configs: dict) -> None:
        super().__init__()
        #me traigo el diccionario de plataforma 
        self.__plataform_configs = stage_dict_configs.get('plataforma')
        #cargo la imagen de la plataforma
        self.image = py.image.load(self.__plataform_configs["plataforma_img"]).convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        
        self.plataform_group = py.sprite.Group()
        
    def update(self, screen: py.surface.Surface):
        self.draw(screen)  
    
    def draw(self, screen: py.surface.Surface):
        screen.blit(self.image, self.rect)
        ### limit_x, limit_y,