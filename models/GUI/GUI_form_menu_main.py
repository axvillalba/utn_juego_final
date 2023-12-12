import pygame
from pygame.locals import *

from models.GUI.GUI_button import *
from models.GUI.GUI_label import *
from models.GUI.GUI_form import *
from models.GUI.GUI_button_image import *
from auxiliar.constantes import *



class formMainMenu(Form):
    
    def __init__(self, name,screen: pygame.Surface, x: int, y: int, w:int, h: int, color_background, color_border = "Black", border_size: int = -1, active = True):
        super().__init__(screen,name, x,y,w,h,color_background, color_border, border_size, active)
        
        self.flag_play = True
        self.stage = None
        
        self.btn_play_start = Button(self._slave, x, y, 210, 25, 100, 40,
                            "red", "blue",self.btn_play_click1, "",
                            path_font, path_font,20, "white")
        
        self.btn_play_config = Button(self._slave, x, y, 210, 85, 100, 40,
                            "red", "blue",self.btn_play_click2, "",
                            path_font, path_font,20, "white")
        
        self.btn_play_slc_nivel = Button(self._slave, x, y, 210, 145, 100, 40,
                            "red", "blue",self.btn_play_click3, "",
                            path_font, path_font,20, "white")
        
        self.label_Stage_1 = Label(self._slave,200,20, 130, 50, "Empezar",
                                path_font,20,"white", "assets/graphics/interfaz/Table.png")

        self.label_Stage_2 = Label(self._slave,200,80, 130, 50, "Configuracion",
                                path_font, 20,"white", "assets/graphics/interfaz/Table.png")
        
        self.label_Stage_3 = Label(self._slave,200,140, 130, 50, "Seleccion nivel",
                                path_font, 20,"white", "assets/graphics/interfaz/Table.png")
        
        
        
        self.lista_widgets.append(self.btn_play_start)
        self.lista_widgets.append(self.btn_play_config)
        self.lista_widgets.append(self.btn_play_slc_nivel)
        self.lista_widgets.append(self.label_Stage_1)
        self.lista_widgets.append(self.label_Stage_2)
        self.lista_widgets.append(self.label_Stage_3)        
        
        
        
        
    def render(self):
        self._slave.fill(self._color_background)
        
    def update(self, lista_eventos,delta_ms=0):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)#POLIMORFISMO
        else:
            self.hijo.update(lista_eventos)
            
        self.elegir_stage()
        
            
    def elegir_stage(self):
        return self.stage
            
            
    def btn_play_click1(self, param):
        Form.set_active('stage_1')   
        Form.get_active()
        
                    
    def btn_play_click2(self, param):
        Form.set_active('sonido_menu')
        Form.get_active()

        
    def btn_play_click3(self, param):
        Form.set_active('seleccion_stage')
        Form.get_active()