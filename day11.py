import numpy as np


def inc(map,x,y):
    map[x,y] += 1
    if map[x,y] == 10:
        xx = -1
        while xx < 2:
            yy = -1
            while yy <2:
                if x+xx >= 0 and x+xx < len(map) and y+yy >= 0 and y+yy < len(list(map[0])):
                    map = inc(map,x+xx,y+yy)
                yy +=1
            xx += 1
    return map


def one():
    f = open('input/part1/day11.txt')
    lines = f.readlines()
    lines = [i.split('\n')[0] for i in lines]
    a = np.zeros((len(lines),len(lines)))
    
    x = 0
    y = 0
    while x < len(lines):
        y = 0
        while y < len(list(lines[0])):
            a[x,y] = list(lines[x])[y]
            y += 1
        x += 1

    x = 0
    y = 0
    flashes = 0
    allFlash = 0
    round = 0
    while allFlash != len(a)*len(a[0]):
        x = 0
        while x < len(lines):
            y = 0
            while y < len(list(lines[0])):
                a = inc(a,x,y)
                y += 1
            x += 1
        round += 1
        allFlash = (a>9).sum()
        flashes += (a>9).sum()
        a[a > 9] = 0
        print(a)
    print(round)












    # x = 0
    # y = 0
    # while x < len(lines):
    #     y = 0
    #     while y < len(list(lines[0])):
    #         if a[x,y] > 9:

    #             xx = -1
    #             while xx < 2:
    #                 yy = -1
    #                 while yy <2:
    #                     if x+xx >= 0 and x+xx < len(lines) and y+yy >= 0 and y+yy < len(list(lines[0])):
    #                         a[x+xx,y+yy] += 1
    #                     yy +=1
    #                 xx += 1
    #         y += 1
    #     x += 1
    

one()