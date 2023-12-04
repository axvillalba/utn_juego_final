from auxiliar.constantes import *
import pygame as pg

main_config = open_configs().get('main_page')
main_img = main_config.get('path_img') 

stage_config = open_configs().get('stage_1')
bg = stage_config.get('background')
stage1_img = bg.get('bg_img') 
data_img = bg.get('fondo_datos')
life_img = bg.get('barra_vida')