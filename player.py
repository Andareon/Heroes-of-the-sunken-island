from pygame import *
import pygame

class Player1(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.backpack = [0] * 4 + [5] + [0]
        self.maxweight = 25
        self.image = image.load("Image/Player/1.png")
        self.actimage = image.load("Image/Player/A1.png")
        self.image_size = self.image.get_rect().size
        self.x = x
        self.y = y
        self.rect = (61 * x + 1 + 9, 61 * y + 15 + 1, 60, 3)
        self.direct = [[-1, 0],
                       [1, 0],
                       [0, -1],
                       [0, 1]]
        self.drain = [[-1, 0],
                       [1, 0],
                       [0, -1],
                       [0, 1]]
        self.distanse = 3
        self.can = self.distanse
        self.cantgo = [1, 2]
        self.swap = [[-1, -1],
                     [-1, 0],
                     [-1, 1],
                     [0, -1],
                     [0, 1],
                     [1, -1],
                     [1, 0],
                     [1, 1]]
    
    def draw(self, screen, active):
        if active:
            screen.blit(self.actimage, ((61 * self.x + 1 + 30 - self.image_size[0] // 2) - 2,(61 * self.y + 1 + 30 - self.image_size[1] // 2) - 2))
        else:
            screen.blit(self.image, ((61 * self.x + 1 + 30 - self.image_size[0] // 2),(61 * self.y + 1 + 30 - self.image_size[1] // 2)))


class Player2(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.backpack = [0] * 4 + [5] + [0]
        self.maxweight = 20
        self.image = image.load("Image/Player/2.png")
        self.actimage = image.load("Image/Player/A2.png")
        self.image_size = self.image.get_rect().size
        self.x = x
        self.y = y
        self.rect = (61 * x + 1 + 9, 61 * y + 15 + 1, 60, 3)
        self.direct = [[-1, 0],
                       [1, 0],
                       [0, -1],
                       [0, 1],
                       [-1, -1],
                       [-1, 1],
                       [1, -1],
                       [1, 1]]
        self.drain = [[-1, 0],
                       [1, 0],
                       [0, -1],
                       [0, 1],
                       [-1, -1],
                       [-1, 1],
                       [1, -1],
                       [1, 1]]
        self.distanse = 3
        self.can = self.distanse
        self.cantgo = [1, 2]
        self.swap = [[-1, -1],
                     [-1, 0],
                     [-1, 1],
                     [0, -1],
                     [0, 1],
                     [1, -1],
                     [1, 0],
                     [1, 1]]
    
    def draw(self, screen, active):
        if active:
            screen.blit(self.actimage, ((61 * self.x + 1 + 30 - self.image_size[0] // 2) - 2,(61 * self.y + 1 + 30 - self.image_size[1] // 2) - 2))
        else:
            screen.blit(self.image, ((61 * self.x + 1 + 30 - self.image_size[0] // 2),(61 * self.y + 1 + 30 - self.image_size[1] // 2)))