from auxiliar.constantes import (open_configs)
import pygame
from models.player import Player
from models.enemy import Enemy
from models.plataforma import Plataforma


class Stage:
    def __init__(self, screen: pygame.surface.Surface, limit_w, limit_h, stage_name: str):

        # Abro el json con todos los datos correspondientes al stage que desee
        self.__configs = open_configs().get(stage_name)
        
        #Aca deberia de colocar el background y datos que corresponda segun el nivel
        
        #Creo las plataformas del stage
        self.__plataforma = pygame.sprite.Group()
        
        # Creo al jugador en la variable player_sprite
        self.__player_sprite = Player(limit_w / 2, 155, limit_h-12, frame_rate = 120, speed=5, gravity = 6, jump = 10,  stage_dict_configs=self.__configs)  # posicion inicial      
        #En self.player voy almacenar y manipular los sprites de player que voy a generar en la linea anterior
        self.__player = pygame.sprite.Group(self.__player_sprite)
        
        #Creo la variable en donde voy a guardar los sprites de Enemy que se crearan en esta clase
        self.__enemies = pygame.sprite.Group()
        #Creo las variables necesarias para poder trabajar con los datos que recibo del json y asi crear a los enemigos necesarios.
        self.__stage_configs = self.__configs.get('stage')
        self.__max_enemies = self.__stage_configs["max_amount_enemies"]
        self.__coordenadas_enemigos = self.__stage_configs.get("coords_enemies")
        self.__max_plataform = self.__stage_configs["max_amount_plataform"]
        self.__coords_plataform = self.__stage_configs[ "coord_plataformas"]
        self.__enemies_config = self.__configs.get('enemy')
        self.__damage_enemy = self.__enemies_config["damage"]     
        
        #Variables sobre el tamaño de pantalla y el surface para la creacion del mismo
        self.__limit_w = limit_w
        self.__limit_h = limit_h
        self.__main_screen = screen
        
        #Creacion de las plataformas correspondientes
        self.__plataforma_class = []
        self.create_plataforma()
        for plataform in self.__plataforma_class:
            self.__plataforma.add(plataform)

        #Creacion de la lista de enemigos y creacion de enemigos qe luego los ire agregando a self.enemies (de más arriba)
        self.__enemies_class = []
        self.spawnear_enemigos()
        for enemy in self.__enemies_class:
            self.__enemies.add(enemy)
            
        self.tiempo_inicios = pygame.time.get_ticks()    
        
        self.__player_win = True
        

    def controlar(self):    #Llamo a la funcion de la clase player para poder controlar sus movimientos
        self.__player_sprite.get_actividad()
        
    def create_plataforma(self):
        if self.__max_plataform > len (self.__coords_plataform):
            for coordenada in self.__coords_plataform:
                self.__plataforma_class.append(
                    Plataforma((coordenada.get("coord_x"),coordenada.get("coord_y")), self.__configs)
                )
        elif self.__max_plataform <= len (self.__coords_plataform):
            for coordenada in range (self.__max_plataform):
                self.__plataforma_class.append(
                    Plataforma((self.__coords_plataform[coordenada].get("coord_x"),
                                self.__coords_plataform[coordenada].get("coord_y")),
                    self.__configs)
                )
        
    def spawnear_enemigos(self):  #Funcion que crea a los enemigos y los guarda en la lista de enemies.class
        #Debo determinar cantidades para saber cual for agarrar para realizar la iteracion correspondiente
        if self.__max_enemies > len(self.__coordenadas_enemigos): 
            #Si la cantidad maxima de enemigos es mayor a las coordenadas enemigos(Se refiere a la lista que contiene en cada indice una coordenada)
            for coordenada in self.__coordenadas_enemigos:
                self.__enemies_class.append(
                    Enemy((coordenada.get("coord_x"), coordenada.get("coord_y")), 
                    self.__limit_w, self.__limit_h, self.__configs)
                )
        elif self.__max_enemies <= len(self.__coordenadas_enemigos):
            #Si la cantidad maxima de enemigos es menor o igual a las coordenadas enemigos(Se refiere a la lista que contiene en cada indice una coordenada)
            for coordenada in range(self.__max_enemies):
                self.__enemies_class.append(
                    Enemy((self.__coordenadas_enemigos[coordenada].get("coord_x"), 
                            self.__coordenadas_enemigos[coordenada].get("coord_y")), 
                    self.__limit_w, self.__limit_h, self.__configs)
                )

    def colisionar_contra_enemigos(self):
        for bullet in self.__player_sprite.get_bullets:
            cantidad_antes = len(self.__enemies)
            pygame.sprite.spritecollide(bullet, self.__enemies, True)
            cantidad_despues = len(self.__enemies)
            if cantidad_antes > cantidad_despues:
                cantidad_vencido = cantidad_antes - cantidad_despues
                self.__player_sprite.puntaje += cantidad_vencido * 100
                print(f'Puntaje actual: {self.__player_sprite.puntaje} Puntos')
            if len(self.__enemies) == 0 and not self.__player_win:
                self.__player_win = True
                print(f'Ganaste la partida con: {self.__player_sprite.puntaje} Puntos!')
    
    def atacan_enemigos(self):
        
        if pygame.sprite.groupcollide(self.__player, self.__enemies,False, False):
                # print("Te dieron!! cuidadoooooooooooooooo")
                self.__player_sprite.vida -= self.__damage_enemy
                # print(f'{self.__player_sprite.vida} vida')  
                # print(f'Vida restante: {self.__player_sprite.vida}')

    def retorno_puntaje(self):
        return self.__player_sprite.puntaje
    
    def retorno_vida(self):
        return self.__player_sprite.vida

    def run(self, delta_ms):
        # Actualizar todos los grupos de sprites
        # Dibujar todos los grupos de sprites
        # Actualizar y Dibujar Jugador        
        
        self.__plataforma.update(self.__main_screen)
        self.__player_sprite.update(self.__main_screen, delta_ms,self.__plataforma_class)
        #self.__player_sprite.draw(self.__main_screen)        
        self.retorno_puntaje()
        self.__enemies.update(delta_ms, self.__main_screen)
        self.atacan_enemigos()
        self.retorno_vida()
        self.colisionar_contra_enemigos()
        
        #self.enemies.draw(self.__main_screen)
