def solution(X, Y , D):
    if (Y - X) % D == 0:
        return (Y - X) // D
    else:
        return (Y - X) // D + 1


if __name__ == '__main__':
    print(solution(10, 85, 30))
    print(solution(2, 11, 3))