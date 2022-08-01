import pygame
from pygame.rect import Rect
import os.path

BLANK_IMAGE = pygame.image.load(os.path.join('PygUtilities','assets','checkbox_blank.png'))
CHECKED_IMAGE = pygame.image.load(os.path.join('PygUtilities', 'assets', 'checkbox_checked.png'))




class CheckBox(Rect):
    def __init__(self,*args):
        super(CheckBox, self).__init__(*args)
        self.blank_img =  pygame.transform.scale(BLANK_IMAGE, (self.width, self.height))
        self.checked_img = pygame.transform.scale(CHECKED_IMAGE, (self.width, self.height))
        self.current_img = self.blank_img
        self.isChecked = False


    def clicked(self):
        self.isChecked = not self.isChecked
        if self.isChecked:
            self.current_img = self.checked_img
        else:
            self.current_img = self.blank_img

    def getState(self):
        return self.isChecked

    def draw(self, window):
        window.blit(self.current_img, Rect(self.x, self.y, self.width, self.height))

    def isClicked(self, mouse_pos):
        if mouse_pos[0] >= self.x and mouse_pos[0] <= self.x + self.width and mouse_pos[1] >= self.y and mouse_pos[1] <= self.y + self.height:
            self.clicked()
            return True

        return False



