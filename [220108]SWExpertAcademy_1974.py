for t in range(int(input())) :
    case = [list(map(int, input().split())) for i in range(9)]
    print(case)
    result = 0
    temp = int()
    for i in range(9) :
        case_transposed = []

        for j in range(9) :
            case_transposed.append(case[j][i])
            for x in range(3) :
                for y in range(3) :

            # temp = 0
            # for m in range(9) :
            #     for n in range(0,7,3) :
            #         print(case[m][n:n+3])
            #         temp += sum(case[m][n:n+3])
            #     print(temp)
            # if temp == sum(case[i]) : result = 1

        if sum(case_transposed) == sum(case[i]) == temp : result = 1

    print(f'#{t+1} {result}')

