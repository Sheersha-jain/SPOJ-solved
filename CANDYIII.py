for _ in range(int(input())):
    input()
    n = int(input())
    candies = [int(input()) for _ in range(n)]
    if sum(candies) % len(candies) == 0:
        print('YES')
    else:
        print('NO')
