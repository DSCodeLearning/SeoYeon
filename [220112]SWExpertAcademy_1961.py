def TurnList90(case) :
    return list(zip(*case[::-1]))

for t in range(int(input())) :
    N = int(input())
    case = [list(map(int, input().split())) for i in range(N)]
    result = [TurnList90(case), TurnList90(TurnList90(case)), TurnList90(TurnList90(TurnList90(case)))]

    print(f'#{t + 1}')
    for i in range(N) :
        for j in range(3) :
            for k in range(N) :
                print(f'{result[j][i][k]}', end='')
            print(end=' ')
        print()