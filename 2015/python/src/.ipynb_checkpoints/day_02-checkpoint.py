import math


def process_input(input):
    boxes = input.splitlines()
    box_data = []
    for box in boxes:
        lengths = box.split("x")
        box_data.append(
            {
                "l": int(lengths[0]),
                "w": int(lengths[1]),
                "h": int(lengths[2]),
            }
        )
    return box_data


def part1(input):
    boxes = process_input(input)
    total = 0
    for box in boxes:
        sides = []
        sides.append(box["l"] * box["w"])
        sides.append(box["w"] * box["h"])
        sides.append(box["h"] * box["l"])
        total = total + min(sides) + (2 * sum(sides))
    return total


def part2(input):
    boxes = process_input(input)
    total = 0
    for box in boxes:
        sides = sorted(list(box.values()))
        total = total + math.prod(sides) + (sum(sides[:2]) * 2)
    return total


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
