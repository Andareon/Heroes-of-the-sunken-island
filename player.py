from pygame import *
import pygame

class Player1(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.backpack = [0] * 4 + [50] + [0]
        self.image = image.load("Image/Player/1.png")
        self.actimage = image.load("Image/Player/Active1.png")
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
    
    def draw(self, screen, active):
        if active:
            screen.blit(self.actimage, ((61 * self.x + 1 + 30 - self.image_size[0] // 2) - 2,(61 * self.y + 1 + 30 - self.image_size[1] // 2) - 2))
        else:
            screen.blit(self.image, ((61 * self.x + 1 + 30 - self.image_size[0] // 2),(61 * self.y + 1 + 30 - self.image_size[1] // 2)))


class Player2(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.backpack = [0] * 4 + [50] + [0]
        self.image = image.load("Image/player.png")
        self.actimage = image.load("Image/player.png")
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
    
    def draw(self, screen, active):
        if active:
            screen.blit(self.actimage, ((61 * self.x + 1 + 30 - self.image_size[0] // 2) - 2,(61 * self.y + 1 + 30 - self.image_size[1] // 2) - 2))
        else:
            screen.blit(self.image, ((61 * self.x + 1 + 30 - self.image_size[0] // 2),(61 * self.y + 1 + 30 - self.image_size[1] // 2)))