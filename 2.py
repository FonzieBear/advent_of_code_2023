import re

f = open('2.txt', 'r')

ret = 0

cubes = {
  'red': 12,
  'green': 13,
  'blue': 14,
}

while True:
  line = f.readline()
  if not line:
    break

  tokens = re.split(':|;', line)

  gameId = int(tokens[0].split()[1])

  valid = True
  for token in tokens[1:]:
    draws = token.split(', ')
    for draw in draws:
      count, color = draw.strip().split()
      if cubes[color] < int(count):
        valid = False
        break

  if valid:
    ret += gameId

print(ret)
f.close()
