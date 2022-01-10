for t in range(int(input())) :
    case = input()
    result = [0]*8

    print(f'#{t+1}')

    j = -1
    for i in range(6, -1, -2) :
        if i == 0 : temp = case[:j] # [:-4]
        else : temp = case[j-1:j]

        try :
            result[i] = int(temp) // 5
            result[i+1] = int(temp) % 5
        except ValueError :
            break
        j-=1

    for i in range(8) : print(result[i], end=' ')
    print()