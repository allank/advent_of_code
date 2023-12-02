import unittest
import src.day_13 as day_13


class TestDay_13(unittest.TestCase):
    input = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""

    def test_part1(self):
        expected = None
        result = day_13.part1(self.input)
        self.assertEqual(result, expected)

    def test_part2(self):
        expected = None
        result = day_13.part2(self.input)
        self.assertEqual(result, expected)
