import pygame

class pauseMenu():
    def __init__(self, paused):
        self.paused = paused
    
    def aditionalControls(self):
        key = pygame.key.get_pressed()
        
        if key [pygame.K_p]:
            self.paused = not self.paused
        
    def update(self):
        if self.paused == True:
            print("Paused")
        else:
            print("Playing")