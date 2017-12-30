import pygame
from math import ceil


class Button:
    def __init__(self, surface: object, color: object, x: object, y: object, height: object, width: object, text: object, text_color: object, bd: object, font: object) -> object:
        self.surface = surface
        self.color = color
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.text = text
        self.text_color = text_color
        self.bd = bd
        self.font = font
        self.pressed = False
        self.active = True

    def draw(self):
        # Заполнение
        col = [(255, 255, 255), (0, 0, 0)]
        if self.pressed and self.active:
            col = col[::-1]

        bl = pygame.Surface((self.width + 2, self.height + 2))  # the size of your rect
        bl.fill((0, 0, 0))  # this fills the entire surface
        self.surface.blit(bl, (self.x - 1, self.y - 1))

        fill = pygame.Surface((self.width, self.height))  # the size of your rect
        fill.fill([self.color, (200, 200, 200)][not self.active])  # this fills the entire surface
        self.surface.blit(fill, (self.x, self.y))

        # Frame
        up_fr = pygame.Surface((self.width - self.bd, self.bd))
        up_fr.set_alpha(120)
        up_fr.fill(col[0])
        self.surface.blit(up_fr, (self.x, self.y))

        lt_fr = pygame.Surface((self.bd, self.height - 2 * self.bd))
        lt_fr.set_alpha(120)
        lt_fr.fill(col[0])
        self.surface.blit(lt_fr, (self.x, self.y + self.bd))

        rt_fr = pygame.Surface((self.bd, self.height - 2 * self.bd))
        rt_fr.set_alpha(120)
        rt_fr.fill(col[1])
        self.surface.blit(rt_fr, (self.x + self.width - self.bd, self.y + self.bd))

        dn_fr = pygame.Surface((self.width - self.bd, self.bd))
        dn_fr.set_alpha(120)
        dn_fr.fill(col[1])
        self.surface.blit(dn_fr, (self.x + self.bd, self.y + self.height - self.bd))

        for x in range(self.bd):
            for y in range(self.bd):
                on = pygame.Surface((1, 1))
                on.set_alpha(120)
                if x < self.bd - y:
                    on.fill(col[0])
                else:
                    on.fill(col[1])
                self.surface.blit(on, (self.x + x, self.y + self.height - self.bd + y))
                self.surface.blit(on, (self.x + self.width - self.bd + x, self.y + y))

        # if not self.active:
        #     ac = pygame.Surface((self.width, self.height))
        #     ac.set_alpha(120)
        #     ac.fill((200, 200, 200))
        #     self.surface.blit(ac, (self.x, self.y))

        # Текст
        text = self.font.render(self.text, 1, self.text_color)
        if self.active and self.pressed:
            text_rect = text.get_rect(
                center=(self.x + self.width / 2 + ceil(self.bd / 2), self.y + self.height / 2 + ceil(self.bd / 2)))
        else:
            text_rect = text.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
        self.surface.blit(text, text_rect)

    def update(self, mouse):
        self.pressed = self.x <= mouse[0] <= self.x + self.width and self.y <= mouse[1] <= self.y + self.height
