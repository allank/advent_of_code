import unittest
import src.day_12 as day_12


class TestDay_12(unittest.TestCase):
    input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

    def test_part1(self):
        expected = None
        result = day_12.part1(self.input)
        self.assertEqual(result, expected)

    def test_part2(self):
        expected = None
        result = day_12.part2(self.input)
        self.assertEqual(result, expected)
