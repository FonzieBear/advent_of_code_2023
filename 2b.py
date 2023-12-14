import re

f = open('2.txt', 'r')

ret = 0

while True:
  line = f.readline()
  if not line:
    break

  max_cubes = {
    'red': 0,
    'green': 0,
    'blue': 0,
  }
  tokens = re.split(':|;', line)

  valid = True
  for token in tokens[1:]:
    draws = token.split(', ')
    for draw in draws:
      count, color = draw.strip().split()
      max_cubes[color] = max(max_cubes[color], int(count))

  ret += max_cubes['red'] * max_cubes['green'] * max_cubes['blue']

print(ret)
f.close()
