import pygame
import game_modules.__search_abs_path__ as m_path
import game_modules.__settings__ as m_settings
import game_modules.rectangle.main_platform as m_platform
import game_modules.sounds.sounds as m_sound

pygame.init()

class Ball():
    def __init__(self, x: int, y: int, width: int, height: int, name_image: str):
        self.X = x
        self.Y = y
        self.WIDTH = width
        self.HEIGHT = height
        self.NAME_IMAGE = name_image
        self.IMAGE = None
        self.BALL_RECT = None
        self.SPEED = 7
        self.IS_GAME_STARTED = True

        self.MOVE_RIGHT_TOP = True
        self.MOVE_LEFT_TOP = False
        self.MOVE_LEFT_BOT = False
        self.MOVE_RIGHT_BOT = False

        self.PLATFORM_MOVE_RIGHT = False
        self.PLATFORM_MOVE_LEFT = False
        self.PLATFORM_NOT_MOVING = True

        self.BALL_CENTER_X = self.WIDTH / 2
        self.BALL_CENTER_Y = self.HEIGHT / 2

        self.load_image()

    def load_image(self):
        image_path = m_path.search_abs_path(file_name= self.NAME_IMAGE)
        image_load = pygame.image.load(image_path)
        self.IMAGE = pygame.transform.scale(surface= image_load, size= (self.WIDTH, self.HEIGHT))
        self.BALL_RECT = pygame.Rect(self.X, self.Y, self.WIDTH, self.HEIGHT)
        
    def show_image(self, name_screen: object):
        name_screen.blit(source= self.IMAGE, dest= (self.X, self.Y))

    def move_ball(self):
        self.BALL_RECT.x = self.X
        self.BALL_RECT.y = self.Y
        if self.MOVE_RIGHT_TOP == True:
            if self.BALL_RECT.x == 0:
                self.X += self.SPEED
                self.Y -= self.SPEED
        if self.IS_GAME_STARTED == True and self.X + self.WIDTH <= m_settings.screen_width and self.X >5 and self.MOVE_RIGHT_TOP == True:
            self.X += self.SPEED
            self.Y -= self.SPEED
            if self.X + self.WIDTH == m_settings.screen_width:
                self.MOVE_RIGHT_TOP = False
                self.MOVE_LEFT_TOP = True
            elif self.Y == 5:
                self.MOVE_RIGHT_TOP = False
                self.MOVE_RIGHT_BOT = True
        if self.MOVE_LEFT_TOP == True and self.Y >= 0:
            self.X -= self.SPEED
            self.Y -= self.SPEED
            if self.Y <= 0:
                self.MOVE_LEFT_TOP = False
                self.MOVE_LEFT_BOT = True
            elif self.X <= 7:
                self.MOVE_RIGHT_TOP = True
                self.MOVE_LEFT_TOP = False
            elif self.BALL_RECT.colliderect(m_platform.main_platform) and self.X <= 7:
                self.MOVE_RIGHT_TOP = True
                self.MOVE_LEFT_TOP = False
        if self.MOVE_LEFT_BOT == True and self.X >= 0:
            self.X -= self.SPEED
            self.Y += self.SPEED
            if self.X <= 0:
                self.MOVE_LEFT_BOT = False
                self.MOVE_RIGHT_BOT = True
            elif self.BALL_RECT.colliderect(m_platform.main_platform) and m_platform.main_platform.y + 10 >= self.BALL_RECT.y + self.BALL_RECT.height and self.PLATFORM_MOVE_LEFT == True:
                m_sound.platfotm_and_edges_sound.play()
                self.MOVE_LEFT_BOT = False
                self.MOVE_LEFT_TOP = True
            elif self.BALL_RECT.colliderect(m_platform.main_platform) and m_platform.main_platform.y + 10 >= self.BALL_RECT.y + self.BALL_RECT.height and self.PLATFORM_MOVE_RIGHT == True:
                m_sound.platfotm_and_edges_sound.play()
                self.MOVE_LEFT_BOT = False
                self.MOVE_RIGHT_TOP = True
            elif self.BALL_RECT.colliderect(m_platform.main_platform) and m_platform.main_platform.y + 10 >= self.BALL_RECT.y + self.BALL_RECT.height and self.PLATFORM_NOT_MOVING == True:
                m_sound.platfotm_and_edges_sound.play()
                self.MOVE_LEFT_BOT = False
                self.MOVE_LEFT_TOP = True
        if self.MOVE_RIGHT_BOT == True:
            self.X += self.SPEED
            self.Y += self.SPEED
            if self.BALL_RECT.colliderect(m_platform.main_platform) and m_platform.main_platform.y + 10 >= self.BALL_RECT.y + self.BALL_RECT.height and self.PLATFORM_MOVE_RIGHT == True:
                m_sound.platfotm_and_edges_sound.play()
                self.MOVE_RIGHT_BOT = False
                self.MOVE_RIGHT_TOP = True
            elif self.BALL_RECT.colliderect(m_platform.main_platform) and m_platform.main_platform.y + 10 >= self.BALL_RECT.y + self.BALL_RECT.height and self.PLATFORM_MOVE_LEFT == True:
                m_sound.platfotm_and_edges_sound.play()
                self.MOVE_RIGHT_BOT = False
                self.MOVE_LEFT_TOP = True
            elif self.BALL_RECT.colliderect(m_platform.main_platform) and m_platform.main_platform.y + 10 >= self.BALL_RECT.y + self.BALL_RECT.height and self.PLATFORM_NOT_MOVING == True:
                m_sound.platfotm_and_edges_sound.play()
                self.MOVE_RIGHT_BOT = False
                self.MOVE_RIGHT_TOP = True
            elif self.X + self.WIDTH == m_settings.screen_width:
                self.MOVE_RIGHT_BOT = False
                self.MOVE_LEFT_BOT = True


ball_1 = Ball(x= 385, y= 600, width= 30, height= 30, name_image= m_settings.ball_path)