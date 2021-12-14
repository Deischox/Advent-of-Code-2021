file = open("input/part1/day3.txt", 'r')
def one():
    lines = file.readlines()
    lines = [i.split('\n')[0] for i in lines]
    i = 0
    gamma = ""
    while i < len(lines[0]):
        bit = [c[i] for c in lines]
        gamma += max(set(bit), key = bit.count)
        i+=1
    delta = gamma.replace('1','2')
    delta = delta.replace('0','1')
    delta = delta.replace('2','0')
    print(int(gamma,2)*int(delta,2))
def two():
    lines = file.readlines()
    lines = [i.split('\n')[0] for i in lines]
    i = 0
    gamma = ""
    r = set()
    while i < len(lines[0])-1 or len(r) == len(lines)-1:
        bit = [c[i] for c in lines]
        gamma = max(set(bit), key = bit.count)
        for l in lines:
            if l[i] != gamma:
                r.add(l)
        i+=1
    print(r)
    l = set(lines)
    print(l.difference(r))

    r = set()
    while i < len(lines[0])-1 or len(r) == len(lines)-1:
        bit = [c[i] for c in lines]
        gamma = max(set(bit), key = bit.count)
        for l in lines:
            if l[i] == gamma:
                r.add(l)
        i+=1
    print("2:",r)
    l = set(lines)
    print(r.difference(l))

two()