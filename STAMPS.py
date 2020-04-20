for t in range(1, int(input()) +1 ):
    stamps_needed, friends = map(int, input().split()) 
    potential_stamps = list(map(int, input().split()))
    current_stamps = 0
    friends_donated = 0
    for i in sorted(potential_stamps, reverse= True):
        current_stamps += i
        friends_donated += 1
        if current_stamps >= stamps_needed:
            break
    print('Scenario #%s:' %t)
    if current_stamps >= stamps_needed:
        print(friends_donated)
    else:
        print('impossible')
    print
