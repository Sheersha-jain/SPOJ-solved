def power(a, b, mod):
    if a == 0:
        return 0
    if b == 0:
        return 1 % mod
    if b%2 == 0:
        return power(a*a % mod, b//2, mod)
    return power(a*a % mod, b//2, mod) * a % mod


for _ in range(int(input())):
    a, b = map(int, input().split())
    print(power(a, b, 10))
