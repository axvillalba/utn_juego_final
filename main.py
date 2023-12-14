import pygame as pg
import sys
from auxiliar.constantes import *
from models.GUI.GUI_form import Form
from models.GUI.GUI_form_menu_score import FormMenuScore
from models.stage import Stage
from auxiliar.auxiliar import *
from auxiliar.auxiliar_assets import *
from models.GUI.GUI_form_menu_main import formMainMenu
from models.GUI.GUI_seleccion_nivel import formSeleccionNivel
from models.GUI.GUI_menu_sonido import formSonido
from models.GUI.GUI_form_info_previa import formIntro
from models.GUI.GUI_form_ganaste import formGanaste
screen = pg.display.set_mode((screen_w, screen_h))
pg.init()
pg.display.set_caption(nombre_juego)
clock = pg.time.Clock()
pg.mixer.init()
back_img = pg.image.load(main_img)
back_img = pg.transform.scale(back_img,(screen_w, screen_h))

timer_10s = pg.USEREVENT + 1 
pg.time.set_timer(timer_10s,10000)


juego_on = True
game = Stage('stage_1',screen, screen_w, screen_h, 'stage_1',False, timer_10s)
game_2 = Stage('stage_2',screen, screen_w, screen_h, 'stage_2',False, timer_10s)
game_3 = Stage('stage_3',screen, screen_w, screen_h, 'stage_3',False, timer_10s)
menu_principal = formMainMenu(screen,"menu_principal",50,350,500,200,"black", COLOR_LINDO,5,True)
seleccion_stage = formSeleccionNivel("seleccion_stage",screen,50,350,500,200,"black", COLOR_LINDO,5,False)
sonido_menu = formSonido("sonido_menu",screen,50,350,500,200,"black", COLOR_LINDO, 5, False)
screen_intro = formIntro(screen,"screen_intro",0,0,600,600,"black",COLOR_LINDO,5,False)
final = formGanaste(screen,"ganamos",50,150,500,300,"black",COLOR_LINDO,5,False)


while juego_on == True:
    lista_eventos = pg.event.get()
    for evento in lista_eventos:
            if evento.type == pg.QUIT:
                pg.quit()
                sys.exit()
                
                
    delta_ms = clock.tick(FPS)
    formulario_activo = Form.get_active()
    screen.blit(back_img, back_img.get_rect())
    formulario_activo.draw(screen)
    formulario_activo.update(lista_eventos,delta_ms)

    pg.display.update()

pg.quit()