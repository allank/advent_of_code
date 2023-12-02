import unittest
import src.day_05 as day_05


class TestDay_05(unittest.TestCase):
    input1 = "ugknbfddgicrmopn"
    input2 = "haegwjzuvuyypxyu"

    input3 = "uurcxstgmygtbstg"
    input4 = "qjhvhtzxzqqjkmpb"

    def test_part1(self):
        expected = 1
        result = day_05.part1(self.input1)
        self.assertEqual(result, expected)

    def test_part1b(self):
        expected = 0
        result = day_05.part1(self.input2)
        self.assertEqual(result, expected)

    def test_part2(self):
        expected = 0
        result = day_05.part2(self.input4)
        self.assertEqual(result, expected)
