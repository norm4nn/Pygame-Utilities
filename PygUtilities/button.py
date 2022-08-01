import pygame
import os.path

BUTTON_IMG_SIZE = (128, 128)
BUTTON_TEXT_SIZE = (128, 32)
BUTTON_IMG_IMG = pygame.image.load(os.path.join('PygUtilities', 'assets', 'popup.png'))
BUTTON_TEXT_IMG = pygame.image.load(os.path.join('PygUtilities', 'assets', 'button_text.png'))
FONT_SIZE = 28
FONT_PATH = os.path.join('PygUtilities', 'assets', 'ARCADECLASSIC.TTF')



class Button:
    def __init__(self, *args, **kwargs):
        self.rect = None
        self.btn_img = None




    def draw(self, window):
        window.blit(self.btn_img, self.rect)

    def action(self):
        pass

    def clicked(self, mouse_pos):
        if mouse_pos[0] >= self.rect.x and mouse_pos[0] <= self.rect.x + self.rect.width:
            if mouse_pos[1] >= self.rect.y and mouse_pos[1] <= self.rect.y + self.rect.height:
                return True
        return False

class Button_image(Button):
    def __init__(self, *args, **kwargs):
        super(Button_image, self).__init__(*args, **kwargs)
        self.rect = pygame.Rect(args[0], args[1], BUTTON_IMG_SIZE[0]*args[2], BUTTON_IMG_SIZE[1]*args[2])
        self.btn_img = pygame.transform.scale(BUTTON_IMG_IMG, (BUTTON_IMG_SIZE[0]*args[2], BUTTON_IMG_SIZE[1]*args[2]))
        self.img = pygame.image.load(kwargs['path2img'])
        self.img = pygame.transform.scale(self.img, (BUTTON_IMG_SIZE[0]*args[2], BUTTON_IMG_SIZE[1]*args[2]))

    def draw(self, window):
        window.blit(self.btn_img, self.rect)
        window.blit(self.btn_img, self.rect)



class Button_text(Button):
    def __init__(self, *args, **kwargs):
        super(Button_text, self).__init__(*args, **kwargs)
        self.rect = pygame.Rect(args[0], args[1], BUTTON_TEXT_SIZE[0] * args[2], BUTTON_TEXT_SIZE[1] * args[2])
        self.btn_img = pygame.transform.scale(BUTTON_TEXT_IMG, (BUTTON_TEXT_SIZE[0] * args[2], BUTTON_TEXT_SIZE[1] * args[2]))
        self.text = kwargs['text']
        self.font_size = FONT_SIZE * args[2]
        while True and self.font_size > 0:
            self.font = pygame.font.Font(FONT_PATH, self.font_size)
            self.text_surface = self.font.render(self.text, False, (0, 0, 0))
            if self.text_surface.get_width() > self.rect.width:
                self.font_size *= 0.9
                self.font_size = int(self.font_size)
            else: break

        if self.font_size == 0:
            self.font_size = 1
            self.font = pygame.font.Font(FONT_PATH, self.font_size)
            self.text_surface = self.font.render(self.text, False, (0, 0, 0))

        self.text_pos = (self.rect.centerx - self.text_surface.get_rect().width//2, self.rect.centery - self.text_surface.get_rect().height//2)

    def draw(self, window):
        window.blit(self.btn_img, self.rect)
        window.blit(self.text_surface, self.text_pos)

