def process_input(input):
    pairs = input.split("\n\n")
    list_pairs = []
    for pair in pairs:
        signals = pair.splitlines()
        list_pairs.append({"left": eval(signals[0]), "right": eval(signals[1])})
    return list_pairs


def check_order(pair):
    pass


def part1(input):
    list_pairs = process_input(input)
    correct = []
    for index, pair in enumerate(list_pairs):
        order = []
        for l, r in zip(pair["left"], pair["right"]):
            if isinstance(l, int) and isinstance(r, int):
                if l == r:
                    pass
                elif l < r:
                    order.append(True)
                else:
                    order.append(False)
        print("order", order)
        if all(order):
            correct.append(index)
    print(correct)
    return None


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
