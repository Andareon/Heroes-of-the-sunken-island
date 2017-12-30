import pygame
from pygame import *


class Slider:
    def __init__(self, surface, x, y, width, height, mn, mx, now, img):
        self.surface = surface
        self.x = x
        self.y = y
        self.image = image.load(img)
        self.width = width
        self.width = width
        self.height = height
        self.min = mn
        self.max = mx
        self.now = now
        if self.max == self.min:
            self.delta = 0
        else:
            self.delta = self.height / (self.max - self.min)
        self.active = False

    def draw(self):
        if self.delta != 0:
            ud = pygame.Surface((self.width, 2))  # the size of your rect
            ud.fill((0, 0, 0))  # this fills the entire surface
            self.surface.blit(ud, (self.x, self.y))
            self.surface.blit(ud, (self.x, self.y + self.height))

            zas = pygame.Surface((self.width // 4, 1))
            zas.fill((0, 0, 0))
            for i in range(self.min + 1, self.max):
                self.surface.blit(zas, (self.x + self.width // 4, self.y + (i - self.min) * self.delta))

            vert = pygame.Surface((2, self.height))  # the size of your rect
            vert.fill((0, 0, 0))  # this fills the entire surface
            self.surface.blit(vert, (self.x + self.width / 2 - 1, self.y))

            self.surface.blit(self.image, (self.x + self.width // 4 + 1, self.y + int(self.delta * self.now) - self.width // 4))
        else:
            ud = pygame.Surface((self.width, 2))  # the size of your rect
            ud.fill((0, 0, 0))  # this fills the entire surface
            self.surface.blit(ud, (self.x, self.y + self.height // 2 - 1))

            self.surface.blit(self.image,
                              (self.x + self.width // 4 + 1, self.y + self.height // 2 - self.width // 4))

        
    def change(self, event):
        if event.type == MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            self.active = self.reag(mouse[0], mouse[1])
            self.update(mouse[0], mouse[1])

        if event.type == MOUSEBUTTONUP:
            self.active = False

        if event.type == MOUSEMOTION:
            mouse = pygame.mouse.get_pos()
            if self.active:
                self.update(mouse[0], mouse[1])


    def update(self, x, y):
        if self.x <= x <= self.x + self.width and self.y - self.width // 4 <= y <= self.y + self.width // 4 + self.height:
            self.now = min(max(round((y - self.y) * (self.max - self.min) / self.height), self.min), self.max)

    def reag(self, x, y):
        return self.x <= x <= self.x + self.width and self.y - self.width // 4 <= y <= self.y + self.width // 4 + self.height