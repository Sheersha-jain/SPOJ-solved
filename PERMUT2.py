while True:
    n = int(input())
    if n == 0:
        break
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[a[i] - 1] = i + 1
    if a == b:
        print('ambiguous')
    else:
        print('not ambiguous')
