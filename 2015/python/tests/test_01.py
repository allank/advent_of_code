import unittest
import src.day_01 as day_01


class TestDay_01(unittest.TestCase):
    input = "))((((("
    input_2 = "()())"

    def test_part1(self):
        expected = 3
        result = day_01.part1(self.input)
        self.assertEqual(result, expected)

    def test_part2(self):
        expected = 5
        result = day_01.part2(self.input_2)
        self.assertEqual(result, expected)
