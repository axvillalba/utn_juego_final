import json

nombre_juego = "En busqueda de Timcanpy"
screen_w = 600
screen_h = 600
FPS = 60
CONFIG_FILE_PATH = './configs/config.json'
path_font = './assets/Fonts/Blomberg-8MKKZ.otf'
DEBUG = False
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AMARILLO = (255,255,0)
COLOR_LINDO = (24,24,88)
altura_rect = 10
game_over_txt  = "FIN DEL JUEGO"
barra_vida_ancho = 136
barra_vida_alto = 12


def open_configs() -> dict:
    with open(CONFIG_FILE_PATH, 'r', encoding='utf-8') as config:
        return json.load(config)