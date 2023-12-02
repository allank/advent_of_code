import hashlib

def find_key(secret_key, leader):
    num = 1
    while True:
        h = hashlib.md5()
        message = "{}{}".format(secret_key, str(num))
        h.update(bytes(message, 'utf-8'))
        if h.hexdigest()[:len(leader)] == leader:
            return num
        else:
            num = num + 1

def part1(input):
    return find_key(input, "00000")


def part2(input):
    return find_key(input, "000000")


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
