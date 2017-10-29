from pygame import *
import pygame
import random

class Grass(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load("Image/grass.png")
        self.x = 61 * x + 1
        self.y = 61 * y + 1
        self.rect = (61 * x + 1, 61 * y + 1, 60, 60)
        self.zatopl = 0
        self.resind = 5
        
        des = open('Description/grass.txt', 'r')
        self.description = []
        a = des.readline().strip()
        while a != '':
            self.description.append(a)
            a = des.readline()[:-1].strip()

class Stock(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load("Image/stock.png")
        self.x = 61 * x + 1
        self.y = 61 * y + 1
        self.rect = (61 * x + 1, 61 * y + 1, 60, 60)
        self.zatopl = 0
        
        des = open('Description/stock.txt', 'r')
        self.description = []
        a = des.readline().strip()
        while a != '':
            self.description.append(a)
            a = des.readline()[:-1].strip()        

class res2(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load("Image/res2.png")
        self.x = 61 * x + 1
        self.y = 61 * y + 1
        self.rect = (61 * x + 1, 61 * y + 1, 60, 60)
        self.zatopl = 0
        self.resind = 0
        
        des = open('Description/res2.txt', 'r')
        self.description = []
        a = des.readline().strip()
        while a != '':
            self.description.append(a)
            a = des.readline()[:-1].strip()        
        
class res3(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load("Image/res3.png")
        self.x = 61 * x + 1
        self.y = 61 * y + 1
        self.rect = (61 * x + 1, 61 * y + 1, 60, 60)
        self.zatopl = 0
        self.resind = 1
        
        des = open('Description/res3.txt', 'r')
        self.description = []
        a = des.readline().strip()
        while a != '':
            self.description.append(a)
            a = des.readline()[:-1].strip()        

class res4(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load("Image/res4.png")
        self.x = 61 * x + 1
        self.y = 61 * y + 1
        self.rect = (61 * x + 1, 61 * y + 1, 60, 60)
        self.zatopl = 0
        self.resind = 2
        
        des = open('Description/res4.txt', 'r')
        self.description = []
        a = des.readline().strip()
        while a != '':
            self.description.append(a)
            a = des.readline()[:-1].strip()        
        
class res5(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load("Image/res5.png")
        self.x = 61 * x + 1
        self.y = 61 * y + 1
        self.rect = (61 * x + 1, 61 * y + 1, 60, 60)
        self.zatopl = 0
        self.resind = 3
        
        des = open('Description/res5.txt', 'r')
        self.description = []
        a = des.readline().strip()
        while a != '':
            self.description.append(a)
            a = des.readline()[:-1].strip()        

class res6(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load("Image/res6.png")
        self.x = 61 * x + 1
        self.y = 61 * y + 1
        self.rect = (61 * x + 1, 61 * y + 1, 60, 60)
        self.zatopl = 0
        self.resind = 4
        
        des = open('Description/res6.txt', 'r')
        self.description = []
        a = des.readline().strip()
        while a != '':
            self.description.append(a)
            a = des.readline()[:-1].strip()        