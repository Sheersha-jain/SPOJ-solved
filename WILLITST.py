n = int(input())
while n > 1:
    if n % 2 != 0:
        print('NIE')
        break
    n = n / 2
else:
    print('TAK')
