import pygame
import webbrowser 

class mainMenu():
    def __init__ (self, playing, mainMenuState, surface, color, logo, startButton, quitButton, setting_button, back_button, github_button, contrls_button, back_button_settings,
                  char1_button, char2_button, bg_image, settingBg_image, keys_spritesheet_img, button_fx, screen_height, screen_width, scale):
        self.playing = playing
        self.menu_state = mainMenuState
        self.surface = surface
        self.color = color
        self.start_button = startButton
        self.quit_button = quitButton
        self.settings_button = setting_button
        self.back_button = back_button
        self.github_button = github_button
        self.controls_button = contrls_button
        self.back_button_settings = back_button_settings
        self.logo = logo
        self.bg_image = bg_image
        self.settingBg = settingBg_image
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.char1_button = char1_button
        self.char2_button = char2_button
        self.scale = scale
        self.key_list = self.upload_key_images(keys_spritesheet_img, 2.5)
        self.ORANGE = (255, 153, 8)
        self.WHITE = (255, 255, 255)
        self.button_fx = button_fx
        self.charIndex = 0
    
    def upload_key_images (self, sprite_sheet, scale):
        key_list = []
        for i in range(6):
            dynamic_list = []
            for j in range(7):
                temp_img = sprite_sheet.subsurface(j*32, i*32, 32, 32)
                dynamic_list.append(pygame.transform.scale(temp_img, (32 * scale, 32 * scale)))
            key_list.append(dynamic_list)
        return key_list
        
    def update(self, runBool, clicked, font):
        self.clicked = clicked
        self.runBool = runBool
        
        if self.playing == False:
            scaled_bg = pygame.transform.scale(self.bg_image, (self.screen_width, self.screen_height))
            scaled_logo = pygame.transform.scale(self.logo, (int(self.screen_width * self.scale), int(self.screen_height * self.scale)))
            if self.menu_state == "Main":
                self.surface.blit(scaled_bg, (0, 0))
                self.surface.blit(scaled_logo, (self.screen_width / 2 - scaled_logo.get_width() / 2, 0))
                if self.start_button.draw(self.surface) and self.clicked == False:
                    #self.playing = True
                    self.menu_state = "EnemySelection"
                    self.button_fx.play()
                    self.clicked = True
                elif self.settings_button.draw(self.surface) and self.clicked == False:
                    self.menu_state = "Settings"
                    self.button_fx.play()
                    self.clicked = True
                elif self.quit_button.draw(self.surface) and self.clicked == False:
                    self.runBool = False
                    self.button_fx.play()
                    self.clicked = True
            
            elif self.menu_state == "EnemySelection":
                scaledSettingBg = pygame.transform.scale(self.settingBg, (self.screen_width, self.screen_height))
                self.surface.blit(scaledSettingBg, (0, 0))
                if self.char1_button.draw(self.surface) and self.clicked == False:
                    self.playing = True
                    self.button_fx.play()
                    self.clicked = True
                    self.charIndex = 1
                elif self.char2_button.draw(self.surface) and self.clicked == False:
                    self.playing = True
                    self.button_fx.play()
                    self.clicked = True
                    self.charIndex = 2
                    
            elif self.menu_state == "Settings":
                scaledSettingBg = pygame.transform.scale(self.settingBg, (self.screen_width, self.screen_height))
                self.surface.blit(scaledSettingBg, (0, 0))
                self.draw_text("Settings", font, self.WHITE, self.screen_width/2 - 120, 0, self.surface)
                if self.github_button.draw(self.surface) and self.clicked == False:
                    webbrowser.open_new_tab('https://github.com/Not-Acode-Master/tilataGameProject2023')
                    self.button_fx.play()
                    self.clicked = True
                elif self.controls_button.draw(self.surface) and self.clicked == False:
                    self.menu_state = "Controls"
                    self.button_fx.play()
                    self.clicked = True
                elif self.back_button.draw(self.surface) and self.clicked == False:
                    self.menu_state = "Main"
                    self.button_fx.play()
                    self.clicked = True
                    
            elif self.menu_state == "Controls":
                scaledSettingBg = pygame.transform.scale(self.settingBg, (self.screen_width, self.screen_height))
                self.surface.blit(scaledSettingBg, (0, 0))
                self.draw_text("Controls", font, self.WHITE, self.screen_width/2 - 120, 0, self.surface)
                self.draw_text("Player 1", font, self.WHITE, self.screen_width / 4 - 100, 460, self.surface)
                self.draw_text("Player 2", font, self.WHITE, self.screen_width / 4 * 3 - 100, 460, self.surface)
                
                self.blitKeycaps(font, 20, 650)
                if self.back_button_settings.draw(self.surface) and self.clicked == False:
                    self.menu_state = "Settings"
                    self.button_fx.play()
                    self.clicked = True
                    
    def draw_text(self, text, font, text_col, x, y, surface):
        img = font.render(text, True, text_col)
        surface.blit(img, (x, y))
        
    def blitKeycaps(self, font, xCoord, xCoord2):
        keyCoords = [[4, 3], [1, 2], [3, 6], [4, 4], [1, 4]]
        keyCoords1 = [[2, 3], [2, 4], [2, 6], [0, 0], [0, 1]]
        keyText = ["JUMP", "LEFT", "RIGHT", "ATTACK 1", "ATTACK 2"]
        for i in range(5):
            self.draw(xCoord, i*70 + 50, self.key_list[keyCoords[i][0]][keyCoords[i][1]], self.surface)
            self.draw_text(keyText[i], font, self.ORANGE, xCoord + 90 , i*70 + 50, self.surface)
            self.draw(xCoord2, i*70 + 50, self.key_list[keyCoords1[i][0]][keyCoords1[i][1]], self.surface)
            self.draw_text(keyText[i], font, self.ORANGE, xCoord2 + 90 , i*70 + 50, self.surface)
        
        
    
    def draw(self, x, y, img, surface):
        surface.blit(img, (x, y))
                
            
    