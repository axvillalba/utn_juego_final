import pygame
from pygame.locals import *

from models.GUI.GUI_button import *
from models.GUI.GUI_label import *
from models.GUI.GUI_form import *
from models.GUI.GUI_button_image import *
from auxiliar.constantes import *



class formSeleccionNivel(Form):
    
    def __init__(self, name,screen: pygame.Surface, x: int, y: int, w:int, h: int, color_background, color_border = "Black", border_size: int = -1, active = True):
        super().__init__(name,screen, x,y,w,h,color_background, color_border, border_size, active)
        
        
        
        self.btn_play_stage1 = Button(self._slave, x, y, 210, 25, 30, 40,
                            "red", "blue",self.btn_play_click1, "",
                            path_font, path_font,15, "white")
        
        self.btn_play_stage2 = Button(self._slave, x, y, 210, 85, 30, 40,
                            "red", "blue",self.btn_play_click2, "",
                            path_font, path_font,15, "white")
        
        self.btn_play_stage3 = Button(self._slave, x, y, 210, 145, 30, 40,
                            "red", "blue",self.btn_play_click3, "",
                            path_font, path_font,15, "white")
        
        self.label_Stage_1 = Label(self._slave,200,20, 80, 50, "Stage 1",
                                path_font, 15,"white", "assets/graphics/interfaz/Table.png")

        self.label_Stage_2 = Label(self._slave,200,80, 80, 50, "Stage 2",
                                path_font, 15,"white", "assets/graphics/interfaz/Table.png")
        
        self.label_Stage_3 = Label(self._slave,200,140, 80, 50, "Stage 3- Final",
                                path_font, 15,"white", "assets/graphics/interfaz/Table.png")
        
        self.bt_exit = Button_Image(self._slave,x,y,20,20,30,30,"assets/graphics/interfaz/close_2.png"
                                    ,self.btn_close, "","","Arial",1,AZUL,AZUL,"Black",-1)
        
        
        
        self.lista_widgets.append(self.btn_play_stage1)
        self.lista_widgets.append(self.btn_play_stage2)
        self.lista_widgets.append(self.btn_play_stage3)
        self.lista_widgets.append(self.label_Stage_1)
        self.lista_widgets.append(self.label_Stage_2)
        self.lista_widgets.append(self.label_Stage_3)   
        self.lista_widgets.append(self.bt_exit)     
        
        
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
            
            
            
    def btn_play_click1(self, param):
        Form.set_active('stage_1')
        Form.get_active()

            
    def btn_play_click2(self, param):
        Form.set_active('stage_1')
        Form.get_active()
        
    def btn_play_click3(self, param):
        pass
    
    def btn_close(self, param):
        Form.set_active('menu_principal')
        Form.get_active()
        
        