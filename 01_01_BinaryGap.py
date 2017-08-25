import unittest

# the largest integer we have to deal with
MAXINT = 2147483647


def solution(N):
    # protect against crazy inputs
    if not isinstance(N, int):
        raise TypeError("Input must be an integer")
    if N < 1:
        raise ValueError("Input must be a positive integer")
    if N > MAXINT:
        raise ValueError("Input must be a positive integer less than 2,147,483,647")
    mx = 0
    count = 0
    found_one = False
    while N != 0:
        if N & 1 == 1:
            if not found_one:
                found_one = True
            else:
                mx = max(mx, count)
            count = 0
        else:
            count += 1
        N >>= 1
    return mx


class TestBinaryGap(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(5, solution(1041))

    def test_example2(self):
        self.assertEqual(0, solution(15))

    def test_extremes(self):
        self.assertEqual(0, solution(1))
        self.assertEqual(1, solution(5))
        self.assertEqual(0, solution(MAXINT))

    def test_trailing_zeros(self):
        self.assertEqual(solution(6), 0)
        self.assertEqual(solution(328), 2)

    def test_simple1(self):
        self.assertEqual(solution(9), 2)
        self.assertEqual(solution(11), 1)

    def test_simple2(self):
        self.assertEqual(solution(19), 2)
        self.assertEqual(solution(42), 1)

    def test_simple3(self):
        self.assertEqual(solution(1162), 3)
        self.assertEqual(solution(5), 1)

    def test_medium1(self):
        self.assertEqual(solution(51712), 2)
        self.assertEqual(solution(20), 1)

    def test_medium2(self):
        self.assertEqual(solution(561892), 3)
        self.assertEqual(solution(9), 2)

    def test_medium3(self):
        self.assertEqual(solution(66561), 9)

    def test_large1(self):
        self.assertEqual(solution(6291457), 20)

    def test_large2(self):
        self.assertEqual(solution(74901729), 4)

    def test_large3(self):
        self.assertEqual(solution(805306369), 27)

    def test_large4(self):
        self.assertEqual(solution(1376796946), 5)

    def test_large5(self):
        self.assertEqual(solution(1073741825), 29)

    def test_large6(self):
        self.assertEqual(solution(1610612737), 28)

    def test_non_int(self):
        self.assertRaises(TypeError, solution, 1.0)

    def test_zero(self):
        self.assertRaises(ValueError, solution, 0)

    def test_maxint_plus_one(self):
        self.assertRaises(ValueError, solution, 2147483648)


if __name__ == '__main__':
    unittest.main()
    solution(1)
