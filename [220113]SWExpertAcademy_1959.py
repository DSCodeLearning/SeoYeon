for t in range(int(input())) :
    N, M = map(int, input().split())
    NList = list(map(int, input().split()))
    MList = list(map(int, input().split()))
    if N>M : N, M, NList, MList = M, N, MList, NList

    result = 0
    for i in range(M-N+1) :
        temp = 0
        for j in range(N) : temp += NList[j]*MList[j+i]
        result = max(result, temp)

    print(f'#{t+1} {result}')