def one(amount):
    f = open('day6.txt').read().splitlines()
    fish = dict([(c, f[0].split(',').count(str(c))) for c in range(9)])
    for i in range(amount):
        t = fish.copy()
        for f in range(9):
            if f < 8:
                fish[f] = t[f+1]
            else:
                fish[8] = t[0]  
            if f == 6:
                fish[6] += t[0]  
    print(sum(fish.values()))
one(80)
one(256)
