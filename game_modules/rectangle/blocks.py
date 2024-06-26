import pygame
import game_modules.main_ball.main_ball as m_ball
import game_modules.main_screen as m_screen
import game_modules.sounds.sounds as m_sound
import game_modules.victory_defeat_text.draw_text as m_text
import game_modules.rectangle.main_platform as m_platform
import game_modules.score_board.score_board as m_board
import game_modules.timer.timer as m_time
import game_modules.menu.buttons as m_button


block_x = 30
block_y = 50
block_width = 75.5
block_height = 20
block_rgb = (125, 0, 225)

block_cords = []

for y_row in range(4):
    for x_row in range(8):
        block_cords.append([block_x, block_y])
        block_x += 95.5
    block_y += 50
    block_x = 30

hit_counter = 0

is_sound = False

victory = False


def place_blocks():
    global hit_counter
    for cord in block_cords:
        block = pygame.Rect(cord[0], cord[1], block_width, block_height)
        pygame.draw.rect(m_screen.screen, block_rgb, block)
        if m_ball.ball_1.BALL_RECT.colliderect(block):
            m_board.score += 5
            m_sound.platfotm_blocks_sound.play()
            hit_counter += 1
            cord[0] = -100
            if m_ball.ball_1.MOVE_LEFT_BOT == True:
                if m_ball.ball_1.BALL_RECT.y - m_ball.ball_1.BALL_RECT.height < block.y and m_ball.ball_1.BALL_RECT.x + 15 > block.x + block.width:
                    m_ball.ball_1.MOVE_LEFT_BOT = False
                    m_ball.ball_1.MOVE_RIGHT_BOT = True
                elif m_ball.ball_1.BALL_RECT.y < block.y:
                    m_ball.ball_1.MOVE_LEFT_BOT = False
                    m_ball.ball_1.MOVE_LEFT_TOP = True

            elif m_ball.ball_1.MOVE_RIGHT_BOT == True:
                if m_ball.ball_1.BALL_RECT.y - m_ball.ball_1.BALL_RECT.height < block.y and m_ball.ball_1.BALL_RECT.x + 15 < block.x:
                    m_ball.ball_1.MOVE_RIGHT_BOT = False
                    m_ball.ball_1.MOVE_LEFT_BOT = True
                elif m_ball.ball_1.BALL_RECT.y < block.y:
                    m_ball.ball_1.MOVE_RIGHT_BOT = False
                    m_ball.ball_1.MOVE_RIGHT_TOP = True

            elif m_ball.ball_1.MOVE_LEFT_TOP == True:
                if m_ball.ball_1.BALL_RECT.y < block.y:
                    m_ball.ball_1.MOVE_LEFT_TOP = False
                    m_ball.ball_1.MOVE_RIGHT_TOP = True
                elif m_ball.ball_1.BALL_RECT.y > block.y:
                    m_ball.ball_1.MOVE_LEFT_TOP = False
                    m_ball.ball_1.MOVE_LEFT_BOT = True
                
            elif m_ball.ball_1.MOVE_RIGHT_TOP == True:
                if m_ball.ball_1.BALL_RECT.y < block.y:
                    m_ball.ball_1.MOVE_RIGHT_TOP = False
                    m_ball.ball_1.MOVE_LEFT_TOP = True
                elif m_ball.ball_1.BALL_RECT.y > block.y:
                    m_ball.ball_1.MOVE_RIGHT_TOP = False
                    m_ball.ball_1.MOVE_RIGHT_BOT = True
    
def show_defeat():
    global victory
    if m_ball.ball_1.BALL_RECT.y > m_platform.main_platform.y + m_platform.rect_height and victory == False:
        m_screen.screen.blit(source= m_text.text_defeat, dest= m_text.defeat_cord_tuple)
        m_time.timer_stop = True
        if m_ball.ball_1.BALL_RECT.y > m_platform.main_platform.y + m_platform.rect_height and m_ball.ball_1.BALL_RECT.y < 700:
            m_sound.defeat_sound.play()

def show_victory():
    global victory
    global hit_counter
    global is_sound
    if hit_counter == 32:
        m_time.timer_stop = True
        victory = True
        m_screen.screen.blit(source= m_text.text_victory, dest= m_text.victory_cord_tuple)
        if is_sound == False:
            m_sound.victory_sound.play()
            is_sound = True




        