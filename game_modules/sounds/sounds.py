import pygame
import game_modules.__search_abs_path__ as m_abs_path


platfotm_and_edges_sound = pygame.mixer.Sound(m_abs_path.search_abs_path("game_modules/sounds/platform_and_screen_track.mp3"))

platfotm_blocks_sound = pygame.mixer.Sound(m_abs_path.search_abs_path("game_modules/sounds/block_track.mp3"))

victory_sound = pygame.mixer.Sound(m_abs_path.search_abs_path("game_modules/sounds/victory_track.mp3"))

defeat_sound = pygame.mixer.Sound(m_abs_path.search_abs_path("game_modules/sounds/defeat_track.mp3"))

platfotm_and_edges_sound.set_volume(0.1)
platfotm_blocks_sound.set_volume(0.1)
victory_sound.set_volume(0.1)
defeat_sound.set_volume(0.1)
