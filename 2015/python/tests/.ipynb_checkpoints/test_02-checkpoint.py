import unittest
import src.day_02 as day


class TestDay_01(unittest.TestCase):
    input = "2x3x4"

    def test_part1(self):
        expected = 58
        result = day.part1(self.input)
        self.assertEqual(result, expected)

    def test_part2(self):
        expected = 34
        result = day.part2(self.input)
        self.assertEqual(result, expected)
