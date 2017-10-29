import pygame, sys, time, random
from blocks import *
from player import *

def endturn():
    global boolgo, nezatop, turn, players
    if turn % 7 == 0:
        for i in range(10):
            for j in range(10):
                if field[i][j].zatopl:
                    field[i][j].zatopl = 2
    else:
        for i in range(min(nezatop, 1)):
            x, y = [random.randint(0, 9) for q in range(2)]
            while field[x][y].zatopl:
                x, y = [random.randint(0, 9) for q in range(2)]
            field[x][y].zatopl = 1
            nezatop -= 1
            
    for player in players:
        player.can = player.distanse
        #try:
        player.backpack[field[player.x][player.y].resind] += random.randint(1, 5)
        #except:
            #None
        if type(field[player.x][player.y]) == Stock:
            for i in range(5):
                rescol[i] += player.backpack[i]
                player.backpack[i] = 0
    boolgo = False
    booldrain = False
    turn += 1


def bfs(x, y, step):
    global st
    st = {(x, y): step}
    d = [[x, y]]
    di = 0
    while di < len(d):
        cx, cy = d[di]
        cs = st[(cx, cy)]
        if cs > 0:
            for i, j in players[active_player].direct:
                nx, ny = cx + i, cy + j
                if 0 <= nx < 10 and 0 <= ny < 10:
                    if not ([nx, ny] in d) and field[nx][ny].zatopl not in players[active_player].cantgo:
                        d.append([nx, ny])
                        st[(nx, ny)] = cs - 1
        di += 1
    return d


