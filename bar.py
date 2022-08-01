import pygame
from pygame.rect import Rect
import os.path

pygame.font.init()

LAYOUT_IMG = pygame.image.load(os.path.join('PygUtilities', 'assets', 'bar_layout.png'))
BASIC_LAYOUT_SIZE_PX = (48, 16)
BASIC_BAR_POSITION_PX = (13, 2)
BASIC_BAR_SIZE_PX = (32, 6)
FONT_SIZE = 8
FONT_SIZE_SMALL = 4
FONT = pygame.font.Font(os.path.join('PygUtilities', 'assets', 'ARCADECLASSIC.TTF'), FONT_SIZE)
FONT_SMALL = pygame.font.Font(os.path.join('PygUtilities', 'assets', 'ARCADECLASSIC.TTF'), FONT_SIZE_SMALL)



class Bar(Rect):
    def __init__(self, *args, **kwargs):
        super(Bar, self).__init__(*args, **kwargs)
        self.scale = kwargs['scale']
        self.width = BASIC_LAYOUT_SIZE_PX[0]*self.scale
        self.height = BASIC_LAYOUT_SIZE_PX[1]*self.scale

        self.font_size = int(FONT_SIZE*self.scale)
        self.font_size_small = int(FONT_SIZE_SMALL*self.scale)
        self.font = pygame.font.Font(os.path.join('PygUtilities', 'assets', 'ARCADECLASSIC.TTF'), self.font_size)
        self.font_small = pygame.font.Font(os.path.join('PygUtilities', 'assets', 'ARCADECLASSIC.TTF'), self.font_size_small)

        self.bar_color = kwargs['color']
        self.value = kwargs['cap']
        self.value_cap = kwargs['cap']
        self.value_surface = self.font_small.render(str(self.value) + '  !' + str(self.value_cap), False, (0,0,0))

        self.name_txt = kwargs['name'][:2]
        self.name_surface = self.font.render(self.name_txt, False, (0, 0, 0))

        self.layout_img = pygame.transform.scale(LAYOUT_IMG, (self.width, self.height))
        self.bar_pos = (self.x + BASIC_BAR_POSITION_PX[0] * self.scale,
                        self.y + BASIC_BAR_POSITION_PX[1] * self.scale)

        self.bar_size = (BASIC_BAR_SIZE_PX[0] * self.scale,
                         BASIC_BAR_SIZE_PX[1] * self.scale)


        self.bar_rect = pygame.Rect(self.bar_pos[0], self.bar_pos[1], self.bar_size[0], self.bar_size[1])

    def draw(self, window):
        window.blit(self.layout_img, Rect(self.x, self.y, self.width, self.height))
        pygame.draw.rect(window, self.bar_color, self.bar_rect)
        window.blit(self.name_surface, (self.x+2*self.scale, self.y+1*self.scale))
        window.blit(self.value_surface, (self.x+3*self.scale, self.y + 10*self.scale))

    def change_value(self, change):
        self.value += change
        if self.value < 0:
            self.value = 0
        elif self.value > self.value_cap:
            self.value = self.value_cap

        modifier = self.value / self.value_cap

        new_len = self.bar_size[0] * modifier
        self.bar_rect.width = new_len
        self.value_surface = self.font_small.render(str(self.value) + '  !' + str(self.value_cap), False, (0, 0, 0))


