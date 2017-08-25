def counting(A, m):
    n = len(A)
    count = [0] * (m + 1)
    for k in range(n):
        count[A[k]] += 1
    return count


def slow_solution(A, B, m):
    n = len(A)
    sum_a = sum(A)
    sum_b = sum(B)
    for i in range(n):
        for j in range(n):
            change = B[j] - A[i]
            sum_a += change
            sum_b -= change
            if sum_a == sum_b:
                return True
            sum_a -= change
            sum_b += change
    return False


def fast_solution(A, B, m):
    n = len(A)
    sum_a = sum(A)
    sum_b = sum(B)
    d = sum_b - sum_a
    if d % 2 == 1:
        return False
    d //= 2
    count = counting(A, m)
    for i in range(n):
        if 0 <= B[i] - d <= m and count[B[i] - d] > 0:
            return True
    return False

v = [0, 0, 4, 2, 4, 5]
res = counting(v, max(v))
s = 0
for i, e in enumerate(res):
    s += i * e
    print("Count of", i, "=", e)
print(s == sum(v))
