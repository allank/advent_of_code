import unittest
import src.day_04 as day


class TestDay_04(unittest.TestCase):
    input = "abcdef"

    def test_part1(self):
        expected = 609043
        result = day.part1(self.input)
        self.assertEqual(result, expected)

