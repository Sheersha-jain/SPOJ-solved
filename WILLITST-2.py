# bitwise method for "https://www.spoj.com/problems/WILLITST/"
n = int(input())
if n & (n - 1) == 0:
    print('TAK')
else:
    print('NIE')
