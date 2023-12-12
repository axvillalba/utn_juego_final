import pygame
from pygame.locals import *

from models.GUI.GUI_button import *
from models.GUI.GUI_slider import *
from models.GUI.GUI_label import *
from models.GUI.GUI_form import *
from models.GUI.GUI_button_image import *
from auxiliar.constantes import *


class formSonido(Form):
    
    def __init__(self, name, screen: pygame.Surface, x: int, y: int, w:int, h: int, color_background, color_border = "Black", border_size: int = -1, active = True):
    
        super().__init__(name, screen, x,y,w,h,color_background, color_border, border_size, active)

        self.flag_play = True
        
        self.volumen = 0.3
                
        pygame.mixer.init()
        pygame.mixer.music.load(r"assets\sounds\sounds_game\dgm-main_menu.wav")
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)
        
        self.btn_play = Button(self._slave, x, y, 195, 50, 70, 40,
                            "red", "blue",self.btn_play_click, "",
                            "Pause", path_font,15, "white")
        
        
        self.slider_volumen = Slider(self._slave, x, y, 100,120, 200, 10, self.volumen, 
                                    "blue", "white")
    
        porcentaje_volumen = f"{self.volumen * 100}%"
        self.label_volumen = Label(self._slave,315,100, 80, 50, porcentaje_volumen,
                                path_font, 15,"white", "assets/graphics/interfaz/Table.png")
        
        self.bt_exit = Button_Image(self._slave,x,y,20,20,30,30,"assets/graphics/interfaz/close_2.png",self.btn_close, "","","Arial",1,AZUL,AZUL,"Black",-1)
        
        
        
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.bt_exit)
        
    def render(self):
        self._slave.fill(self._color_background)

    def update(self, lista_eventos, delta_ms=0):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)#POLIMORFISMO
                self.update_volumen(lista_eventos)
                
        else:
            self.hijo.update(lista_eventos)
            
    def update_volumen(self, lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label_volumen.update(lista_eventos)
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)
        
        
    
    def btn_play_click(self, param):
        if self.flag_play:
            pygame.mixer.music.pause()
            self.btn_play._color_background = "blue"
            self.btn_play.set_text("Play")
        else:
            
            pygame.mixer.music.unpause()
            self.btn_play._color_background = "red"
            self.btn_play.set_text("Pause")
            
        self.flag_play = not self.flag_play
        
    def btn_close(self, param):
        Form.set_active('menu_principal')
        Form.get_active()
        
        
        
        