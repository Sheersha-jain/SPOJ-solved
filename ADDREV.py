#https://www.spoj.com/problems/ADDREV/


for _ in xrange(int(raw_input())):
    a, b = map(int, raw_input().split())
    print int(str(int(str(a)[::-1]) + int(str(b)[::-1]))[::-1])
