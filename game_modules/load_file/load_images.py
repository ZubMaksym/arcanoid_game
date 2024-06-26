import pygame
import game_modules.__search_abs_path__ as m_path
import game_modules.__settings__ as m_settings


pygame.init()

def load_bg_image(name_file: str):
    img_path = m_path.search_abs_path(file_name= name_file)
    img_bg_file = pygame.image.load(img_path) 
    img_file_transform = pygame.transform.scale(img_bg_file, (m_settings.screen_width, m_settings.screen_height))
    return img_file_transform
