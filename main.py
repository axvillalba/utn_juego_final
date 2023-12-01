import pygame as pg
import sys
from auxiliar.constantes import *
from models.stage import Stage
from auxiliar.auxiliar import *


screen = pg.display.set_mode((screen_w, screen_h))
pg.init()
clock = pg.time.Clock()

back_img = pg.image.load('assets\graphics\stage1_background.png')
back_img = pg.transform.scale(back_img,(screen_w, screen_h))
puntos_barra = pg.image.load('assets/graphics/interfaz/Banner04.png')
puntos_barra = pg.transform.scale(puntos_barra,(200,50))
juego_on = True
game = Stage(screen, screen_w, screen_h, 'stage_1') 

while juego_on == True:

    lista_eventos = pg.event.get()
    for evento in lista_eventos:
        match evento.type:
            case pg.QUIT:
                pg.quit()
                sys.exit()
            case pg.KEYDOWN:
                game.controlar()
    
    current_time =pg.time.get_ticks()
    segundos = current_time //1000
    current_time_txt = f'Time: {segundos} SEG '
    fuente = pg.font.Font("assets\Fonts\Blomberg-8MKKZ.otf", 25)
    texto = fuente.render(current_time_txt, True, COLOR_LINDO)

    puntos = game.retorno_puntaje()
    texto_puntos = f'Pts: {puntos}'
    render_puntos = fuente.render(texto_puntos, True, COLOR_LINDO)


    screen.blit(back_img, back_img.get_rect())
    screen.blit(puntos_barra,(10,10))
    screen.blit(puntos_barra,(380,10))
    screen.blit(texto, (50, 15))
    screen.blit(render_puntos,(440,15))
    delta_ms = clock.tick(FPS)
    game.run(delta_ms)
    
    
    pg.display.update()

pg.quit()