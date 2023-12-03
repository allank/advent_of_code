import re

def input():

#     return """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# .......755
# ...$..*...
# .664.598.."""

#     return """"""

    with open('input_03.txt', 'r') as file:
        return file.read()
  

def is_part(characters):
    characters = [c for c in characters if not c.isdigit()]
    characters = [c for c in characters if c != "."]
    if len(characters) > 0:
        return True
    else:
        return False

def part_01(input):
    sum = 0
    lines = input.split("\n")
    for line_num, line in enumerate(lines):
        part_nums = re.findall(r'\d+', line)
        start_pos = 0
        for part in part_nums:
            start_pos = line.find(part, start_pos)
            characters = []
            for i in range(line_num-1, line_num+2):
                for j in range(start_pos-1, start_pos + len(part) + 1):
                    if i >= 0 and i < len(lines)  and j >=0 and j < len(line):
                        characters.append(lines[i][j])
            start_pos = start_pos + len(part)
            if is_part(characters):
                sum = sum + int(part)
    return sum     

    
def part_02(input):
    sum = 0
    gears = {}
    lines = input.split("\n")
    for line_num, line in enumerate(lines):
        part_nums = re.findall(r'\d+', line)
        start_pos = 0
        for part in part_nums:
            start_pos = line.find(part, start_pos)
            characters = []
            for i in range(line_num-1, line_num+2):
                for j in range(start_pos-1, start_pos + len(part) + 1):
                    if i >= 0 and i < len(lines)  and j >=0 and j < len(line):
                        if lines[i][j] == "*":
                            if (i, j) in gears:
                                gears[(i, j)].append(part)
                            else:
                                gears[(i, j)] = [part]
            start_pos = start_pos + len(part)
    for gear, parts in gears.items():
        if len(parts) == 2:
            sum = sum + (int(parts[0]) * int(parts[1]))
    return sum  

print(part_01(input()))
print(part_02(input()))