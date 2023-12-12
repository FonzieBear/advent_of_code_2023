f = open('1.txt', 'r')
chars = 'abcdefghijklmnopqrstuvwxyz\n'
total = 0

while True:
  line = f.readline()
  if not line:
    break

  new_line = line.strip(chars)

  if new_line:
    total += 10*int(new_line[0]) + int(new_line[-1])

print(total)
f.close()
