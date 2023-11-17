import pygame
from models.Bullet import Bullet
from auxiliar.auxiliar import SurfaceManager as sf


class Player(pygame.sprite.Sprite):
    
    
    def __init__(self, coord_x, coord_y, constraint, speed, stage_dict_configs: dict, gravity = 16, jump = 32):
        super().__init__()

        self.__player_configs = stage_dict_configs.get('player')
        # Mostrar sprite del jugador
        self.image = pygame.image.load(self.__player_configs['player_img']).convert_alpha()
        self.rect = self.image.get_rect(midbottom=(coord_x, coord_y))

        # Atributos de movimiento
        self.speed = speed
        self.max_x_constraint = constraint
        
        

        self.__iddle_r = sf.get_surface_from_spritesheet('./assets/graphics/player_allen/stand.png', 4, 1)
        self.__iddle_l = sf.get_surface_from_spritesheet('./assets/graphics/player_allen/stand.png', 4, 1, flip=True)
        self.__walk_r = sf.get_surface_from_spritesheet('./assets/graphics/player_allen/run.png', 8, 1)
        self.__walk_l = sf.get_surface_from_spritesheet('./assets/graphics/player_allen/run.png', 8, 1, flip=True)
        
        # self.__jump_r = sf.get_surface_from_spritesheet('./assets/graphics/player_allen/player_jump.png', 6, 1)
        # self.__jump_l = sf.get_surface_from_spritesheet('./assets/graphics/player_allen/player_jump.png', 6, 1, flip=True)

        self.__move_x = coord_x
        self.__move_y = coord_y
        self.__gravity = gravity
        self.__jump = jump
        self.__is_jumping = False
        self.__initial_frame = 0
        self.__actual_animation = self.__iddle_r
        self.__actual_img_animation = self.__actual_animation[self.__initial_frame]
        self.__rect = self.__actual_img_animation.get_rect()
        self.__is_looking_right = True




        # Atributos para disparar y recargar
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 600
        self.bullet_group = pygame.sprite.Group()
        self.puntaje = 0


    def __set_x_animations_preset(self, pos_x: int, animation_list: list[pygame.surface.Surface], look_r: bool):
        self.__move_x = pos_x
        self.__actual_animation = animation_list
        self.__is_looking_right = look_r
        
        
    def walk(self, direction: str):
        
        
        
        
        match direction:
            case 'Right':
                look_right = True
                self.__set_x_animations_preset(self.speed, self.__walk_r, look_r=look_right)
            case 'Left':
                look_right = False
                self.__set_x_animations_preset(self.speed, self.__walk_l, look_r=look_right)
                
    def stay(self):
        if self.__actual_animation != self.__iddle_l and self.__actual_animation != self.__iddle_r:
            self.__actual_animation = self.__iddle_r if self.__is_looking_right else self.__iddle_l
            self.__initial_frame = 0
            self.__pos_x = 0
            self.__pos_y = 0


    def manejar_eventos_teclado(self):  # Eventos del jugador
        """
        The function handles keyboard events for player movement and shooting.
        """
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:  # movimiento sobre eje x
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        
        if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:# movimiento sobre eje x
            self.walk('Right')
        if keys[pygame.K_LEFT]:
            self.walk('Left') 
        
        if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            self.stay()

    def constraint(self):  # Ajusta al jugador a los limites de la pantalla
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_x_constraint:
            self.rect.right = self.max_x_constraint


    def update(self, screen: pygame.surface.Surface):
        self.manejar_eventos_teclado()
        self.constraint()
        self.bullet_group.draw(screen)
        self.bullet_group.update()
