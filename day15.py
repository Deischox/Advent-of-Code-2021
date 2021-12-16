import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

def one():
    lines = open('day15.txt').read().splitlines()
    paths = {(x,y): 0 for x in range(len(lines)) for y in range(len(lines))}
    maze = np.array([list(int(i) for i in line) for line in lines])
    pathArray = np.array([list(int(i) for i in line) for line in lines])
    


    for xx in range(len(maze)):
        if xx >= 1:
            paths[(xx,0)] = paths[(xx-1,0)] + maze[xx-1,0]
            

    for x in range(len(maze)):
        for y in range(len(maze[0])):
            new_y = y-1
            if new_y >= 0:
                paths[(x,y)] = paths[(x,new_y)] + maze[x,new_y]
            pathArray[x,y] = paths[(x,y)]

    for x in range(len(maze)):
        for y in range(len(maze[0])):
            a = [[-1,0],[1,0],[0,-1],[0,1]]
            for n in a:
                new_x = x+n[0]
                new_y = y+n[1]
                if new_x >= 0 and new_x < len(maze) and new_y >= 0 and new_y < len(maze):
                    cost = paths[(new_x,new_y)] + maze[new_x,new_y]
                    old_cost = paths[(x,y)]
                    if cost < old_cost:
                        paths[(x,y)] = cost
            pathArray[x,y] = paths[(x,y)]

    print("RISK FOR WHOLE TRIP: {}".format(paths[(len(maze)-1,len(maze[0])-1)]))
def two():
    lines = open('day15.txt').read().splitlines()
    maze = np.array([list(int(i) for i in line) for line in lines])
    new_maze = np.zeros((len(lines)*5,len(lines)*5))
    

    for x in range(len(new_maze)):
        for y in range(len(new_maze)):
            new_x = x%(len(maze))
            new_y = y%(len(maze))
            value = (maze[new_x,new_y] + x//(len(maze)) + y//(len(maze)))
            if value > 9:
                new_maze[x,y] = value%9
            else: 
                new_maze[x,y] = value
    
    maze = new_maze.copy()

    paths = {(x,y): 0 for x in range(len(new_maze)) for y in range(len(new_maze))}
    
    pathArray = np.zeros((len(lines)*5,len(lines)*5))

    


    for xx in range(len(maze)):
        if xx >= 1:
            paths[(xx,0)] = paths[(xx-1,0)] + maze[xx-1,0]
            

    for x in range(len(maze)):
        for y in range(len(maze[0])):
            new_y = y-1
            if new_y >= 0:
                paths[(x,y)] = paths[(x,new_y)] + maze[x,new_y]
            pathArray[x,y] = paths[(x,y)]
    
    

    for x in range(len(maze)):
        for y in range(len(maze[0])):
            a = [[-1,0],[1,0],[0,-1],[0,1]]
            for n in a:
                new_x = x+n[0]
                new_y = y+n[1]
                if new_x >= 0 and new_x < len(maze) and new_y >= 0 and new_y < len(maze):
                    cost = paths[(new_x,new_y)] + maze[new_x,new_y]
                    old_cost = paths[(x,y)]
                    if cost == 3:
                        print("HEY")
                    if cost < old_cost:
                        paths[(x,y)] = cost
            pathArray[x,y] = paths[(x,y)]
    np.savetxt('cost.txt',pathArray, fmt="%03d")
    np.savetxt('nomral.txt',new_maze, fmt="%d")

    print("RISK FOR WHOLE TRIP: {}".format(paths[(len(maze)-1,len(maze[0])-1)]))
two()