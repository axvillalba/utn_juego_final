import pygame as pg
import sys
from auxiliar.constantes import *
from models.stage import Stage
from auxiliar.auxiliar import *

# from models.game import Game

# if __name__ == '__main__':
    
#     Game.run_stage('stage_2')

screen = pg.display.set_mode((screen_w, screen_h))
pg.init()
clock = pg.time.Clock()


back_img = pg.image.load('assets\graphics\stage1_background.png')
back_img = pg.transform.scale(back_img,(screen_w, screen_h))
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
    
    screen.blit(back_img, back_img.get_rect())
    delta_ms = clock.tick(FPS)
    game.run(delta_ms)
    
    
    pg.display.update()

pg.quit()