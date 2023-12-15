import re

f = open('4.txt', 'r')

ret = 0

while True:
    line = f.readline().strip()
    if not line:
        break

    _, numsLeft, numsRight = re.split(':|\|', line)
    numMatches = len(set([int(n) for n in numsLeft.strip().split()]).intersection(set([int(n) for n in numsRight.strip().split()])))
    
    if numMatches:
        ret += 2**(numMatches-1)

print(ret)
f.close()
