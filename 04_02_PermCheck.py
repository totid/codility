import unittest


def solution(A):
    return 1 if set(A) == set(range(1, len(A) + 1)) else 0


class TestPermCheck(unittest.TestCase):
    def test_permutation_present(self):
        self.assertTrue(solution([4, 1, 3, 2]))

    def test_permutation_not_present(self):
        self.assertFalse(solution([4, 1, 3]))

    def test_repeated_elements(self):
        self.assertFalse(solution([2, 2]), 0)


if __name__ == '__main__':
    unittest.main()