import pygame

class pauseMenu():
    def __init__(self, paused, screen_color, surface, play_button, quit_button):
        self.paused = paused
        self.screen_color = screen_color
        self.surface = surface
        self.play_button = play_button
        self.quit_button = quit_button
        
    def update(self, runt):
        self.runt = runt
        if self.paused == True:
            self.surface.fill(self.screen_color)
            if self.play_button.draw(self.surface):
                self.paused = not self.paused
            elif self.quit_button.draw(self.surface):
                self.runt = False