import pygame
import game_modules.main_screen as m_screen
import time


timer_font = pygame.font.SysFont('bahnschrift', 40)
timer_color = (255, 0, 0)

clock = pygame.time.Clock()

timer_stop = False
finish_time = 0

def count_time():
    global timer_stop
    global finish_time
    if timer_stop == False:
        start_ticks = pygame.time.get_ticks()
        time_in_sec = start_ticks * 10**-3
        text_time_sec = timer_font.render(f"Time: {int(time_in_sec)}s", True, timer_color)
        time_cord_tuple = (15, 750)
        finish_time = time_in_sec
        m_screen.screen.blit(source= text_time_sec, dest= time_cord_tuple)
    else:
        time_cord_tuple = (15, 750)
        finish_time_sec = timer_font.render(f"Time: {int(finish_time)}s", True, timer_color)
        m_screen.screen.blit(source= finish_time_sec, dest= time_cord_tuple)


