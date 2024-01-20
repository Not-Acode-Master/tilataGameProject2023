import pygame

class pauseMenu():
    def __init__(self, paused, screen_color, surface, play_button, quit_button, image, screen_width, screen_height, pauseText):
        self.paused = paused
        self.screen_color = screen_color
        self.surface = surface
        self.play_button = play_button
        self.quit_button = quit_button
        self.image = image
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.pauseText = pauseText
        
    def update(self, runt):
        self.runt = runt
        if self.paused == True:
            scaled_bg = pygame.transform.scale(self.image, (self.screen_width, self.screen_height))
            self.surface.blit(scaled_bg, (0, 0))
            self.surface.blit(self.pauseText, (self.screen_width / 2 - self.pauseText.get_width() / 2, 0))
            if self.play_button.draw(self.surface):
                self.paused = not self.paused
            elif self.quit_button.draw(self.surface):
                self.runt = False