for t in range(int(input())) :
    case = list(input())

    for i in range(len(case)) :
        if case[i] == 'b' : case[i] = 'd'
        elif case[i] == 'd' : case[i] = 'b'
        elif case[i] == 'p' : case[i] = 'q'
        else : case[i] = 'p'

    print(f'#{t+1} {"".join(reversed(case))}')