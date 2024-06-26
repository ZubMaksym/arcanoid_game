import pygame
import game_modules.main_screen as m_screen
import game_modules.__settings__ as m_settings
import game_modules.load_file.load_images as m_image
import game_modules.rectangle.main_platform as m_rect
import game_modules.rectangle.blocks as m_block
import game_modules.main_ball.main_ball as m_ball
import game_modules.timer.timer as m_time
import game_modules.score_board.score_board as m_board
import game_modules.menu.buttons as m_button
import game_modules.victory_defeat_text.draw_text as m_text



pygame.init()

game = True

def start_game():
    global game

    while game:

        if m_button.start_button.IS_GAME_STARTED == False:
            m_screen.screen.blit(source= m_image.load_bg_image(name_file= m_settings.bg_path), dest= (0,0))
            m_button.start_button.show_image(name_screen= m_screen.screen)
            m_button.exit_button.show_image(name_screen= m_screen.screen)
            m_button.start_button.button_pressed()
            m_screen.screen.blit(source= m_text.title_text, dest= m_text.main_title_cord_tuple)
            m_screen.screen.blit(source= m_text.title_lower_text, dest= m_text.lower_title_cord_tuple)
        else:
            m_settings.FPS.tick(60)
            m_screen.screen.blit(source= m_image.load_bg_image(name_file= m_settings.bg_path), dest= (0,0))
            m_ball.ball_1.show_image(name_screen= m_screen.screen)
            m_ball.ball_1.move_ball()
            pygame.draw.rect(m_screen.screen, m_rect.rect_rgb, m_rect.main_platform)
            m_block.place_blocks()
            m_rect.move_left(m_screen.screen)
            m_rect.move_right(m_screen.screen)
            m_time.count_time()
            m_board.count_score()
            m_block.show_victory()       
            m_block.show_defeat()
            m_time.count_time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        
        pygame.display.flip()


