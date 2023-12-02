def process_input(input):
    lines = input.splitlines()
    return lines


def test_vowels(letters):
    vowels = ["a", "e", "i", "o", "u"]
    valid = [l for l in letters if l in vowels]
    return True if len(valid) >= 3 else False


def sliding_window(elements, window_size):
    if len(elements) <= window_size:
        return elements
    windows = []
    for i in range(len(elements)):
        windows.append(elements[i : i + window_size])
    return windows


def double_letters(letters):
    windows = sliding_window(letters, 2)
    for window in windows:
        if len(window) >= 2:
            if window[0] == window[1]:
                return True
    return False


def enumerate_double_letters(letters):
    windows = sliding_window(letters, 2)
    windows = [tuple(w) for w in windows if len(w) > 1]
    doubles = {}
    for window in windows:
        if doubles.get(window):
            doubles[window] = doubles[window] + 1
        else:
            doubles[window] = 1
    test_doubles = []
    for k, v in doubles.items():
        if v >= 2:
            test_doubles.append(k)

    if len(test_doubles) > 0:
        for double in test_doubles:
            indexes = []
            for i, d in enumerate(windows):
                if d == double:
                    indexes.append(i)
            diff_list = []
            for x, y in zip(indexes[0::], indexes[1::]):
                diff_list.append(y - x)
            if 1 in diff_list:
                return False
        return True
    else:
        return False


def test_exclusions(letters):
    exclusions = ["ab", "cd", "pq", "xy"]
    letters_string = "".join(letters)
    return not any([e in letters_string for e in exclusions])


def process_line(line):
    letters = [l for l in line]
    return letters


def run_test(letters):
    return [test_vowels(letters), double_letters(letters), test_exclusions(letters)]


def part1(input):
    lines = process_input(input)
    lines_status = []
    for line in lines:
        letters = process_line(line)
        if all(run_test(letters)):
            lines_status.append("nice")
        else:
            lines_status.append("naughty")
    return len([l for l in lines_status if l == "nice"])


def part2(input):
    lines = process_input(input)
    for line in lines:
        letters = process_line(line)
        print(enumerate_double_letters(letters))
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
