import copy
def one():
    #CREATE DATA
    f = open('input/part1/day4.txt')
    lines = f.readlines()
    lines = [i.split('\n')[0] for i in lines]
    boards = []
    i = 2
    while i < len(lines):
        b = [i.split(' ') for i in lines[i:i+5]]
        for x in b:
            for y in x:
                if y == '':
                    x.remove(y)
        boards.append(b)
        i+=6

    #CHECK FOR MATCH IN BOARD
    bingo = [[[ None for x in range(5) ] for y in range(5) ] for z in range(100)]
    
    winner = ""
    for n in lines[0].split(','):    
        if winner != "":
            break
        for board in boards:
            for row in board:
                for number in row:
                    if number == n:
                        x = boards.index(board)
                        y = board.index(row)
                        z = row.index(number)
                        bingo[x][y][z] = "*"
                        
                        #CHECK FOR BINGO (HORIZONTAL)
                        if bingo[x][y] == ["*","*","*","*","*"]:
                            winner = boards[x][y]
                            xx = 0
                            yy = 0
                            counter = 0
                            while xx < len(bingo[x]):
                                while yy < len(bingo[x][xx]):
                                    
                                    if bingo[x][xx][yy] != "*":
                                        counter += int(boards[x][xx][yy])
                                    yy+=1
                                yy = 0
                                xx += 1
                            print(counter,number,counter*int(number))

                        #CHECK FOR BINGO (VERTICAL)
                        b = []
                        r = 0
                        while r < len(bingo[x]):
                            if bingo[x][r][z] == "*":
                                b.append(boards[x][r][z])
                            r+=1
                        if len(b) == 5: 
                            winner = b

                            xx = 0
                            yy = 0
                            counter = 0
                            while xx < len(bingo[x]):
                                while yy < len(bingo[x][xx]):
                                    
                                    if bingo[x][xx][yy] != "*":
                                        counter += int(boards[x][xx][yy])
                                    yy+=1
                                yy = 0
                                xx += 1
                            print(counter,number,counter*int(number))
    print(winner)                  
                        
    

def two():
    #CREATE DATA
    f = open('input/part1/day4.txt')
    lines = f.readlines()
    lines = [i.split('\n')[0] for i in lines]
    boards = []
    i = 2
    while i < len(lines):
        b = [i.split(' ') for i in lines[i:i+5]]
        for x in b:
            for y in x:
                if y == '':
                    x.remove(y)
        boards.append(b)
        i+=6

    #CHECK FOR MATCH IN BOARD
    bingo = [[[ None for x in range(5) ] for y in range(5) ] for z in range(100)]
    
    board_won = [ None for x in range(len(boards)) ]

    winner = ""
    for n in lines[0].split(','):    
        all_won = True
        for b in board_won:
            if b != "YES":
                all_won = False
        if all_won:
            break

        for board in boards:
            for row in board:
                for number in row:
                    if number == n:
                        x = boards.index(board)
                        y = board.index(row)
                        z = row.index(number)
                        bingo[x][y][z] = "*"
                        
                        #CHECK FOR BINGO (HORIZONTAL)
                        if bingo[x][y] == ["*","*","*","*","*"]:
                            winner = boards[x][y]
                            xx = 0
                            yy = 0
                            counter = 0
                            while xx < len(bingo[x]):
                                while yy < len(bingo[x][xx]):
                                    
                                    if bingo[x][xx][yy] != "*":
                                        counter += int(boards[x][xx][yy])
                                    yy+=1
                                yy = 0
                                xx += 1
                            
                            board_won[x] = "YES"
                            c = 0
                            for b in board_won:
                                if b != "YES":
                                    c = 1
                            if c == 0:
                                print(winner)
                                print(counter,number,counter*int(number))
                            c = 0


                        #CHECK FOR BINGO (VERTICAL)
                        b = []
                        r = 0
                        while r < len(bingo[x]):
                            if bingo[x][r][z] == "*":
                                b.append(boards[x][r][z])
                            r+=1
                        if len(b) == 5: 
                            winner = b

                            xx = 0
                            yy = 0
                            counter = 0
                            while xx < len(bingo[x]):
                                while yy < len(bingo[x][xx]):
                                    
                                    if bingo[x][xx][yy] != "*":
                                        counter += int(boards[x][xx][yy])
                                    yy+=1
                                yy = 0
                                xx += 1
                            board_won[x] = "YES"
                            c = 0
                            for b in board_won:
                                if b != "YES":
                                    c = 1
                            if c == 0:
                                print(counter,number,counter*int(number))
                            c = 0
    

    
one()
two()