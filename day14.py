def one():
    f = open('day14.txt')
    lines = f.readlines()
    lines = [i.split('\n')[0] for i in lines]
    start = lines[0]

    element = start
    lines.remove(start)
    lines.remove('')

    rules = [i.split(' -> ')[0] for i in lines]
    to = [i.split(' -> ')[1] for i in lines]

    for u in range(10):
        print(u)
        new = ""
        for i in range(len(start)):
           
            if start[i:i+2] in rules:
                new += start[i] + to[rules.index(start[i:i+2])]
            else:
                new += start[i]
        
        start = new
    
    keys = set([i for i in list(element) if list(element).count(i) > 0])
    a = []
    for k in keys:
        a.append(start.count(k))
    
    print("Value: {}".format(max(a)-min(a)))

one()