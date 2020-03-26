count = 0
for i in range(1, int(input()) + 1):
    for j in range(1, int(i**0.5) + 1):
        if i%j == 0:
            count += 1
print(count)
