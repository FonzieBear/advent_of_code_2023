import re

f = open('3.txt', 'r')

nums = '0123456789'

ret = 0

prev_symbols = set()
prev_parts = []

while True:
    line = f.readline().strip()
    if not line:
        break

    new_parts = []
    new_symbols = set()

    num_index = 0
    num_string = ''
    last_symbol_index = -1

    for i, c in enumerate(line):
        if c == '.':
            if num_string:
                # See if there was a symbol immediately before
                # See if it's adjacent to a symbol from the previous row
                if (last_symbol_index >= 0 and num_index == last_symbol_index + 1) or len(prev_symbols.intersection(set([j + num_index - 1 for j in range(len(num_string)+2)]))):
                    ret += int(num_string)
                else:
                    new_parts.append((num_index, num_string))
                num_string = ''
        elif c in nums:
            if not num_string:
                num_index = i
            num_string += c
        else:
            # This is a symbol
            if num_string:
                ret += int(num_string)
                num_string = ''

            # See if this activated any parts in the previous row
            for part_index, part in enumerate(prev_parts):
                if not part:
                    continue

                part_start, part_string = part
                if i in [j + part_start - 1 for j in range(len(part_string) + 2)]:
                    ret += int(part_string)

                    # Make sure a part does not get activated twice.
                    prev_parts[part_index] = None

            new_symbols.add(i)
            last_symbol_index = i

    # Check whether the line ended with a string
    if num_string:
        # See if there was a symbol immediately before
        # See if it's adjacent to a symbol from the previous row
        if (last_symbol_index >= 0 and num_index == last_symbol_index + 1) or len(prev_symbols.intersection(set([j + num_index - 1 for j in range(len(num_string)+2)]))):
            ret += int(num_string)
        else:
            new_parts.append((num_index, num_string))

    prev_symbols = new_symbols
    prev_parts = new_parts

print(ret)
f.close()