def mouse_click(x, y):
    global description, active_player, boolgo, booldrain, nezatop, goproz
    if 0 <= x <= 611 and 0 <= y <= 611:
        xi = min(9, x // 61)
        yi = min(9, y // 61)
        description = field[xi][yi].description
        for player in players:
            if [player.x, player.y] == [xi, yi]:
                active_player = players.index(player)
  
        if boolgo and [xi, yi] in letgo:
            players[active_player].can = st[xi, yi]
            players[active_player].x, players[active_player].y = xi, yi
            boolgo = False
            goproz = True
        else:
            boolgo = False
        
        if booldrain and [xi, yi] in letdrain:
            players[active_player].backpack[4] -= 5
            field[xi][yi].zatopl = 0
            nezatop -= 1
            booldrain = False
            drainproz = True
        else:
            booldrain = False

def create_field():
    global stockx, stocky
    col = [random.randint(1, 3) for i in range(5)]
    a = [0] * (99 - sum(col)) + [1] + [2] * col[0] + [3] * col[1] + [4] * col[2] + [5] * col[3] + [6] * col[4]
    random.shuffle(a)
    field = [a[i * 10:i * 10 + 10] for i in range(10)]
    field2 = field[::]
    for i in range(10):
        for j in range(10):
            if field[i][j] == 0:
                blocks.add(Grass(i, j))
                field2[i][j] = Grass(i, j)
            elif field[i][j] == 1:
                stockx = i
                stocky = j
                blocks.add(Stock(i, j))
                field2[i][j] = Stock(i, j)
            elif field[i][j] == 2:
                blocks.add(res2(i, j))
                field2[i][j] = res2(i, j)
            elif field[i][j] == 3:
                blocks.add(res3(i, j))
                field2[i][j] = res3(i, j)
            elif field[i][j] == 4:
                blocks.add(res4(i, j))
                field2[i][j] = res4(i, j)
            elif field[i][j] == 5:
                blocks.add(res5(i, j))
                field2[i][j] = res5(i, j)
            elif field[i][j] == 6:
                blocks.add(res6(i, j))
                field2[i][j] = res6(i, j)
    return field2


def go():
    global boolgo, letgo, proz, booldrain, goproz, active_player
    booldrain = False
    letgo = bfs(players[active_player].x, players[active_player].y, players[active_player].can)
    boolgo = not boolgo
    if not boolgo:
        goproz = True

def drain():
    global booldrain, letdrain, proz, boolgo
    booldrain = not booldrain
    boolgo = False
    if not booldrain:
        drainproz = True    
    if field[players[active_player].x][players[active_player].y].zatopl == 1:
        letdrain = [[players[active_player].x, players[active_player].y]]
    else:
        letdrain = []
        for i, j in players[active_player].drain:
            nx, ny = players[active_player].x + i, players[active_player].y + j
            if 0 <= nx < 10 and 0 <= ny < 10:
                if field[nx][ny].zatopl == 1:
                    letdrain.append([nx, ny])
    if len(letdrain) == 0:
        booldrain = False
    proz = 0
        


#Константы
clock = pygame.time.Clock()
nezatop = 100
proz = 0
turn = 1
stockx = stocky = 0
blocks = pygame.sprite.Group()
description = []
rescol = [0, 0, 0, 0, 0]
active_player = 0
goproz = False
drainproz = False
width = 911
height = 611
letgo = []

pygame.init()
screen = pygame.display.set_mode((width, height))

#Шрифты
mainfont = pygame.font.SysFont("Times new roman", 20)
canfont = pygame.font.SysFont("Times new roman", 12)
descfont = pygame.font.SysFont("Times new roman", 25)

field = create_field()

players = [Player1(0, 0), Player1(9, 9), Player2(0, 9)]

golab = mainfont.render('Go', 1, (0,0,0))
gorect = golab.get_rect(center=(761, 190))

endlab = mainfont.render('End turn', 1, (0,0,0))
endrect = endlab.get_rect(center=(761, 360))

drainlab = mainfont.render('Drain', 1, (0,0,0))
drainrect = drainlab.get_rect(center=(761, 220))

bgcolor = (0, 0, 0)
mainloop = True
boolgo = False
booldrain = False

while mainloop:
    for event in pygame.event.get():
        if event.type == QUIT:
            mainloop = False
        if event.type == MOUSEBUTTONDOWN:
            mouse_click(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if gorect.collidepoint(mouse_pos) and field[players[active_player].x][players[active_player].y].zatopl == 0 and players[active_player].can > 0:
                go()
            if endrect.collidepoint(mouse_pos):
                endturn()
            if drainrect.collidepoint(mouse_pos) and players[active_player].backpack[4] >= 5:
                drain()
                
    
    screen.fill(bgcolor)
    
    blocks.draw(screen)
    
    ty = 400
    draw.rect(screen, (255, 250, 184), (611, 0, 300, 611))
    draw.rect(screen, (245, 222, 179), (611, 380, 911, 2))
    draw.rect(screen, (245, 222, 179), (611, 80, 911, 2))    
    for i in description:
        label = descfont.render(i, 1, (0,0,0))
        rect = label.get_rect(center=(761, ty))
        screen.blit(label, rect)
        ty += 30
    
    
    if active_player != -1:
        draw.rect(screen, (245, 222, 179), (611, 160, 911, 2)) 
        for i in range(5):
            lb = mainfont.render(str(players[active_player].backpack[i]), 1, (0,0,0))
            rect = lb.get_rect(center=(611 + 30 + 60 * i, 60 + 80))
            screen.blit(lb, rect)
        
        mres2 = pygame.image.load('Image/mres2.png')
        screen.blit(mres2, (611 + 15 + 60 * 0, 15 + 80))
        
        mres3 = pygame.image.load('Image/mres3.png')
        screen.blit(mres3, (611 + 15 + 60 * 1, 15 + 80))
        
        mres4 = pygame.image.load('Image/mres4.png')
        screen.blit(mres4, (611 + 15 + 60 * 2, 15 + 80))
            
        mres5 = pygame.image.load('Image/mres5.png')
        screen.blit(mres5, (611 + 15 + 60 * 3, 15 + 80))
            
        mres6 = pygame.image.load('Image/mres6.png')
        screen.blit(mres6, (611 + 15 + 60 * 4, 15 + 80))   
        
        screen.blit(golab, gorect)
        screen.blit(drainlab, drainrect)        
    
    for i in range(5):
        lb = mainfont.render(str(rescol[i]), 1, (0,0,0))
        rect = lb.get_rect(center=(611 + 30 + 60 * i, 60))
        screen.blit(lb, rect)
    
    mres2 = pygame.image.load('Image/mres2.png')
    screen.blit(mres2, (611 + 15 + 60 * 0, 15))
    
    mres3 = pygame.image.load('Image/mres3.png')
    screen.blit(mres3, (611 + 15 + 60 * 1, 15))
    
    mres4 = pygame.image.load('Image/mres4.png')
    screen.blit(mres4, (611 + 15 + 60 * 2, 15))
        
    mres5 = pygame.image.load('Image/mres5.png')
    screen.blit(mres5, (611 + 15 + 60 * 3, 15))
        
    mres6 = pygame.image.load('Image/mres6.png')
    screen.blit(mres6, (611 + 15 + 60 * 4, 15))

    
    screen.blit(endlab, endrect)
    
    for i in range(10):
        for j in range(10):
            if field[i][j].zatopl == 1:
                s = pygame.Surface((60,60))  # the size of your rect
                s.set_alpha(128)  
                s.fill((0, 0, 255))           # this fills the entire surface
                screen.blit(s, (61 * i + 1,61 * j + 1))
            elif field[i][j].zatopl == 2:
                abyss = pygame.image.load('Image/abyss.png')          # this fills the entire surface
                screen.blit(abyss, (61 * i + 1,61 * j + 1))
                
        
    if boolgo:
        for i in range(10):
            for j in range(10):
                if [i, j] not in letgo:
                    s = pygame.Surface((60,60))  # the size of your rect
                    s.set_alpha(proz)  
                    s.fill((0, 0, 0))           # this fills the entire surface
                    screen.blit(s, (61 * i + 1,61 * j + 1))     
        if proz < 128:
            proz = 128#+= 4
    
    #if goproz:
        #for i in range(10):
            #for j in range(10):
                #if [i, j] not in letgo:
                    #s = pygame.Surface((60,60))  # the size of your rect
                    #s.set_alpha(proz)  
                    #s.fill((0, 0, 0))           # this fills the entire surface
                    #screen.blit(s, (61 * i + 1,61 * j + 1))     
        #if proz > 0:
            #proz -= 4
        #if proz == 0:
            #goproz = False
    
    if booldrain:
        for i in range(10):
            for j in range(10):
                if [i, j] not in letdrain:
                    s = pygame.Surface((60,60))  # the size of your rect
                    s.set_alpha(proz)  
                    s.fill((255, 255, 0))           # this fills the entire surface
                    screen.blit(s, (61 * i + 1,61 * j + 1))     
        if proz < 128:
            proz = 128#+= 4

    #if drainproz:
        #for i in range(10):
            #for j in range(10):
                #if [i, j] not in letdrain:
                    #s = pygame.Surface((60,60))  # the size of your rect
                    #s.set_alpha(proz)  
                    #s.fill((255, 255, 0))           # this fills the entire surface
                    #screen.blit(s, (61 * i + 1,61 * j + 1))     
        #if proz > 0:
            #proz -= 4
        #if proz == 0:
            #drainproz = False
    
    for player in range(len(players)):
        players[player].draw(screen, player == active_player)
        
    
    
    
    for i in range(len(players)):
        if i == active_player:
            screen.blit(players[i].actimage, (611 - players[i].image_size[0] // 2 + 30 + 60 * i - 2, 280 - 2))
        else:
            screen.blit(players[i].image, (611 - players[i].image_size[0] // 2 + 30 + 60 * i, 280))
        cg = canfont.render(str(players[i].can), 1, (219,55,20))
        cgrect = cg.get_rect(center=(611 - players[i].image_size[0] // 2 + 30 + 60 * i + 32, 330))        
        screen.blit(cg, cgrect)
        #screen.draw.text(str(players[i].can), center=(611 - players[i].image_size[0] // 2 + 30 + 60 * i + 32, 330), fontsize=12, owidth=1.5)
        
    
    
    
        
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

