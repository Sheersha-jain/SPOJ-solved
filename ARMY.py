for _ in range(int(input())):
    input()
    godzilla_num, mechagodzilla_num = map(int, input().split())
    godzilla_army = max(list(map(int, input().split())))
    mechagodzilla_army = max(list(map(int, input().split())))
    if godzilla_army < mechagodzilla_army:
        print('MechaGodzilla')        
    else:
        print('Godzilla')
