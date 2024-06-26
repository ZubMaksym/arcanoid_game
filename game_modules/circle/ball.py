import pygame
import game_modules.main_screen as m_screen
import game_modules.__settings__ as m_settings
import game_modules.rectangle.main_platform as m_platform


ball_x = 400
ball_y = 635
center = 400
ball_radius = 15
ball_rgb = (255,   0,   0)

ball_move_left_top = False
ball_move_right_top = True
ball_move_left_bot = False
ball_move_right_bot = False

class Ball():
    def __init__(self, surface: object, color: tuple, center: tuple, radius: int):
        self.SURFACE = surface
        self.COLOR = color
        self.CENTER = center
        self.RADIUS = radius

    def create_ball(self):
        pygame.draw.circle(surface= self.SURFACE, color= self.COLOR, center= self.CENTER, radius= self.RADIUS)

ball_1 = Ball(m_screen.screen, color= ball_rgb, center= center, radius= ball_radius)

def move_ball_right_top():
    global ball_y
    global ball_x
    global ball_move_right_top
    global ball_move_left_top
    pygame.draw.circle(surface= m_screen.screen, color= ball_rgb, center= (ball_x, ball_y), radius= ball_radius)
    if ball_y + ball_radius < m_settings.screen_width and ball_x + ball_radius < m_settings.screen_width:
        ball_y -= 5
        ball_x += 5
        print(ball_y)
    if ball_x == m_settings.screen_width - ball_radius:
        ball_move_right_top = False
        ball_move_left_top = True

def move_ball_left_top():
    global ball_y
    global ball_x
    global ball_move_left_top
    global ball_move_left_bot
    pygame.draw.circle(surface= m_screen.screen, color= ball_rgb, center= (ball_x, ball_y), radius= ball_radius)
    if ball_y > ball_radius:
        ball_y -= 5
        ball_x -= 5
        print(ball_y)
    if ball_y == ball_radius:
        ball_move_left_top = False
        ball_move_left_bot = True

def move_ball_left_bot():
    global ball_y
    global ball_x
    global ball_move_left_top
    global ball_move_left_bot
    pygame.draw.circle(surface= m_screen.screen, color= ball_rgb, center= (ball_x, ball_y), radius= ball_radius)
    if ball_x + ball_radius > ball_radius:
        ball_y += 5
        ball_x -= 5
    if ball_x == m_settings.screen_width - ball_radius:
        ball_move_left_top = False
        ball_move_left_bot = True


def move_ball():
    global ball_move_left_top
    global ball_move_right_top
    global ball_move_left_bot
    global ball_move_right_bot

    if ball_move_right_top == True:
        move_ball_right_top()
    elif ball_move_left_top == True:
        move_ball_left_top()
    elif ball_move_left_bot == True:
        move_ball_left_bot()

    



    
    

        



        
    # if ball_y + ball_radius < m_settings.screen_width and ball_x + ball_radius < m_settings.screen_width and is_game_started == False:
    #     is_game_started = False
    #     ball_y -= 5
    #     ball_x += 5
    





# def move_ball():
#     global ball_y
#     if ball_radius + ball_y < m_settings.screen_width: 
#         ball_y += 5
    