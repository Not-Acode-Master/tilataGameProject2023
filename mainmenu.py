import pygame

class mainMenu():
    def __init__ (self, playing, mainMenuState, surface, color, logo, startButton, quitButton, bg_image, screen_height, screen_width, scale):
        self.playing = playing
        self.menu_state = mainMenuState
        self.surface = surface
        self.color = color
        self.start_button = startButton
        self.quit_button = quitButton
        self.logo = logo
        self.bg_image = bg_image
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.scale = scale
        
    def update(self, runBool):
        self.runBool = runBool
        if self.playing == False:
            scaled_bg = pygame.transform.scale(self.bg_image, (self.screen_width, self.screen_height))
            self.surface.blit(scaled_bg, (0, 0))
            scaled_logo = pygame.transform.scale(self.logo, (int(self.screen_width * self.scale), int(self.screen_height * self.scale)))
            self.surface.blit(scaled_logo, (self.screen_width / 2 - scaled_logo.get_width() / 2, 0))
            if self.menu_state == "Main":
                if self.start_button.draw(self.surface):
                    self.playing = True
                if self.quit_button.draw(self.surface):
                    self.runBool = False
            
    