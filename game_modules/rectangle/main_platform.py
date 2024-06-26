import pygame
import game_modules.__settings__ as m_settings
import game_modules.main_ball.main_ball as m_ball



rect_x = 345
rect_y = 650
rect_width = 110
rect_height = 15
rect_rgb = (130, 255, 100)

rect_speed_x = 15

main_platform = pygame.Rect(rect_x, rect_y, rect_width, rect_height)


def move_right(screen: object):
    event_pressed = pygame.key.get_pressed()
    if event_pressed[pygame.K_RIGHT] == True and main_platform.x + rect_width < m_settings.screen_width:
        m_ball.ball_1.PLATFORM_MOVE_RIGHT = True
        m_ball.ball_1.PLATFORM_MOVE_LEFT = False
        m_ball.ball_1.PLATFORM_NOT_MOVING = False
        main_platform.x += rect_speed_x
    elif event_pressed[pygame.K_LEFT] == False and event_pressed[pygame.K_RIGHT] == False:
        m_ball.ball_1.PLATFORM_NOT_MOVING = True
        m_ball.ball_1.PLATFORM_MOVE_RIGHT = False
        m_ball.ball_1.PLATFORM_MOVE_LEFT = False

def move_left(screen: object):
    event_pressed = pygame.key.get_pressed()
    if event_pressed[pygame.K_LEFT] == True and main_platform.x > 0:
        m_ball.ball_1.PLATFORM_MOVE_LEFT = True
        m_ball.ball_1.PLATFORM_MOVE_RIGHT = False
        m_ball.ball_1.PLATFORM_NOT_MOVING = False
        main_platform.x -= rect_speed_x
    elif event_pressed[pygame.K_RIGHT] == False and event_pressed[pygame.K_LEFT] == False:
        m_ball.ball_1.PLATFORM_NOT_MOVING = True
        m_ball.ball_1.PLATFORM_MOVE_RIGHT = False
        m_ball.ball_1.PLATFORM_MOVE_LEFT = False




