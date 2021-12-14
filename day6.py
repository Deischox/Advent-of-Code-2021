from typing import Counter


def one():
    f = open('input/part1/day6.txt')
    lines = f.readlines()
    fish = lines[0].split(',')

    for i in range(len(fish)):
        fish[i] = int(fish[i])
    print(fish)
    for i in range(11):
        for n in range(len(fish)):
            fish[n] -= 1
            if fish[n] == -1:
                fish[n] = 6
                fish.append(8)
        print("After {} day: {}".format(i+1,fish))
    print("Number of Fish after 80 Days: {}".format(len(fish)) )

def two():
    f = open('input/part1/day6.txt')
    lines = f.readlines()
    fish = lines[0].split(',')

    for i in range(len(fish)):
        fish[i] = int(fish[i])
        counter = 0
        
        counter += fish[i]
        

    print(fish)

counter = 0

def calcChild(startNumber, daysLeft, currentDay, ALLDAYS):
    if daysLeft <= 0: 
        return 

    childs = 0
    if startNumber < daysLeft: childs+=1
    childs += abs(startNumber-(currentDay-daysLeft))//7

    for i in range(childs):
        if (startNumber+1+(i)*7) < ALLDAYS:
            global counter
            counter += 1
            calcChild(8,daysLeft-(startNumber+1+(i)*7),(startNumber+1+(i)*7)+currentDay,ALLDAYS)

calcChild(3,80,0,80)
calcChild(4,80,0,80)
calcChild(3,80,0,80)
calcChild(1,80,0,80)
calcChild(2,80,0,80)
print(counter)