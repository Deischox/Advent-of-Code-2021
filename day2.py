file = open("input/part1/day2.txt", 'r')
h = 0
d = 0
aim = 0
for line in file:
    if line.split(' ')[0] == "up":
        aim -= int(line.split(' ')[1])
    elif line.split(' ')[0] == "down":
        aim += int(line.split(' ')[1])
    elif line.split(' ')[0] == "forward":
        h += int(line.split(' ')[1])
        d += (aim*int(line.split(' ')[1]))
print(h*d)