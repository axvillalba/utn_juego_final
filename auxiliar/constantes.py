import json

screen_w = 600
screen_h = 600
FPS = 60
CONFIG_FILE_PATH = './configs/config.json'


def open_configs() -> dict:
    with open(CONFIG_FILE_PATH, 'r', encoding='utf-8') as config:
        return json.load(config)