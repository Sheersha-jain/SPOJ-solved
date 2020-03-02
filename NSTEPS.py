#https://www.spoj.com/problems/NSTEPS/

for _ in xrange(int(raw_input())):
    x, y = map(int, raw_input().split())
    if x == y or x == y + 2:
        print x + y - (x % 2)
    else:
        print 'No Number'
