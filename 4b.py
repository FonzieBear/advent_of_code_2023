import re

f = open('4.txt', 'r')

ret = 0
copies = []

while True:
    line = f.readline().strip()
    if not line:
        break

    copiesOfThis = 1
    if len(copies):
        copiesOfThis += copies[0]
        copies = copies[1:]

    ret += copiesOfThis

    _, numsLeft, numsRight = re.split(':|\|', line)
    numMatches = len(set([int(n) for n in numsLeft.strip().split()]).intersection(set([int(n) for n in numsRight.strip().split()])))

    for i in range(numMatches):
        if i > len(copies) - 1:
            copies.append(copiesOfThis)
        else:
            copies[i] += copiesOfThis

print(ret)
f.close()
