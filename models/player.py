import pygame
from auxiliar.auxiliar import *
from models.Bullet import *


class Player(pygame.sprite.Sprite):
    
    def __init__(self, coord_x, coord_y, constraint, speed, jump, gravity, stage_dict_configs: dict):
        super().__init__()
        
        #Cargar del json el diccionario del player
        self.__player_configs = stage_dict_configs.get('player')
        # Mostrar sprite del jugador / Solo la figura estatica / probar con eso, despues le damos movimiento a la imagen.
        self.image = pygame.image.load(self.__player_configs['player_stand']).convert_alpha()
        #En este caso lo que hago es darle el rectangulo al sprite de la linea anterior. ahora self.rect tendrá los metodos de rectangulos. 
        self.rect = self.image.get_rect(midbottom=(coord_x, coord_y))
        
        self.image_shot = pygame.image.load(self.__player_configs['player_shoot']).convert_alpha()
        self.rect = self.image_shot.get_rect(midbottom=(coord_x, coord_y))
        
        
        # Atributos de movimiento / speed=movimientos de pixeles que se mueve el personaje (recibe el valor por parametro) / constrait = restriccion de mov en el eje x
        self.speed = speed 
        self.max_x_constraint = constraint
        self.jump = jump
        self.gravity = gravity

        #Booleanos de movimientos
        self.is_jumping = False
        self.is_looking_right = True
        
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
    
    def get_actividad(self):
        #Esta funcion va a determinar los movimientos del Player 
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:  # movimiento sobre eje x
            self.rect.x += self.speed
            self.is_looking_right = True
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed 
            self.is_looking_right = False
        elif keys [pygame.K_DOWN]: #Solo va a quedar ahora para probar movimientos
            self.rect.y += 2
        elif keys[pygame.K_SPACE] and not self.is_jumping:
            self.saltar()
        elif keys [pygame.K_h] and not self.is_shooting:
            print('Estoy apretando una h')
            self.disparar()
            
            
    @property
    def get_bullets(self) -> list[Bullet]:
        return self.bullet_group
        
    def disparar(self):
        if not self.is_shooting:
            self.shoot_laser()
            self.is_shooting = False
            
    def create_bullet(self):
        return Bullet(self.rect.centerx, self.rect.bottom, 'left', True)

    def shoot_laser(self):  # disparar laser
        self.bullet_group.add(self.create_bullet())

    
    def saltar(self):

        #self.is_jumping = True
        self.rect.y -= self.jump        
        self.rect.y += self.gravity
    # Actualizar la posición del personaje
        self.coord_x += self.rect.x
        self.coord_y += self.rect.y
    # Ver si el personaje salto de más
        if self.coord_y <= (self.rect.y - self.jump):
            self.rect.y += self.jump

        self.is_jumping = False


    def constraint(self):  # Ajusta al jugador a los limites de la pantalla
        if self.rect.left<= 12:
            self.rect.left = 12
        if self.rect.right >= self.max_x_constraint:
            self.rect.right = self.max_x_constraint
        if self.rect.top <= 100:
            self.rect.top = 100
        if self.rect.bottom >= 555:
            self.rect.bottom = 555
            

    def update(self, screen: pygame.surface.Surface):
        self.get_actividad()
        self.constraint()
        self.bullet_group.draw(screen)
        self.bullet_group.update()
        