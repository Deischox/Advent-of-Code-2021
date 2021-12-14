import numpy as np

def one():
    f = open('input/part1/day5.txt')
    lines = f.readlines()
    a = np.zeros((1000,1000))
    
    for line in lines:
        x1 = int(line.split(',')[0])
        y1 = int(line.split(',')[1].split(' ')[0])

        x2 = int(line.split(',')[1].split(' ')[2])
        y2 = int(line.split(',')[2])
        if x1 == x2:
            if y1 < y2:
                y_k = y1
                while y_k <= y2:
                    a[y_k,x1] += 1
                    y_k +=1
            else:
                y_k = y1
                while y_k >= y2:
                    a[y_k,x1] += 1
                    y_k -=1
        if y1 == y2:
            if x1 < x2:
                x_k = x1
                while x_k <= x2:
                    a[y2,x_k] += 1
                    x_k +=1
            else:
                x_k = x1
                while x_k >= x2:
                    a[y2,x_k] += 1
                    x_k -=1
    print("Solution 1:", np.count_nonzero(a >= 2))

def two():
    f = open('input/part1/day5.txt')
    lines = f.readlines()
    a = np.zeros((1000,1000))
    
    for line in lines:
        x1 = int(line.split(',')[0])
        y1 = int(line.split(',')[1].split(' ')[0])

        x2 = int(line.split(',')[1].split(' ')[2])
        y2 = int(line.split(',')[2])
        if x1 == x2:
            if y1 < y2:
                y_k = y1
                while y_k <= y2:
                    a[y_k,x1] += 1
                    y_k +=1
            else:
                y_k = y1
                while y_k >= y2:
                    a[y_k,x1] += 1
                    y_k -=1
        elif y1 == y2:
            if x1 < x2:
                x_k = x1
                while x_k <= x2:
                    a[y2,x_k] += 1
                    x_k +=1
            else:
                x_k = x1
                while x_k >= x2:
                    a[y2,x_k] += 1
                    x_k -=1
        elif abs(y1-y2) == abs(x1-x2):
           #DOWN RIGHT
            if x1 < x2 and y1 < y2:
               x_k = x1
               y_k = y1
               while x_k <= x2:
                   a[y_k,x_k] += 1
                   x_k += 1
                   y_k += 1

           #DOWN LEFT
            if x1 > x2 and y1 < y2:
               x_k = x1
               y_k = y1
               while x_k >= x2:
                   a[y_k,x_k] += 1
                   x_k -= 1
                   y_k += 1
           
           #UP RIGHT
            if x1 < x2 and y1 > y2:
                x_k = x1
                y_k = y1
                while x_k <= x2:
                    a[y_k,x_k] += 1
                    x_k += 1
                    y_k -= 1

           #UP LEFT
            if x1 > x2 and y1 > y2:
                x_k = x1
                y_k = y1
                while x_k >= x2:
                    a[y_k,x_k] += 1
                    x_k -= 1
                    y_k -= 1

    print("Solution 2:", np.count_nonzero(a >= 2))

one()
two()