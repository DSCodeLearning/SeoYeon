for t in range(int(input())) :
    N, K = map(int, input().split())
    case = ["".join(list(map(str,input().split()))) for i in range(N)]

    case_transposed = []
    for i in range(N):
        row = list()
        for sublist in case: row.append(sublist[i])
        case_transposed.append("".join(row))

    case = [case[i].split('0') for i in range(N)]
    case_transposed = [case_transposed[i].split('0') for i in range(N)]

    result = 0
    temp = '1'*K
    for i in range(N) :
        for j in case[i] :
            if j == temp : result += 1
        for j in case_transposed[i] :
            if j == temp : result += 1

    print(f'#{t+1} {result}')