for t in range(int(input())) :
    case = [list(map(int, input().split())) for i in range(9)]
    case_transposed = [list(range(9)) for i in range(9)]
    result = 0

    temp2 = []
    for n in range(0, 7, 3):
        for y in range(0, 7, 3):
            temp = 0
            for x in range(3): temp += sum(case[x + y][y:y + 3])
            temp2.append(temp)

    for i in range(9) :
        for j in range(9) :
            case_transposed[i][j] = case[j][i]
        if sum(case_transposed[i])*9 == sum(case[i])*9 == temp2[0]*9 == sum(temp2) : result = 1
        else :
            result = 0
            break

    print(f'#{t+1} {result}')

