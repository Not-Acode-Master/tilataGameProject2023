import pygame

class displaytext():
    def __init__(self, surface, text, pos, font, color):
        self.surface = surface
        self.text = text
        self.pos = pos
        self.font = font
        self.color = color
        
    def display(self):
        collection = [word.split(' ') for word in self.text.splitlines()]
        space = self.font.size(' ')[0]
        x,y = self.pos
        for lines in collection:
            for words in lines:
                word_surface = self.font.render(words, True, self.color)
                word_width , word_height = word_surface.get_size()
                if x + word_width >= 800:
                    x = self.pos[0]
                    y += word_height
                self.surface.blit(word_surface, (x,y))
                x += word_width + space
            x = self.pos[0]
            y += word_height