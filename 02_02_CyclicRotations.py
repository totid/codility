import unittest
import random

ARRAY_RANGE = (-1000, 1000)
INT_RANGE = (0, 100)


def solution(A, K):
    l = len(A)
    if l == 0:
        return []
    else:
        shifts = (-K % l)
        return A[shifts:] + A[:shifts]


class TestCyclicRotation(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(solution([6, 3, 8, 9, 7], 0), [6, 3, 8, 9, 7])

    def test_one(self):
        self.assertEqual(solution([6, 3, 8, 9, 7], 1), [7, 6, 3, 8, 9])

    def test_example1(self):
        self.assertEqual(solution([3, 8, 9, 7, 6], 3), [9, 7, 6, 3, 8])

    def test_full(self):
        self.assertEqual(solution([6, 3, 8, 9, 7], 5), [6, 3, 8, 9, 7])

    def test_empty(self):
        self.assertEqual(solution([], 5), [])

    def test_random(self):
        N = random.randint(*INT_RANGE)
        K = random.randint(*INT_RANGE)
        A = [random.randint(*ARRAY_RANGE) for _ in range(0, N)]
        print(N, K, A)
        print(solution(A, K))


if __name__ == '__main__':
    unittest.main()
