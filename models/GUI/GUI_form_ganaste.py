import pygame
from pygame.locals import *


from models.GUI.GUI_form import *
from models.GUI.GUI_button_image import *
from auxiliar.constantes import *
from auxiliar.auxiliar_assets import *


class formGanaste(Form):
    
    def __init__(self, name,screen: pygame.Surface, x: int, y: int, w:int, h: int, color_background, color_border = "Black", border_size: int = -1, active = True):
        super().__init__(screen,name, x,y,w,h,color_background, color_border, border_size, active)
        
        self.screen = screen
        # self.volumen = 0.5
        # pygame.mixer.init()
        # pygame.mixer.music.load(audio_final)
        # pygame.mixer.music.set_volume(self.volumen)
        # pygame.mixer.music.play(-1)
        
        
        self.image_bg = pygame.image.load(ganamos)
        self.image_bg = pygame.transform.scale(self.image_bg,(500,300))
                
                
        self.btn_exit = Button_Image(self._slave,x,y,250,400,100,70,table_gui,self.btn_next, "","Seguir",path_font,20,"White",None,"Black",-1)
        self.lista_widgets.append(self.btn_exit)
    
        
        
        
        
    def render(self):
        self._slave.fill(self._color_background)
        self._slave.blit(self.image_bg, self.image_bg.get_rect())
        
    def update(self, lista_eventos,delta_ms=0):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos) #POLIMORFISMO
        else:
            self.hijo.update(lista_eventos)
            
            
    def btn_next(self, param):
        Form.set_active('menu_principal')   
        Form.get_active()
        