for _ in range(int(input())):
    third, last_third, ap_sum = map(int, input().split())
    total = 2*ap_sum // (third + last_third)
    print(total)
    difference = (last_third - third) // (total -5)
    a = third - 2* difference
    j = 0
    for j in range(total - 1):
        print(a, end= " ")
        a += difference
    print(a)
