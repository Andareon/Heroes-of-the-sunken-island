import pygame, sys, time, random
from blocks import *
from player import *
from Button import Button
from Slider import Slider


def test():
    sl = Slider(screen, 50, 50, 30, 100, 0, 25, 3, 'Image/red_circle.png')
    mainloop = True
    bgcolor = (245, 222, 179)
    while mainloop:
        for event in pygame.event.get():
            if event.type == QUIT:
                mainloop = False

            sl.change(event)

        screen.fill(bgcolor)
        sl.draw()

        pygame.display.flip()
        clock.tick(60)


def player_choose():
    global players
    mainloop = True
    bgcolor = (245, 222, 179)
    fx, fy = 20, 350
    numplay = 1
    player_list = [Player1(0, 0), Player2(0, 0)]
    list_play = [Player1, Player2]
    choosen_play = [0]
    boolchoose = False
    choose = 0
    while mainloop:
        for event in pygame.event.get():
            if event.type == QUIT:
                mainloop = False
            if event.type == MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if boolchoose and not(fx + choose * 62 <= mouse[0] <= fx + choose * 62 + 62 and fy - len(player_list) * 31 <= mouse[1] <= fy + 62 + len(player_list) * 31):
                    boolchoose = False
                q = False
                if boolchoose and fx + choose * 62 <= mouse[0] <= fx + choose * 62 + 62 and fy - len(player_list) * 31 <= mouse[1] <= fy + 62 + len(player_list) * 31:
                    if fy + len(player_list) * 31 <= mouse[1] <= fy + 62 + len(player_list) * 31:
                        if numplay > 1:
                            choosen_play.pop(choose)
                            numplay -= 1
                    else:
                        choosen_play[choose] = (mouse[1] - (fy - len(player_list) * 31)) // 62
                    q = True
                    boolchoose = False
                if not q and fy <= mouse[1] <= fy + 64 and fx + 2 <= mouse[0] <= fx + 2 + numplay * 62:
                    choose = (mouse[0] - fx) // 62
                    boolchoose = True
                if numplay < 14 and fx + 2 + numplay * 62 <= mouse[0] <= fx + 64 + numplay * 62 and fy <= mouse[1] <= fy + 64:
                    numplay += 1
                    choosen_play.append(0)

            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    s = set()
                    while len(s) < numplay:
                        s.add((random.randint(0, 9), random.randint(0, 9)))
                    s = list(s)
                    for i in range(numplay):
                        s[i] = list_play[choosen_play[i]](s[i][0], s[i][1])
                    players = s
                    return game()
                if event.key == 270:
                    if numplay < 15:
                        numplay += 1
                        choosen_play.append(0)
                if event.key == 269:
                    if numplay > 1:
                        numplay -= 1
                        choosen_play = choosen_play[:-1]
                if event.key == 49:
                    if numplay < 14:
                        choosen_play.append(0)
                        numplay += 1
                if event.key == 50:
                    if numplay < 14:
                        choosen_play.append(1)
                        numplay += 1

        screen.fill(bgcolor)

        for i in range(numplay):
            rup = pygame.Surface((64, 2))  # the size of your rect
            rup.fill((0, 0, 0))  # this fills the entire surface
            screen.blit(rup, (fx + 62 * i, fy))
            screen.blit(rup, (fx + 62 * i, fy + 62))

            rlt = pygame.Surface((2, 64))  # the size of your rect
            rlt.fill((0, 0, 0))  # this fills the entire surface
            screen.blit(rlt, (fx + 62 * i, fy))
            screen.blit(rlt, (fx + 62 * i + 62, fy))
            screen.blit(player_list[choosen_play[i]].image, player_list[choosen_play[i]].image.get_rect(center=(fx + 2 + 62 * i + 30, fy + 32)))

        if boolchoose:
            q = len(player_list) + 1
            ynow = fy - (q - 1) * 31
            for i in range(q):
                rup = pygame.Surface((64, 2))  # the size of your rect
                rup.fill((0, 0, 0))  # this fills the entire surface
                screen.blit(rup, (fx + choose * 62, ynow))
                screen.blit(rup, (fx + 62 * choose, ynow + 62))

                rlt = pygame.Surface((2, 64))  # the size of your rect
                rlt.fill((0, 0, 0))  # this fills the entire surface
                screen.blit(rlt, (fx + 62 * choose, ynow))
                screen.blit(rlt, (fx + 62 * choose + 62, ynow))
                ynow += 62

                fill = pygame.Surface((60, 60))
                fill.fill(bgcolor)
                screen.blit(fill, (fx + choose * 62 + 2, ynow + 2))

                if i < q - 1:
                    screen.blit(player_list[i].image, player_list[i].image.get_rect(center=(fx + choose * 62 + 32, ynow - 62 + 32)))
                else:
                    screen.blit(image.load("Image/Player/Delete.png"),
                                image.load("Image/Player/Delete.png").get_rect(center=(fx + choose * 62 + 32, ynow - 62 + 32)))


        if numplay < 14:
            rup = pygame.Surface((64, 2))  # the size of your rect
            rup.fill((0, 0, 0))  # this fills the entire surface
            screen.blit(rup, (fx + 62 * numplay, fy))
            screen.blit(rup, (fx + 62 * numplay, fy + 62))

            rlt = pygame.Surface((2, 64))  # the size of your rect
            rlt.fill((0, 0, 0))  # this fills the entire surface
            screen.blit(rlt, (fx + 62 * numplay, fy))
            screen.blit(rlt, (fx + 62 * numplay + 62, fy))

            screen.blit(image.load("Image/Player/Add.png"),
                                    image.load("Image/Player/Add.png").get_rect(center=(fx + 2 + 62 * numplay + 30, fy + 32)))



        pygame.display.flip()
        clock.tick(60)


