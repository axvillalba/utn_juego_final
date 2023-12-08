import pygame as pg
import sys
from auxiliar.constantes import *
from models.stage import Stage
from auxiliar.auxiliar import *
from auxiliar.auxiliar_assets import *


screen = pg.display.set_mode((screen_w, screen_h))
pg.init()
pg.display.set_caption(nombre_juego)
clock = pg.time.Clock()
pg.mixer.init()

sonido_fondo = pg.mixer.Sound(music_fondo)
sonido_fondo.play(-1)



back_img = pg.image.load(stage1_img)
back_img = pg.transform.scale(back_img,(screen_w, screen_h))
puntos_barra = pg.image.load(data_img)
puntos_barra = pg.transform.scale(puntos_barra,(200,50))
vida_barra = pg.image.load(life_img)
vida_barra = pg.transform.scale(vida_barra, (148,18))

juego_on = True
game = Stage(screen, screen_w, screen_h, 'stage_1') 

while juego_on == True:
    sonido_fondo.play(-1)
    
    

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
    fuente = pg.font.Font(path_font, 25)
    fuente_vida = pg.font.Font(path_font, 20)
    texto_tiempo = fuente.render(current_time_txt, True, COLOR_LINDO)

    puntos = game.retorno_puntaje()
    vida = game.retorno_vida()
    
    texto_puntos = f'Pts: {puntos}'
    render_puntos = fuente.render(texto_puntos, True, COLOR_LINDO)
    texto_vida = f'Vida: {vida}%'
    render_vida = fuente_vida.render(texto_vida, True, COLOR_LINDO)

    screen.blit(back_img, back_img.get_rect())
    screen.blit(puntos_barra,(10,10))
    screen.blit(puntos_barra,(385,10))
    screen.blit(vida_barra, (225,20))
    screen.blit(texto_tiempo, (50, 15))

    
    delta_ms = clock.tick(FPS)
    game.run(delta_ms)
    screen.blit(render_puntos,(440,15))
    screen.blit(render_vida, (255,20))
    
    
    pg.display.update()

pg.quit()