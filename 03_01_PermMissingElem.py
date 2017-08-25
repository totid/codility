def solution(A):
    n = len(A)
    if n < 1:
        return 1
    else:
        expected = (n + 1) * (n + 2) // 2
        return expected - sum(A)

if __name__ == '__main__':
    A = []
    print(solution(A))
