import functools
#import sys


@functools.lru_cache(maxsize=10**9)
def value(n):
    if n < 12:
        return n
    return max(n, value(n // 2) + value(n // 3) + value(n // 4))


# for i in map(int, sys.stdin.read().split()):
#     print(value(i))

try:
    while True:
        print(value(int(input())))
except EOFError:
    pass 
