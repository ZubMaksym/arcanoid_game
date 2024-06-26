import pygame
import game_modules.run_game as m_game
import game_modules.__search_abs_path__ as m_path


exit_image= "game_modules/menu/exit_btn.png"
start_image ="game_modules/menu/start_btn.png"

class Button():
    def __init__(self, x: int, y: int, width: int, height: int, name_image: str):
        self.X = x
        self.Y = y
        self.WIDTH = width
        self.HEIGHT = height
        self.NAME_IMAGE = name_image
        self.IMAGE = None
        self.START_BUTTON_RECT = None
        self.EXIT_BUTTON_RECT = None
        self.IS_GAME_STARTED = False

        self.load_image()

    def load_image(self):
        image_path = m_path.search_abs_path(file_name= self.NAME_IMAGE)
        image_load = pygame.image.load(image_path)
        self.IMAGE = pygame.transform.scale(surface= image_load, size= (self.WIDTH, self.HEIGHT))
        self.START_BUTTON_RECT = pygame.Rect(self.X, self.Y, self.WIDTH, self.HEIGHT)
        self.EXIT_BUTTON_RECT = pygame.Rect(self.X, self.Y + 150, self.WIDTH, self.HEIGHT)
        self.RESTART_BUTTON_RECT = pygame.Rect(self.X, self.Y, self.WIDTH, self.HEIGHT)
        
    def show_image(self, name_screen: object):
        name_screen.blit(source= self.IMAGE, dest= (self.X, self.Y))

    def button_pressed(self):
        self.START_BUTTON_RECT.x = self.X
        self.START_BUTTON_RECT.y = self.Y
        pos = pygame.mouse.get_pos()
        if self.START_BUTTON_RECT.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                self.IS_GAME_STARTED = True
        if self.EXIT_BUTTON_RECT.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                m_game.game = False
                                

start_button = Button(x= 300, y= 350, width= 200, height= 80, name_image= start_image)

exit_button = Button(x= 300, y= 500, width= 200, height= 80, name_image= exit_image)


        





