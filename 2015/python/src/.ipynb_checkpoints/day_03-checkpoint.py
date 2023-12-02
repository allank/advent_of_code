def process_input(input):
    moves = [m for m in input]
    return moves

def process_moves(current_house, moves):
    houses = [
        current_house
    ]
    for move in moves:
        if move == '<':
            # decrement col
            current_house = [current_house[0] + 1, current_house[1]]
        elif move == '>':
            # increment col
            current_house = [current_house[0] - 1, current_house[1]]
        elif move == '^':
            # decrement row
            current_house = [current_house[0], current_house[1] - 1]
        elif move == 'v': # move == 'v'
            # increment row
            current_house = [current_house[0], current_house[1] + 1]
        else:
            pass
        houses.append(current_house)
    return houses

def part1(input):
    moves = process_input(input)
    return len(set(map(tuple, process_moves([0,0], moves))))


def part2(input):
    moves = process_input(input)
    santa = moves[::2]
    robo = moves[1::2]
    all_houses = process_moves([0,0], santa)
    all_houses.extend(process_moves([0,0], robo))
    return len(set(map(tuple,all_houses)))


if __name__ == "__main__":
    # get day number
    day = __file__.split(".")[0].split("_")[-1]
    # get raw input
    with open(f"data/input_{day}.txt", "r") as f:
        input = f.read()
    # TODO: if function returns 0 then this will not print ....
    if result_one := part1(input):
        print(f"Part 1: {result_one}")
    if result_two := part2(input):
        print(f"Part 2: {result_two}")
