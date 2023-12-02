def process_input(input):
    moves = [m for m in input]
    return moves


def part1(input):
    moves = process_input(input)
    up = [m for m in moves if m == "("]
    down = [m for m in moves if m == ")"]
    final_floor = 0 + len(up) - len(down)
    return final_floor


def walk_moves(moves):
    start = 0
    for i, m in enumerate(moves):
        if m == "(":
            start = start + 1
        elif m == ")":
            start = start - 1
        if start < 0:
            return i + 1


def part2(input):
    moves = process_input(input)
    basement = walk_moves(moves)
    return basement


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
