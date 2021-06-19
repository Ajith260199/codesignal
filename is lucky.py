def isLucky(n):
    s = str(n)
    part1 = sum([int(i) for i in list(s[0:int(len(s)/2)])])
    part2 = sum([int(i) for i in list(s[int(len(s)/2):len(s)])])
    return part1==part2
    