def game():
    global proz, players, boolgo, booldrain, field, active_player, boolswap1, boolswap2, letswap, swapwidth, swapheight, swapplayer, slides, slidefont
    mainloop = True
    boolswap1 = False
    boolswap2 = False
    swap_but = Button(screen, (228, 47, 200), 640, 395, 30, 56, 'SWAP', (0, 0, 0), 2, mainfont)
    slides = []
    field = create_field()
    active_player = 0
    bgcolor = (0, 0, 0)
    slides = []
    while mainloop:
        for event in pygame.event.get():
            if boolswap2:
                for i in range(5):
                    slides[i].change(event)
            if event.type == QUIT:
                mainloop = False
            if event.type == KEYDOWN:
                if event.key == K_g:
                    if field[players[active_player].x][players[active_player].y].zatopl == 0 and players[
                    active_player].can > 0:
                        go()
                if event.key == K_e:
                    endturn()
                if event.key == K_d:
                    if players[active_player].backpack[4] >= 1 and 1 in [field[players[active_player].x + dx][players[active_player].y + dy].zatopl
                                                                            for dx, dy in players[active_player].drain + [[0, 0]] if (0 <= players[active_player].x + dx < 10 and
                                                                            0 <= players[active_player].y + dy < 10)]:
                        drain()
                if event.key == K_s:
                    if swapbut.active:
                        boolswap1 = True
                        swap()
                        boolgo = booldrain = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                mouse_click(mouse_pos[0], mouse_pos[1])


                gobut.update(mouse_pos)
                endbut.update(mouse_pos)
                drainbut.update(mouse_pos)
                swapbut.update(mouse_pos)
                swap_but.update(mouse_pos)

                if gobut.pressed and gobut.active:
                    go()
                if endbut.pressed and endbut.active:
                    endturn()
                if drainbut.pressed and drainbut.active:
                    drain()
                if swapbut.pressed and swapbut.active:
                    boolswap1 = True
                    boolgo = booldrain = False
                if swap_but.pressed and swap_but.active:
                    for z in range(5):
                        players[active_player].backpack[z], players[swapplayer].backpack[z] = slides[z].now, slides[z].max - slides[z].now
                    boolswap2 = False
            if event.type == pygame.MOUSEBUTTONUP:
                gobut.pressed = False
                endbut.pressed = False
                drainbut.pressed = False
                swapbut.pressed = False
                swap_but.pressed = False
        if not len(players) or field[stockx][stocky].zatopl == 2:
            return menu()


        gobut.active = field[players[active_player].x][players[active_player].y].zatopl == 0 and players[
            active_player].can > 0

        drainbut.active = players[active_player].backpack[4] >= 1 and 1 in [field[players[active_player].x + dx][players[active_player].y + dy].zatopl
                                                                            for dx, dy in players[active_player].drain + [[0, 0]] if (0 <= players[active_player].x + dx < 10 and
                                                                            0 <= players[active_player].y + dy < 10)]

        swapbut.active = field[players[active_player].x][players[active_player].y].zatopl == 0 and \
                         [players[active_player].x, players[active_player].y] in \
                         [[stockx, stocky]] + [[players[i].x + dx, players[i].y + dy]
                                               for i in range(len(players))
                                               for dx, dy in players[active_player].swap
                                               if (0 <= players[i].x + dx < 10 and 0 <= players[i].y + dy < 10) and
                                               i != active_player]


        screen.fill(bgcolor)

        blocks.draw(screen)

        draw.rect(screen, (255, 250, 184), (611, 0, 300, 611))
        # draw.rect(screen, (245, 222, 179), (611, 380, 911, 2))
        draw.rect(screen, (245, 222, 179), (611, 80, 911, 2))


        if active_player != -1:
            draw.rect(screen, (245, 222, 179), (611, 160, 911, 2))
            for i in range(5):
                lb = mainfont.render(str(players[active_player].backpack[i]), 1, (0, 0, 0))
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

        gobut.draw()
        endbut.draw()
        drainbut.draw()
        swapbut.draw()

        for i in range(5):
            lb = mainfont.render(str(rescol[i]), 1, (0, 0, 0))
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


        for i in range(10):
            for j in range(10):
                if field[i][j].zatopl == 1:
                    s = pygame.Surface((60, 60))  # the size of your rect
                    s.set_alpha(128)
                    s.fill((0, 0, 255))  # this fills the entire surface
                    screen.blit(s, (61 * i + 1, 61 * j + 1))
                elif field[i][j].zatopl == 2:
                    abyss = pygame.image.load('Image/abyss.png')  # this fills the entire surface
                    screen.blit(abyss, (61 * i + 1, 61 * j + 1))

        if boolgo:
            for i in range(10):
                for j in range(10):
                    if [i, j] not in letgo:
                        s = pygame.Surface((60, 60))  # the size of your rect
                        s.set_alpha(proz)
                        s.fill((0, 0, 0))  # this fills the entire surface
                        screen.blit(s, (61 * i + 1, 61 * j + 1))
            if proz < 128:
                proz = 128  # += 4

        # if goproz:
        # for i in range(10):
        # for j in range(10):
        # if [i, j] not in letgo:
        # s = pygame.Surface((60,60))  # the size of your rect
        # s.set_alpha(proz)
        # s.fill((0, 0, 0))           # this fills the entire surface
        # screen.blit(s, (61 * i + 1,61 * j + 1))
        # if proz > 0:
        # proz -= 4
        # if proz == 0:
        # goproz = False

        if booldrain:
            for i in range(10):
                for j in range(10):
                    if [i, j] not in letdrain:
                        s = pygame.Surface((60, 60))  # the size of your rect
                        s.set_alpha(proz)
                        s.fill((255, 255, 0))  # this fills the entire surface
                        screen.blit(s, (61 * i + 1, 61 * j + 1))
            if proz < 128:
                proz = 128  # += 4

        # if drainproz:
        # for i in range(10):
        # for j in range(10):
        # if [i, j] not in letdrain:
        # s = pygame.Surface((60,60))  # the size of your rect
        # s.set_alpha(proz)
        # s.fill((255, 255, 0))           # this fills the entire surface
        # screen.blit(s, (61 * i + 1,61 * j + 1))
        # if proz > 0:
        # proz -= 4
        # if proz == 0:
        # drainproz = False

        if boolswap1:
            for i in range(10):
                for j in range(10):
                    if [i, j] in letswap:
                        s = pygame.Surface((60, 60))  # the size of your rect
                        s.set_alpha(proz)
                        s.fill((115, 40, 255))  # this fills the entire surface
                        screen.blit(s, (61 * i + 1, 61 * j + 1))
            if proz < 128:
                proz = 128  # += 4

        for player in range(len(players)):
            players[player].draw(screen, player == active_player)

        for i in range(len(players)):
            if i == active_player:
                screen.blit(players[i].actimage, (611 - players[i].image_size[0] // 2 + 30 + 60 * (i % 5) - 2, 280 - 2 + 10 + i // 5 * 60))
            else:
                screen.blit(players[i].image, (611 - players[i].image_size[0] // 2 + 30 + 60 * (i % 5), 280 + 10 + i // 5 * 60))
            cg = canfont.render(str(players[i].can), 1, (219, 55, 20))
            cgrect = cg.get_rect(center=(611 - players[i].image_size[0] // 2 + 30 + 60 * (i % 5) + 32, 330 + i // 5 * 60))
            screen.blit(cg, cgrect)

        if boolswap2:
            boolswap1 = False
            bg = pygame.Surface((911, 611))
            bg.fill((120, 120, 120))
            bg.set_alpha(200)
            screen.blit(bg, (0, 0))

            swapwidth = 450
            swapheight = 250
            swapbg = pygame.Surface((swapwidth, swapheight))
            swapbg.fill((245, 222, 179))
            screen.blit(swapbg, (911 // 2 - swapwidth // 2 + 25, 611 // 2 - swapheight // 2))

            for i in range(5):
                if len(slides) < 5:
                    slides.append(Slider(screen, 911 // 2 - 350 // 2 + 20 * (i * 2 + 1) + 30 * i, 611 // 2 - 200 // 2 + 15,
                                         30, 150, 0, players[active_player].backpack[i] + players[swapplayer].backpack[i], players[active_player].backpack[i], 'Image/' + str(i + 1) + 'slide.png'))
                slides[i].draw()
                cg = slidefont.render(str(slides[i].now), 1, (0, 0, 0))
                cgrect = cg.get_rect(
                    center=(911 // 2 - 350 // 2 + 20 * (i * 2 + 1) + 30 * i + 15, 611 // 2 - 200 // 2))
                screen.blit(cg, cgrect)

                cg = slidefont.render(str(slides[i].max - slides[i].now), 1, (0, 0, 0))
                cgrect = cg.get_rect(
                    center=(911 // 2 - 350 // 2 + 20 * (i * 2 + 1) + 30 * i + 15, 611 // 2 - 200 // 2 + 178))
                screen.blit(cg, cgrect)

            ras = pygame.Surface((2, swapheight))
            ras.fill((0, 0, 0))
            screen.blit(ras, (911 // 2 - swapwidth // 2 + 400, 611 // 2 - swapheight // 2))

            cg = slidefont2.render(str(sum([slides[i].now for i in range(5)])), 1,
                                   [(255, 0, 0), (19, 193, 0)][sum([slides[i].now for i in range(5)]) <= players[active_player].maxweight])
            cgrect = cg.get_rect(
                center=(911 // 2 - swapwidth // 2 + 437, 611 // 2 - 200 // 2))
            screen.blit(cg, cgrect)

            cg = slidefont2.render(str(sum([slides[i].max - slides[i].now for i in range(5)])), 1,
                                   [(255, 0, 0), (19, 193, 0)][
                                       sum([slides[i].max - slides[i].now for i in range(5)]) <= players[swapplayer].maxweight])
            cgrect = cg.get_rect(
                center=(911 // 2 - swapwidth // 2 + 437, 611 // 2 - 200 // 2 + 178))
            screen.blit(cg, cgrect)

            swap_but.active = sum([slides[i].max - slides[i].now for i in range(5)]) <= players[swapplayer].maxweight and sum([slides[i].now for i in range(5)]) <= players[active_player].maxweight

            swap_but.draw()

        pygame.display.flip()
        clock.tick(60)


def menu():
    mainloop = True
    bgcolor = (245, 222, 179)
    start_but = Button(screen, (228, 47, 200), 20, 100, 100, 200, 'START GAME', (0, 0, 0), 2, butfont)
    bgtime = 0
    bgtimefps = 0
    while mainloop:
        for event in pygame.event.get():
            if event.type == QUIT:
                mainloop = False
            elif event.type == MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                start_but.update(mouse)
            elif event.type == MOUSEBUTTONUP:
                if start_but.pressed:
                    start_but.pressed = False
                    return player_choose()
                start_but.pressed = False

        screen.fill(bgcolor)

        background = pygame.image.load('Image/bg/frame-1.gif')  # + str(bgtime + 1) + '.gif')
        screen.blit(background, (0, 0))
        # if bgtimefps == 3:
        #     bgtime = (bgtime + 1) % 3
        #     bgtimefps = -1
        # bgtimefps += 1

        start_but.draw()
        pygame.display.flip()
        clock.tick(60)


def endturn():
    global boolgo, nezatop, turn, players, active_player
    if turn % 7 == 0:
        for i in range(10):
            for j in range(10):
                if field[i][j].zatopl:
                    field[i][j].zatopl = 2
                    q = 0
                    while q < len(players):
                        if players[q].x == i and players[q].y == j:
                            players.pop(q)
                            if q == active_player:
                                active_player = max(0, active_player - 1)
                            q -= 1
                        q += 1
    else:
        for i in range(min(nezatop, 1)):
            x, y = [random.randint(0, 9) for q in range(2)]
            while field[x][y].zatopl:
                x, y = [random.randint(0, 9) for q in range(2)]
            field[x][y].zatopl = 1
            nezatop -= 1

    for player in players:
        player.can = player.distanse
        # try:
        can = player.maxweight - sum(player.backpack[:-1])
        if can:
            player.backpack[field[player.x][player.y].resind] += random.randint(1, min(can, 5))
        # except:
        # None
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
                    if not ([nx, ny] in d) and field[nx][ny].zatopl not in players[active_player].cantgo and [nx, ny] not in [[player.x, player.y] for player in players]:
                        d.append([nx, ny])
                        st[(nx, ny)] = cs - 1
        di += 1
    return d


def mouse_click(x, y):
    global active_player, boolgo, booldrain, nezatop, goproz, boolswap1, swapplayer, boolswap2, swapwidth, swapheight, letswap, slides
    if not boolswap2:
        if 0 <= x <= 611 and 0 <= y <= 611:
            xi = min(9, x // 61)
            yi = min(9, y // 61)

            for player in players:
                if [player.x, player.y] == [xi, yi]:
                    if boolswap1 and [xi, yi] in letswap:
                        swapplayer = players.index(player)
                        boolswap2 = True

                    else:
                        active_player = players.index(player)


            if boolgo and [xi, yi] in letgo:
                players[active_player].can = st[xi, yi]
                players[active_player].x, players[active_player].y = xi, yi
                boolgo = False
                goproz = True
            else:
                boolgo = False

            if booldrain and [xi, yi] in letdrain:
                players[active_player].backpack[4] -= 1
                field[xi][yi].zatopl = 0
                nezatop += 1
                booldrain = False
                drainproz = True
            else:
                booldrain = False

            boolswap1 = False
    else:
        if not(911 // 2 - swapwidth // 2 < x - 25 < 911 // 2 + swapwidth // 2 and 611 // 2 - swapheight // 2 < y < 611 // 2 + swapheight // 2):
            boolswap2 = False
            slides = []



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

def swap():
    global players, letswap, boolswap2
    letswap = []
    for dx, dy in players[active_player].swap:
        nx, ny = players[active_player].x + dx, players[active_player].y + dy
        if 0 <= nx < 10 and 0 < ny < 10:
            for player in players:
                if player.x == nx and player.y == ny:
                    letswap.append([nx, ny])
    if players[active_player].x == stockx and players[active_player].y == stocky:
        letswap.append([stockx, stocky])



# Константы
clock = pygame.time.Clock()
nezatop = 100
proz = 0
turn = 1
stockx = stocky = 0
blocks = pygame.sprite.Group()
rescol = [0, 0, 0, 0, 0]
active_player = 0
goproz = False
drainproz = False
width = 911
height = 611
letgo = []

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Heroes of the sunken island')

# Шрифты
mainfont = pygame.font.SysFont("Times new roman", 20)
canfont = pygame.font.SysFont("Times new roman", 12)
descfont = pygame.font.SysFont("Times new roman", 25)
butfont = pygame.font.SysFont("Times new roman", 25)
slidefont = pygame.font.SysFont("Times new roman", 18)
slidefont2 = pygame.font.SysFont("Times new roman", 22)

gobut = Button(screen, (255, 250, 184), 611 + 36, 190 - 13 + 15, 26, 80, 'GO', (0, 0, 0), 2, mainfont)

endbut = Button(screen, (255, 250, 184), 611 + 36 + 80 + 36, 220 - 13 + 15 + 10, 26, 110, 'END TURN', (0, 0, 0), 2, mainfont)

swapbut = Button(screen, (255, 250, 184), 611 + 36 + 80 + 36, 190 - 13 + 15, 26, 110, 'SWAP', (0, 0, 0), 2, mainfont)

drainbut = Button(screen, (255, 250, 184), 611 + 36, 220 - 13 + 15 + 10, 26, 80, 'DRAIN', (0, 0, 0), 2, mainfont)

mainloop = True
boolgo = False
booldrain = False

scene = 0

if scene == 2:
    game()
elif scene == 0:
    menu()
elif scene == 1:
    player_choose()
elif scene == 3:
    test()

pygame.quit()
