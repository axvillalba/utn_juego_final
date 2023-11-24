import pygame
from auxiliar.auxiliar import SurfaceManager as sf
from models.Bullet import *


class Player(pygame.sprite.Sprite):
    
    def __init__(self, coord_x, coord_y, constraint, frame_rate, speed, jump, gravity, stage_dict_configs: dict):
        super().__init__()
        
        #Cargar del json el diccionario del player
        self.__player_configs = stage_dict_configs.get('player')
        # Mostrar sprite del jugador / Solo la figura estatica / probar con eso, despues le damos movimiento a la imagen.
        
        
        # self.image = pygame.image.load(self.__player_configs['player_stand']).convert_alpha()
        # #En este caso lo que hago es darle el rectangulo al sprite de la linea anterior. ahora self.rect tendrá los metodos de rectangulos. 
        #self.__rect = self.image.get_rect(midbottom=(coord_x, coord_y))
        
        
        self.__iddle_r = sf.get_surface_from_spritesheet('./assets/graphics/player_allen/stand.png',4,1)
        self.__iddle_l = sf.get_surface_from_spritesheet('./assets/graphics/player_allen/stand.png',4,1,True)        
        self.__walk_r = sf.get_surface_from_spritesheet('./assets/graphics/player_allen/run.png', 8,1)
        self.__walk_l = sf.get_surface_from_spritesheet('./assets/graphics/player_allen/run.png', 8,1, flip=True)
        # self.__attack_melee_r = sf.get_surface_from_spritesheet('./assets/graphics/player_allen/attack_melee.png',7,1)
        # self.__attack_melee_l = sf.get_surface_from_spritesheet('./assets/graphics/player_allen/attack_melee.png',7,1, flip=True)
        self.__attack_laser_r = sf.get_surface_from_spritesheet('./assets/graphics/player_allen/attack_3.png',4,1)
        self.__attack_laser_l = sf.get_surface_from_spritesheet('./assets/graphics/player_allen/attack_3.png',4,1, flip = True)
        
        
        #self.__image_shot = sf.get_surface_from_spritesheet('./assets\graphics\player_allen\power_attack.png',8,1)
        #self.__rect_disparo = self.__rect
        
        self.__player_animation_time = 0
        self.__actual_frame_index = 0
        self.__frame_rate = frame_rate
        self.__actual_animation = self.__iddle_r
        self.__actual_img_animation = self.__actual_animation[self.__actual_frame_index]
        self.__rect = self.__actual_img_animation.get_rect(midbottom=(coord_x, coord_y))
        
        # Atributos de movimiento / speed=movimientos de pixeles que se mueve el personaje (recibe el valor por parametro) / constrait = restriccion de mov en el eje x
        self.speed = speed 
        self.max_x_constraint = constraint
        self.jump = jump
        self.gravity = gravity

        #Booleanos de movimientos
        self.__is_jumping = False
        self.__is_looking_right = True
        
        #coordenadas
        self.coord_x = coord_x
        self.coord_y = coord_y
        
        # # Atributos para disparar y recargar
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 600
        self.bullet_group = pygame.sprite.Group()
        self.puntaje = 0
        self.is_shooting = False
        
    # Comienzo a crear todas los metodos correspondientes a Player
    
    #Metodos para la animacion
    
    def __set_x_animations_preset(self,animation_list: list[pygame.surface.Surface], look_r: bool):
        self.__actual_animation = animation_list
        self.__is_looking_right = look_r
        
    
    # def __set_y_animations_preset(self):
    #     self.__move_y = -self.__jump
    #     self.__move_x = self.__speed_run if self.__is_looking_right else -self.__speed_run
    #     self.__actual_animation = self.__jump_r if self.__is_looking_right else self.__jump_l
    #     self.__initial_frame = 0
    #     self.__is_jumping = True
        
    def get_actividad(self):
        #Esta funcion va a determinar los movimientos del Player 
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:  # movimiento sobre eje x
            self.__rect.x += self.speed
            self.__is_looking_right = True
            self.__set_x_animations_preset(self.__walk_r, self.__is_looking_right)
        elif keys[pygame.K_LEFT]:
            self.__rect.x -= self.speed 
            self.__is_looking_right = False
            self.__set_x_animations_preset(self.__walk_l, self.__is_looking_right)
        elif keys [pygame.K_DOWN]: #Solo va a quedar ahora para probar movimientos
            self.__rect.y += 2
        elif keys[pygame.K_SPACE] and not self.__is_jumping:
            self.saltar()
        elif keys [pygame.K_j] and not self.is_shooting:
            if self.__is_looking_right == True:
                self.__set_x_animations_preset(self.__attack_laser_r,self.__is_looking_right)
                self.disparar()
            elif self.__is_looking_right == False:
                self.__set_x_animations_preset(self.__attack_laser_l, self.__is_looking_right)
                self.disparar()
        else:
            self.stay()
            
        
            
    @property
    def get_bullets(self) -> list[Bullet]:
        return self.bullet_group
        
    def disparar(self):
        if not self.is_shooting:
            self.shoot_laser()
            self.is_shooting = False
            
    def create_bullet(self):
        if self.__is_looking_right == True:
            direccion = 'right'
        else:
            direccion = 'left'
        return Bullet(self.__rect.x, self.__rect.y, direccion, True)

    def shoot_laser(self):  # disparar laser
        self.bullet_group.add(self.create_bullet())

    
    def saltar(self):

        #self.is_jumping = True
        self.__rect.y -= self.jump        
        self.__rect.y += self.gravity
    # Actualizar la posición del personaje
        self.coord_x += self.__rect.x
        self.coord_y += self.__rect.y
    # Ver si el personaje salto de más
        if self.coord_y <= (self.__rect.y - self.jump):
            self.__rect.y += self.jump

        self.__is_jumping = False
        
        
    def stay(self):
        if self.__actual_animation != self.__iddle_l and self.__actual_animation != self.__iddle_r:
            self.__actual_animation = self.__iddle_r if self.__is_looking_right else self.__iddle_l
            self.__actual_frame_index = 0

    def constraint(self):  # Ajusta al jugador a los limites de la pantalla
        if self.__rect.left<= 12:
            self.__rect.left = 12
        if self.__rect.right >= self.max_x_constraint:
            self.__rect.right = self.max_x_constraint
        if self.__rect.top <= 100:
            self.__rect.top = 100
        if self.__rect.bottom >= 555:
            self.__rect.bottom = 555
            
    def do_animation(self, delta_ms):
        self.__player_animation_time += delta_ms
        if self.__player_animation_time >= self.__frame_rate:
            self.__player_animation_time = 0
            if self.__actual_frame_index < len(self.__actual_animation) - 1:
                self.__actual_frame_index += 1
            else:
                self.__actual_frame_index = 0
                if self.__is_jumping:
                    self.__is_jumping = False
                    self.__rect.y = 0
                    

    def update(self, screen: pygame.surface.Surface, delta_ms):
        
        self.do_animation(delta_ms)    
        self.get_actividad()
        self.constraint()
        self.bullet_group.draw(screen)
        self.bullet_group.update()

    def draw(self, screen: pygame.surface.Surface):
        
        self.__actual_img_animation = self.__actual_animation[self.__actual_frame_index]
        screen.blit(self.__actual_img_animation, self.__rect)