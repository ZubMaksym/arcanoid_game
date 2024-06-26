import pygame
import game_modules.main_screen as m_screen


scoreboard_font = pygame.font.SysFont('bahnschrift', 40)
scoreboard_color = (255, 255, 0)
time_cord_tuple = (200, 750)

score = 0

def count_score():
    global score
    scoreboard_text = scoreboard_font.render(f"Score: {score}", True, scoreboard_color)
    m_screen.screen.blit(source= scoreboard_text, dest= time_cord_tuple)