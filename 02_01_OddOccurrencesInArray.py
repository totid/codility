import unittest


def solution(A):
    odd = 0
    for element in A:
        odd ^= element
    return odd


class TestOddOccurences(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(7, solution([9, 3, 9, 3, 9, 7, 9]))


if __name__ == '__main__':
    unittest.main()
