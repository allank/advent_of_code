import unittest
import src.day_03 as day


class TestDay_03(unittest.TestCase):
    input = "^v^v^v^v^v"

    def test_part1(self):
        expected = 2
        result = day.part1(self.input)
        self.assertEqual(result, expected)

    def test_part2(self):
        expected = 11
        result = day.part2(self.input)
        self.assertEqual(result, expected)
