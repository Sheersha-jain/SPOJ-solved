for _ in range(int(input())):
    n = int(input())
    print((3 * n * (n + 1) // 2 - n) % (10**6 + 7))
