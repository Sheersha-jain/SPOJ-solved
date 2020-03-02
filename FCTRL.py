#https://www.spoj.com/problems/FCTRL

for _ in xrange(int(raw_input())):
    n = int(raw_input())
    a = 5
    r = 0
    while a <= n:
        r += n/a
        a *= 5
    print r
