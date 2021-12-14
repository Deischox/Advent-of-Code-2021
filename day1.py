def part1():
    with open('input/part1/day1input.txt') as f:
        line = f.readlines()
    a = [i.split('\n', 1)[0] for i in line]
    i = 0
    last = 10000000
    c = 0
    while i < len(a):
        if int(a[i]) > last:
            c += 1
        last = int(a[i])
        i+=1
    print(c)

def part2():
    with open('input/part2/day1input.txt') as f:
        line = f.readlines()
    a = [i.split(' ')[0] for i in line]
    a = [int(i) for i in a]
    i = 0
    c = 0
    while i+3 < len(a):
        if sum(a[i:i+3]) < sum(a[i+1:i+4]):
            c+=1
        i+=1
    print(c)
              
part2()
