import string
import copy


def process_input(input):
    lines = input.splitlines()
    peaks = []
    for line in lines:
        peaks.append([l for l in line])
    # peaks = [p for p in line for line in lines]
    return peaks


def print_grid(peaks):
    for r in peaks:
        print(" ".join(r))


def find_next_moves(peaks, current_position):
    heights = [l for l in string.ascii_lowercase]
    r, c = current_position[0], current_position[1]
    current_height = peaks[r][c]
    if current_height == "S":
        current_height = "a"
    heights.append("E")
    valid_heights = heights[: heights.index(current_height) + 2]
    next_moves = []
    # check up
    if r > 0 and peaks[r - 1][c] in valid_heights:
        next_moves.append([r - 1, c])
    # check down
    if r < len(peaks) - 1 and peaks[r + 1][c] in valid_heights:
        next_moves.append([r + 1, c])
    # check left
    if c > 0 and peaks[r][c - 1] in valid_heights:
        next_moves.append([r, c - 1])
    # check right
    if c < len(peaks[0]) - 1 and peaks[r][c + 1] in valid_heights:
        next_moves.append([r, c + 1])
    # print(current_height, valid_heights, next_moves)
    return next_moves


def process_paths(peaks, paths):
    new_paths = []
    for path in paths:
        next_steps = find_next_moves(peaks, path[-1])
        if len(next_steps) > 0:
            for step in next_steps:
                new_path = copy.deepcopy(path)
                # check the step is not already in our list of steps
                check_list = [tuple(s) for s in new_path]
                if tuple(step) not in check_list:
                    # print(tuple(step), " not in ", check_list)
                    new_path.append(step)
                    new_paths.append(new_path)
    return new_paths


def must_continue(peaks, paths):
    for path in paths:
        lp = path[-1]
        if peaks[lp[0]][lp[1]] == "E":
            return False
        else:
            return True


def find_route(peaks, paths):
    while must_continue(peaks, paths):
        print(len(paths))
        paths = process_paths(peaks, paths)
    return paths


def part1(input):
    peaks = process_input(input)
    rows = len(peaks)
    cols = len(peaks[0])
    start, end = [0, 0], [0, 0]
    for r, row in enumerate(peaks):
        if "S" in row:
            start = [r, row.index("S")]
        if "E" in row:
            end = [r, row.index("E")]
    move_grid = []
    for r in range(rows):
        col = []
        for c in range(cols):
            col.append(".")
        move_grid.append(col)
    paths = []
    paths.append([start])
    valid_paths = find_route(peaks, paths)
    for p in valid_paths:
        print(len(p))
        print(len(list(set([tuple(i) for i in p]))))
        print(p)
    path_lengths = [len(p) for p in valid_paths]
    print(max(path_lengths) - 1)


def part2(input):
    lines = process_input(input)
    return None


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
