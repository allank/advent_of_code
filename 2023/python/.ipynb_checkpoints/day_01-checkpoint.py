def input():
    # part 1 test
#     return """1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet"""
    # part 2 test
#     return """two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen"""
    # input data
    with open('input_01.txt', 'r') as file:
        return file.read()
    
    
def part_01(input):
    sum = 0 
    for line in input.split("\n"):
        digits = [c for c in line if c.isdigit()]
        sum += int("{}{}".format(digits[0], digits[-1]))
    return sum 

def part_02(input):
    sum = 0
    find = [
        ("one","1"),
        ("two","2"),
        ("three","3"),
        ("four","4"),
        ("five","5"),
        ("six","6"),
        ("seven","7"),
        ("eight","8"),
        ("nine","9"),
    ]   
    for line in input.split("\n"):
        first_digit = None
        last_digit = None
        for i in range(1, len(line)+1):
            if not first_digit:
                if line[i-1].isdigit():
                    first_digit = line[i-1]
                for r in find:
                    if r[0] in line[0:i]:
                        first_digit = r[1]
        for i in range(len(line), 0, -1):
            if not last_digit:
                if line[i-1].isdigit():
                    last_digit = line[i-1]
                for r in find:
                    if r[0] in line[i-1:]:
                        last_digit = r[1]
        sum = sum + int("{}{}".format(first_digit, last_digit))
    return sum


print(part_01(input()))
print(part_02(input()))
    
