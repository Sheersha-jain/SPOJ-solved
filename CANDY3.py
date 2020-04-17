def equal_divide_possibility(array):
    if sum(array) % len(array) == 0:
        print('YES')
    else:
        print('NO')

for _ in range(int(input())):
    input()
    n = int(input())
    candies = [int(input()) for _ in range(n)]
    equal_divide_possibility(candies)
