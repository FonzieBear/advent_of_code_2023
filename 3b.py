import re

f = open('3.txt', 'r')

nums = '0123456789'

ret = 0

prev_parts = []

gear_map = {}

row = 0
while True:
    line = f.readline().strip()
    if not line:
        break
    row += 1

    new_parts = []

    num_index = 0
    num_string = ''

    for i, c in enumerate(line):
        if not c in nums and num_string:
            # Just finished a number. Update any gears that were activated.
            for j in range(num_index - 1, num_index + len(num_string) + 1):
                if (row-1, j) in gear_map:
                    gear_map[(row-1, j)].append(int(num_string))
            if (row, num_index - 1) in gear_map:
                gear_map[(row, num_index - 1)].append(int(num_string))

            new_parts.append((num_index, num_string))
            num_string = ''

        if c == '*':
            gear_map[(row, i)] = []

            # Look above for parts
            for part_start, part_string in prev_parts:
                if not (part_start + len(part_string) < i or part_start > i + 1):
                    gear_map[(row, i)].append(int(part_string))

            if len(new_parts) and new_parts[-1][0] + len(new_parts[-1][1]) == i:
                gear_map[(row, i)].append(int(new_parts[-1][1]))

        if c in nums:
            if not num_string:
                num_index = i
            num_string += c

    # Check whether the line ended with a number
    if num_string:
        # Just finished a number. Update any gears that were activated.
        for j in range(num_index - 1, num_index + len(num_string) + 1):
            if (row-1, j) in gear_map:
                gear_map[(row-1, j)].append(int(num_string))
        if (row, num_index - 1) in gear_map:
            gear_map[(row, num_index - 1)].append(int(num_string))

        new_parts.append((num_index, num_string))

    prev_parts = new_parts

for gear in gear_map:
    if (len(gear_map[gear]) == 2):
        ret += gear_map[gear][0] * gear_map[gear][1]

print(ret)
f.close()
