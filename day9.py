import numpy as np
def one():
    f = open('input/part1/day9.txt')
    lines = f.readlines()  
    
    
    HIGHX = len(lines)
    HIGHY = len(list(lines)[0])-1
    heightmap = np.zeros((HIGHX,HIGHY))
    
    x = 0
    y = 0
    
    #CREATE ARRAY
    for l in lines:
        x = 0
        for c in list(l):
            if c != "\n":
                heightmap[y,x] = int(c)
                x += 1
        y += 1
    
    #Check 
    x = 0
    y = 0

    a = []
    cor = []

    

    while x < HIGHY:
        y = 0
        while y < HIGHX:
           
           v = -1
           h = -1
           low = heightmap[y,x]
           while v < 2:
               h = -1
               while h < 2:
                   if y+v >= 0 and y+v < HIGHX and x+h >= 0 and x+h < HIGHY:
                        if heightmap[y,x] > heightmap[y+v,x+h]:
                            v += 100000
                            h += 100000
                            low = 1000
                   h +=1
               v +=1
           if low == heightmap[y,x]:
               a.append(low)
               cor.append([y,x])

           y +=1 
        x += 1
    
    counter = 0
    for i in a:
        counter += i +1
    #print(counter)
    return cor


def two():
    f = open('input/part1/day9.txt')
    lines = f.readlines()  
    
    
    HIGHX = len(lines)
    HIGHY = len(list(lines)[0])-1
    heightmap = np.zeros((HIGHX,HIGHY))
    
    x = 0
    y = 0
    
    #CREATE ARRAY
    for l in lines:
        x = 0
        for c in list(l):
            if c != "\n":
                heightmap[y,x] = int(c)
                x += 1
        y += 1
    
    cor = one()
    l = []
    for c in cor:
        r = recur(c[0],c[1],heightmap,[])
        l.append(len(r))
    l = sorted(l)
    count = 1
    for i in l[-3:]:
        count *= i
    print(count)

def adjust(x,y,map,xmax,ymax,fromx,fromy):
    a = [[-1,0],[0,-1],[0,1],[1,0]]
    for c in a:
        if x+c[0] >= 0 and y+c[1] >= 0 and x+c[0] < xmax and y+c[1] < ymax and not (y+c[1] == fromy and x+c[0] == fromx):
            if map[x+c[0],y+c[1]] != 9:
                return 1 + adjust(x+c[0],y+c[1],map,xmax,ymax,x,y)
    return 1



def recur(x,y,map,v):
    a = [[-1,0],[0,-1],[0,1],[1,0]]
    
    if [x,y] not in v:
        v.append([x,y])

    for c in a:
        if x+c[0] >= 0 and y+c[1] >= 0 and [x+c[0],y+c[1]] not in v and x+c[0] < len(map) and y+c[1] < len(map[0]):
            if map[x+c[0],y+c[1]] != 9:
                v.append([x+c[0],y+c[1]])
                recur(x+c[0],y+c[1],map,v)
    return v
two()