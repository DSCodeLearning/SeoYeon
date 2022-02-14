for t in range(int(input())) :
    case = dict()
    result = list()
    for i in input() :
        if i in case.keys() : case[i] += 1
        else : case[i] = 1

    for i in case.keys() :
        if case[i] % 2 != 0 : result.append(i)

    if len(result) == 0 : result = 'Good'
    else : result = ''.join(sorted(result))

    print(f'#{t+1} {result}')
