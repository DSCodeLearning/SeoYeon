for t in range(int(input())) :
    case = dict()

    for a in input() :
        if a in list(case.keys()) :case[a] += 1
        else : case[a] = 1

    if len(list(case.keys())) != 2 : result = 'No'
    elif list(case.values()) != [2, 2] : result = 'No'
    else : result = 'Yes'

    print(f'#{t+1} {result}')