from auxiliar.constantes import (open_configs)
import pygame
from models.player import Player
from models.enemy import Enemy

class Stage:
    def __init__(self, screen: pygame.surface.Surface, limit_w, limit_h, stage_name: str):

        # Abro el json con todos los datos correspondientes al stage que desee
        self.__configs = open_configs().get(stage_name)
        # Creo al jugador en la variable player_sprite
        self.player_sprite = Player(limit_w / 2, 445, limit_h-12, speed=5, gravity = 5, jump = 10,  stage_dict_configs=self.__configs)  # posicion inicial      
        #En self.player voy almacenar y manipular los sprites de player que voy a generar en la linea anterior
        self.player = pygame.sprite.Group(self.player_sprite)
        #Creo la variable en donde voy a guardar los sprites de Enemy que se crearan en esta clase
        self.enemies = pygame.sprite.Group()
        #Creo las variables necesarias para poder trabajar con los datos que recibo del json y asi crear a los enemigos necesarios.
        self.__stage_configs = self.__configs.get('stage')
        self.__max_enemies = self.__stage_configs["max_amount_enemies"]
        self.__coordenadas_enemigos = self.__stage_configs.get("coords_enemies")
        
        #Variables sobre el tamaño de pantalla y el surface para la creacion del mismo
        self.__limit_w = limit_w
        self.__limit_h = limit_h
        self.__main_screen = screen

        #Creacion de la lista de enemigos y creacion de enemigos qe leugo los ire agregando a self.enemies (de más arriba)
        self.enemies_class = []
        self.spawnear_enemigos()
        for enemy in self.enemies_class:
            self.enemies.add(enemy)
            
        self.__player_win = True


    def controlar(self):    #Llamo a la funcion de la clase player para poder controlar sus movimientos
        self.player_sprite.get_actividad()

    def spawnear_enemigos(self):  #Funcion que crea a los enemigos y los guarda en la lista de enemies.class
        #Debo determinar cantidades para saber cual for agarrar para realizar la iteracion correspondiente
        if self.__max_enemies > len(self.__coordenadas_enemigos): 
            #Si la cantidad maxima de enemigos es mayor a las coordenadas enemigos(Se refiere a la lista que contiene en cada indice una coordenada)
            for coordenada in self.__coordenadas_enemigos:
                self.enemies_class.append(
                    Enemy((coordenada.get("coord_x"), coordenada.get("coord_y")), 
                    self.__limit_w, self.__limit_h, self.__configs)
                )
        elif self.__max_enemies <= len(self.__coordenadas_enemigos):
            #Si la cantidad maxima de enemigos es menor o igual a las coordenadas enemigos(Se refiere a la lista que contiene en cada indice una coordenada)
            for coordenada in range(self.__max_enemies):
                self.enemies_class.append(
                    Enemy((self.__coordenadas_enemigos[coordenada].get("coord_x"), 
                            self.__coordenadas_enemigos[coordenada].get("coord_y")), 
                    self.__limit_w, self.__limit_h, self.__configs)
                )

    def colisionar_contra_enemigos(self):
        for bullet in self.player_sprite.get_bullets:
            cantidad_antes = len(self.enemies)
            pygame.sprite.spritecollide(bullet, self.enemies, True)
            cantidad_despues = len(self.enemies)
            if cantidad_antes > cantidad_despues:
                cantidad_vencido = cantidad_antes - cantidad_despues
                self.player_sprite.puntaje += cantidad_vencido * 100
                print(f'Puntaje actual: {self.player_sprite.puntaje} Puntos')
            if len(self.enemies) == 0 and not self.__player_win:
                self.__player_win = True
                print(f'Ganaste la partida con: {self.player_sprite.puntaje} Puntos!')

    def run(self, delta_ms):
        # Actualizar todos los grupos de sprites
        # Dibujar todos los grupos de sprites
        # Actualizar y Dibujar Jugador        
        self.player.update(self.__main_screen)
        self.player.draw(self.__main_screen)        
        self.enemies.update(delta_ms, self.__main_screen)
        self.colisionar_contra_enemigos()
        #self.enemies.draw(self.__main_screen)
