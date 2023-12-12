import pygame
import sys
from pygame.locals import *
from models.GUI.GUI_seleccion_nivel import formSeleccionNivel
from models.GUI.GUI_menu_sonido import formSonido
from models.GUI.GUI_form_menu_main import formMainMenu
from auxiliar.constantes import *
from auxiliar.auxiliar_assets import *
from probando_cositas import Game_On

pygame.init()
reloj = pygame.time.Clock()
screen = pygame.display.set_mode((screen_w, screen_h))
back_img = pygame.image.load(main_img)
back_img = pg.transform.scale(back_img,(screen_w, screen_h))



#sonido_menu = formSonido(screen,50,350,500,200,"black", COLOR_LINDO, 5, True)
#seleccion_stage = formSeleccionNivel(screen,50,350,500,200,"black", COLOR_LINDO,5,True)
menu_principal = formMainMenu(screen,50,350,500,200,"black", COLOR_LINDO,5,True)




while True:
    reloj.tick(FPS)
    eventos = pygame.event.get()
    for event in eventos:
        match event.type:
            case pg.QUIT:
                pg.quit()
                sys.exit()
            case pg.KEYDOWN:
                Game_On('stage_1')
                

    
    screen.blit(back_img, back_img.get_rect())
    #sonido_menu.update(eventos)
    #seleccion_stage.update(eventos)
    menu_principal.update(eventos)
    
    pygame.display.flip()