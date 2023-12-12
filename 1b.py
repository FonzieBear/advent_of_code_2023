f = open('1.txt', 'r')
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']

total = 0

while True:
  line = f.readline()
  if not line:
    break

  done = False
  while line:
    for index, number in enumerate(numbers):
      if line.startswith(number):
        total += 10 * int(index % 9 + 1)
        done = True
        break

    if done:
      break

    line = line[1:]

  done = False
  while line:
    for index, number in enumerate(numbers):
      if line.endswith(number):
        total += int(index % 9 + 1)
        done = True
        break

    if done:
      break
    line = line[:-1]

  print(total)

print(total)
f.close()
