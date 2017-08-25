import unittest
import random

N_RANGE = (2, 100000)
ELM_RANGE = (-1000, 1000)


def solution(A):
    N = len(A)
    if N == 0:
        return 0
    elif N == 1:
        return A[0]
    else:
        left = A[0]
        right = sum(A[1:])
        res = abs(left - right)
        for P in range(1, N - 1):
            left += A[P]
            right -= A[P]
            curr = abs(left - right)
            res = min(curr, res)
        return res


class TestTapeEquilibrium(unittest.TestCase):
    def test_double(self):
        self.assertEqual(2000, solution([-1000, 1000]))

    def test_example(self):
        self.assertEqual(1, solution([3, 1, 2, 4, 3]))

    def test_negative(self):
        self.assertEqual(20, solution([-10, -20, -30, -40, 100]))

    def test_none(self):
        self.assertEqual(0, solution([]))

    def test_single_element(self):
        vector = [1]
        elm = vector[0]
        self.assertEqual(elm, solution(vector))

    def test_random(self):
        N = random.randint(*N_RANGE)
        arr = [random.randint(*ELM_RANGE) for _ in range(N)]
        print(N, solution(arr), arr)

    def test_maximum(self):
        arr = [random.randint(*ELM_RANGE) for _ in range(N_RANGE[1])]
        print(N_RANGE[1], solution(arr), arr)


if __name__ == '__main__':
    unittest.main()
