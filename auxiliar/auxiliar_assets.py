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
bells_fondo = bg.get('musica')
risa_fondo = bg.get('risa_fondo')
ataque_sonido = bg.get('ataque')
timcanpy = bg.get('timca')


gui_config = open_configs().get('GUI')
table_gui = gui_config.get('table')
home_gui = gui_config.get('home')
menu_btn = gui_config.get('menu_btn')
close_btn = gui_config.get('close_btn')
previa_img = gui_config.get('pantalla_previa')
ganamos = gui_config.get('winwin')
audio_final = gui_config.get('audio_final')



musica_fondo = gui_config.get('musica_fondo')



