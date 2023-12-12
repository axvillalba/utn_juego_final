from auxiliar.constantes import *
import pygame as pg

main_config = open_configs().get('main_page')
main_bg = main_config.get('background')
main_img = main_bg.get('path_img') 

stage_config = open_configs().get('stage_1')
bg = stage_config.get('background')
stage1_img = bg.get('bg_img') 
data_img = bg.get('fondo_datos')
life_img = bg.get('barra_vida')
music_fondo = bg.get('musica')
risa_fondo = bg.get('risa_fondo')
ataque_sonido = bg.get('ataque')





