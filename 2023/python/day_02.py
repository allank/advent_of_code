def input():
#     part 1 test
#     return """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
    # part 2 test
#     return """two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen"""
    # input data
    with open('input_02.txt', 'r') as file:
        return file.read()
    
    
def part_01(input):
    sum = 0
    games = {}
    for line in input.split("\n"):
        gb = line.split(":")
        game_number = gb[0].split(" ")[1].strip()
        game_possible = []
        pulls = []
        game_pulls = [bb.strip() for bb in gb[1].split(";")]
        for game_pull in game_pulls:
            boxes_pulled = [gp.strip() for gp in game_pull.split(",")]
            boxes = {}
            for box in boxes_pulled:
                temp = box.split(" ")
                boxes[temp[1].strip()] = int(temp[0].strip())
                game_possible.append(is_possible(temp[1].strip(), int(temp[0].strip())))
            pulls.append(boxes)
        games[game_number] = pulls
        if all(game_possible):
            sum = sum + int(game_number)
    return sum     

def is_possible(color, count):
    if color == "red" and count <= 12:
        return True
    elif color == "green" and count <= 13:
        return True
    elif color == "blue" and count <= 14:
        return True
    else:
        return False
    
def part_02(input):
    from functools import reduce
    games = {}
    game_powers = []
    for line in input.split("\n"):
        gb = line.split(":")
        game_number = gb[0].split(" ")[1].strip()
        game_possible = []
        pulls = []
        game_pulls = [bb.strip() for bb in gb[1].split(";")]
        temp_dict = { 'red': [], 'blue': [], 'green': [] }
        for game_pull in game_pulls:
            boxes_pulled = [gp.strip() for gp in game_pull.split(",")]
            boxes = {}
            for box in boxes_pulled:
                temp = box.split(" ")
                boxes[temp[1].strip()] = int(temp[0].strip())
                game_possible.append(is_possible(temp[1].strip(), int(temp[0].strip())))
                temp_dict[temp[1].strip()].append(int(temp[0].strip()))
            pulls.append(boxes)
        games[game_number] = pulls
        ops = [max(v) for k, v in temp_dict.items()]
        game_powers.append(reduce((lambda x, y: x * y), ops))
    return sum(game_powers)

print(part_01(input()))
print(part_02(input()))