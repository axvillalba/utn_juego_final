from auxiliar.constantes import (open_configs)
import pygame
from models.player import Player
from models.enemy import Enemy
from models.plataforma import Plataforma
from models.fruta import Fruta
from models.trampas import Trampas
from auxiliar.auxiliar_assets import *
from models.GUI.GUI_form import Form


class Stage(Form):
    def __init__(self, name, screen: pygame.surface.Surface, limit_w, limit_h, stage_name: str,active,timer_10s):
        super().__init__(name, screen,0,0,0,0,AZUL,AZUL,-1,active)

        # Abro el json con todos los datos correspondientes al stage que desee
        self.__configs = open_configs().get(stage_name)
        self.active = active
        #Aca deberia de colocar el background y datos que corresponda segun el nivel
        
        #Creo las plataformas del stage y de las frutas
        self.__plataforma = pygame.sprite.Group()
        self.__fruta = pygame.sprite.Group()
        self.__trampa = pygame.sprite.Group()
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
        self.__enemies_config = self.__configs.get('enemy')
        self.__damage_enemy = self.__enemies_config["damage"]
        self.__max_plataform = self.__stage_configs["max_amount_plataform"]
        self.__coords_plataform = self.__stage_configs.get("coord_plataformas")
        self.__max_frutas = self.__stage_configs["max_amount_frutas"]
        self.__coordenadas_frutas = self.__stage_configs.get("coords_frutas")
        self.__frutas_configs = self.__configs.get("frutas")
        self.__fruta_vida_adicion = self.__frutas_configs['vida_adicional']
        self.__max_trampas = self.__stage_configs["max_amount_trampas"]
        self.__coords_trampas = self.__stage_configs.get("coords_trampas")
        self.__trampa_configs = self.__configs.get('trampas')
        self.__damage_trampa = self.__trampa_configs['damage']
        
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
        #Creacion de las frutas
        self.__frutas_class = []
        self.create_frutas()
        for frutas in self.__frutas_class:
            self.__fruta.add(frutas)
        #Creacion de las trampas    
        self.__trampas_class = []
        self.create_trampas()
        for trampas in self.__trampas_class:
            self.__trampa.add(trampas)
        
        self.tiempo_inicios = pygame.time.get_ticks()    
        self.__player_win = False
        #Atributos de sonidos
        self.risa_malvada = pygame.mixer.Sound(risa_fondo)
        self.timer_10s= timer_10s
        
        #Atributos de cosas
        self.back_img = pg.image.load(stage1_img)
        self.back_img = pg.transform.scale(self.back_img,(screen_w, screen_h))
        self.puntos_barra = pg.image.load(data_img)
        self.puntos_barra = pg.transform.scale(self.puntos_barra,(200,50))
        self.vida_barra = pg.image.load(life_img)
        self.vida_barra = pg.transform.scale(self.vida_barra, (148,18))
        
        #Atributo de fuentes
        self.fuente = pg.font.Font(path_font, 25)
        self.fuente_vida = pg.font.Font(path_font, 20)


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
                
    def create_frutas(self):
        if self.__max_frutas > len (self.__coordenadas_frutas):
            for coordenada in self.__coordenadas_frutas:
                self.__frutas_class.append(
                    Fruta((coordenada.get("coord_x"), coordenada.get("coord_y")), 
                    self.__configs)
                )
        elif self.__max_frutas <= len (self.__coordenadas_frutas):
            for coordenada in range(self.__max_frutas):
                self.__frutas_class.append(
                    Fruta((self.__coordenadas_frutas[coordenada].get("coord_x"), 
                            self.__coordenadas_frutas[coordenada].get("coord_y")), 
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

    def create_trampas(self):
        if self.__max_trampas > len(self.__coords_trampas): 
            for coordenada in self.__coords_trampas:
                self.__trampas_class.append(
                    Trampas((coordenada.get("coord_x"), coordenada.get("coord_y")), 
                    self.__configs)
                )
        elif self.__max_trampas <= len(self.__coords_trampas):
            for coordenada in range(self.__max_trampas):
                self.__trampas_class.append(
                    Trampas((self.__coords_trampas[coordenada].get("coord_x"), 
                            self.__coords_trampas[coordenada].get("coord_y")), 
                    self.__configs)
                )
        
    def colisionar_contra_enemigos(self):
        for bullet in self.__player_sprite.get_bullets:
            cantidad_antes = len(self.__enemies)
            pygame.sprite.spritecollide(bullet, self.__enemies, True)
            cantidad_despues = len(self.__enemies)
            if cantidad_antes > cantidad_despues:
                cantidad_vencido = cantidad_antes - cantidad_despues
                self.__player_sprite.puntaje += cantidad_vencido * 100
                bullet.kill()
                print(f'Puntaje actual: {self.__player_sprite.puntaje} Puntos')
            if len(self.__enemies) == 0 and not self.__player_win:
                self.__player_win = True
                print(f'Ganaste la partida con: {self.__player_sprite.puntaje} Puntos!')
                
    def gana_nivel(self):
        if self.__player_win == True:
            if Form.get_active() == 'stage_1':
                Form.set_active('stage_2')
                Form.get_active()
            elif Form.get_active() =='stage_2':
                Form.set_active('stage_3')
                Form.get_active()
            elif Form.get_active() =='stage_3':
                Form.set_active('menu_principal')
                Form.get_active()
                
    def toco_fruta(self):
        if pygame.sprite.groupcollide(self.__player, self.__fruta, False, True):
            self.__player_sprite.vida += self.__fruta_vida_adicion

    def atacan_enemigos(self):
        if pygame.sprite.groupcollide(self.__player, self.__enemies,False, False):
                self.__player_sprite.vida -= self.__damage_enemy

    def atacan_trampas(self):
        if pygame.sprite.groupcollide(self.__player, self.__trampa,False, True):
            self.__player_sprite.vida -= self.__damage_trampa

    def trampas_renuevan(self):
        
        self.create_trampas()
        for trampas in self.__trampas_class:
            self.__trampa.add(trampas)
            
    def retorno_puntaje(self):
        return self.__player_sprite.puntaje
    
    def retorno_vida(self):
        return self.__player_sprite.vida

    def run(self, delta_ms):
        # Actualizar todos los grupos de sprites
        # Dibujar todos los grupos de sprites
        # Actualizar y Dibujar Jugador        
        self.retorno_vida()
        self.__plataforma.update(self.__main_screen)
        self.__fruta.update(self.__main_screen)
        self.__player_sprite.update(self.__main_screen, delta_ms,self.__plataforma_class) 
        self.__enemies.update(delta_ms, self.__main_screen)
        self.__trampa.update(self.__main_screen)
        self.atacan_enemigos()
        self.colisionar_contra_enemigos()
        self.atacan_trampas()
        self.toco_fruta()
        
    def update(self,lista_eventos,delta_ms):
        
        for evento in lista_eventos:
            match evento.type:
                case pygame.KEYDOWN: 
                    self.controlar()
                case self.timer_10s:
                    self.trampas_renuevan()
                    self.risa_malvada.play()
                    
        self.run(delta_ms)
        

    def draw (self, screen:pygame.surface.Surface):
        self.render_texto()
        screen.blit(self.back_img, self.back_img.get_rect())
        
        screen.blit(self.puntos_barra,(10,10))
        screen.blit(self.puntos_barra,(385,10))
        screen.blit(self.vida_barra, (225,20))
        
        screen.blit(self.texto_tiempo, (50, 15))
        screen.blit(self.render_puntos,(440,15))
        screen.blit(self.render_vida, (255,20))
        

    def render_texto(self):
        current_time =pg.time.get_ticks()
        segundos = current_time //1000
        current_time_txt = f'Time: {segundos} SEG '
        
        self.texto_tiempo = self.fuente.render(current_time_txt, True, COLOR_LINDO)

        puntos = self.retorno_puntaje()
        vida = self.retorno_vida()
        #vida_redondeo = round(vida, 2)
        vida_formato = format(vida, '.2f')
        
        texto_puntos = f'Pts: {puntos}'
        self.render_puntos = self.fuente.render(texto_puntos, True, COLOR_LINDO)
        texto_vida = f'Vida: {vida_formato}'
        self.render_vida = self.fuente_vida.render(texto_vida, True, COLOR_LINDO)
