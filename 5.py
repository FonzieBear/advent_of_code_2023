import re
import sys

f = open('5.txt', 'r')

seeds = list(map(int, f.readline().strip()[7:].split()))

maps = []

def readMap(f):
    m = []
    line = None
    while not line:
        line = f.readline().strip()
    
    # Skip map title
    line = f.readline().strip()

    while line:
        m.append(list(map(int, line.split())))
        line = f.readline().strip()

    return m

for i in range(7):
    maps.append(readMap(f))

ret = sys.maxsize
for seed in seeds:
    result = seed
    for m in maps:
        for mapping in m:
            if result >= mapping[1] and result < mapping[1] + mapping[2]:
                result = mapping[0] + result - mapping[1]
                break
    
    ret = min(ret, result)

print(ret)
f.close()
