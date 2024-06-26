import pygame
import game_modules.__settings__ as m_settings
import game_modules.main_screen as m_screen


rect_x = 345
rect_y = 650
rect_width = 110
rect_height = 20
rect_rgb = (130, 255, 100)

rect_speed_x = 10

# purple 125,0,225
rect_1 = pygame.Rect(rect_x, rect_y, rect_width, rect_height)


def move_right(screen: object):
    global rect_x
    event_pressed = pygame.key.get_pressed()
    if event_pressed[pygame.K_RIGHT] == True and rect_x + rect_width <= m_settings.screen_width:
        rect_x += rect_speed_x
        pygame.Rect.move_ip(rect_1, rect_speed_x, 0)

        
def move_left(screen: object):
    global rect_x
    event_pressed = pygame.key.get_pressed()
    if event_pressed[pygame.K_LEFT] == True and rect_x > 0:
        rect_x -= rect_speed_x
        pygame.Rect.move_ip(rect_1, -rect_speed_x, 0)






     
