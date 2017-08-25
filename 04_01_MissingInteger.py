import unittest

N_RANGE = (1, 100000)
ELEMENT_RANGE = (-2147483648, 2147483647)


def counting(A, m):
    n = len(A)
    count = [0] * (m + 2)
    for k in range(n):
        if A[k] >= 0:
            count[A[k]] += 1
    return count


def solution(A):
    count = counting(A, max(A))
    sz = len(count)
    res = 0
    if sz == 1 and count[0] == 0:
        res = 1
    else:
        for i in range(1, sz):
            if count[i] == 0:
                res = i
                break
    return res


class TestMissingInteger(unittest.TestCase):
    def test_example_1(self):
        a = [1, 3, 6, 4, 1, 2]
        self.assertEqual(solution(a), 5)

    def test_example_2(self):
        a = [1, 2, 3]
        self.assertEqual(solution(a), 4)

    def test_consecutive_duplicates(self):
        a = [1, 1, 1, 2, 2, 2, 2]
        self.assertEqual(solution(a), 3)

    def test_duplicates(self):
        a = [1, 1, 1, 4, 4, 4, 4]
        self.assertEqual(solution(a), 2)

    def test_single_lower(self):
        a = [1]
        self.assertEqual(solution(a), 2)

    def test_single_upper(self):
        a = [2]
        self.assertEqual(solution(a), 1)

    def test_negative(self):
        self.assertEqual(solution([-1, 0, 1, 2, 3, 4, 5, 6, 10, 1000]), 7)

    def test_negative_two_elements(self):
        self.assertEqual(solution([-1, 10]), 1)

    def test_negative_single(self):
        self.assertEqual(solution([-1]), 1)

    def test_negative_many(self):
        self.assertEqual(solution([-1, -3, -10]), 1)

if __name__ == '__main__':
    unittest.main()
