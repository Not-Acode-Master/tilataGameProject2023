import pygame

class mainMenu():
    def __init__ (self, playing, mainMenuState, surface, color, logo, startButton, quitButton, setting_button, back_button, 
                  bg_image, settingBg_image, screen_height, screen_width, scale):
        self.playing = playing
        self.menu_state = mainMenuState
        self.surface = surface
        self.color = color
        self.start_button = startButton
        self.quit_button = quitButton
        self.settings_button = setting_button
        self.back_button = back_button
        self.logo = logo
        self.bg_image = bg_image
        self.settingBg = settingBg_image
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.scale = scale
        
    def update(self, runBool, clicked):
        self.clicked = clicked
        self.runBool = runBool
        if self.playing == False:
            scaled_bg = pygame.transform.scale(self.bg_image, (self.screen_width, self.screen_height))
            scaled_logo = pygame.transform.scale(self.logo, (int(self.screen_width * self.scale), int(self.screen_height * self.scale)))
            if self.menu_state == "Main":
                self.surface.blit(scaled_bg, (0, 0))
                self.surface.blit(scaled_logo, (self.screen_width / 2 - scaled_logo.get_width() / 2, 0))
                if self.start_button.draw(self.surface) and self.clicked == False:
                    self.playing = True
                    self.clicked = True
                elif self.quit_button.draw(self.surface) and self.clicked == False:
                    self.runBool = False
                    self.clicked = True
                elif self.settings_button.draw(self.surface) and self.clicked == False:
                    self.menu_state = "Settings"
                    self.clicked = True
            elif self.menu_state == "Settings":
                scaledSettingBg = pygame.transform.scale(self.settingBg, (self.screen_width, self.screen_height))
                self.surface.blit(scaledSettingBg, (0, 0))
                if self.back_button.draw(self.surface) and self.clicked == False:
                    self.menu_state = "Main"
                    self.clicked = True
            
    