import re

def input():

#     return """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

#     return """"""

    with open('input_04.txt', 'r') as file:
        return file.read()
  


def part_01(input):
    import functools
    sum = 0
    for line in input.split("\n"):
        haves = line.split("|")[0].split(":")[1].strip().split()
        draws = line.split("|")[1].strip().split()
        matches = list(set(haves).intersection(set(draws)))
        if matches:
            matches[0] = 1
            points = functools.reduce(lambda a, b: a*2, matches)
            sum = sum + points
    return sum     

    
def part_02(input):
    sum = 0
    cards = {}
    lines = input.split("\n")
    for line_number, line in enumerate(lines):
        card_num = line_number + 1
        current_cards = cards.get(card_num, 1)
        haves = line.split("|")[0].split(":")[1].strip().split()
        draws = line.split("|")[1].strip().split()
        matches = list(set(haves).intersection(set(draws)))
        sum = sum + current_cards
        if matches:
            for i in range(0, len(matches)):
                if cards.get(card_num + i + 1):
                    cards[card_num + i + 1] = cards[card_num + i + 1] + current_cards
                else:
                    cards[card_num + i + 1] = current_cards + 1
    return sum

print(part_01(input()))
print(part_02(input()))

