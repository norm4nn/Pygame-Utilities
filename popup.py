import pygame
from pygame.rect import Rect
import os.path

POPUP_IMG = pygame.image.load(os.path.join('PygUtilities', 'assets', 'popup.png'))
CLOSE_BOX_IMG = pygame.image.load(os.path.join('PygUtilities', 'assets', 'close_box.png'))
CLOSE_BOX_SIZE = (32, 32)

class Popup(Rect):
    def __init__(self, *args, **kwargs):
        super(Popup, self).__init__(*args, **kwargs)
        self.content = []
        # if kwargs['content']:
        #     self.content = kwargs['content']
        self.opened = False
        self.popup_img = pygame.transform.scale(POPUP_IMG, (self.width, self.height))
        self.close_box_img = pygame.transform.scale(CLOSE_BOX_IMG, CLOSE_BOX_SIZE)
        self.close_box_pos = (self.x + int((7/8)*self.width), self.y - CLOSE_BOX_SIZE[0]//2)
        self.close_box_rect = pygame.Rect(self.close_box_pos[0], self.close_box_pos[1],
                                          CLOSE_BOX_SIZE[0], CLOSE_BOX_SIZE[1])

    def draw(self, window):
        if self.opened:
            window.blit(self.popup_img, Rect(self.x, self.y, self.width, self.height))
            window.blit(self.close_box_img, self.close_box_rect)
            for box in self.content:
                box.draw(window)


    def box_clicked(self, rect_x, rect_y, rect_width, rect_height, mouse_pos):
        if mouse_pos[0] >= rect_x and mouse_pos[0] <= rect_x + rect_width:
            if mouse_pos[1] >= rect_y and mouse_pos[1] <= rect_y + rect_height:
                return True
        return False

    def clicked(self, mouse_pos):
        if self.box_clicked(self.close_box_rect.x, self.close_box_rect.y,
                                  self.close_box_rect.width, self.close_box_rect.height,mouse_pos):#close box clicked
            self.opened = False
        for box in self.content:
            if box.clicked(mouse_pos):
                box.action()

