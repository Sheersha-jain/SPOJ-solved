https://www.spoj.com/problems/PRIME1/


def is_prime(n):
    if n < 2:
        return False
    if n < 4 :
        return True
    if n % 2 == 0:
        return False
    for i in xrange(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

for _ in xrange(int(raw_input())):
    a, b = map(int, raw_input().split())
    for i in xrange(a, b + 1):
        if is_prime(i):
            print i
    print
