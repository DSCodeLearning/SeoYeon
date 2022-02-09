for t in range(int(input())) :
    N = int(input())
    case = list(map(int, input().split()))
    result = 0

    for i in range(1, N-1) :
        if (case[i] != min(case[i-1], case[i], case[i+1])) and (case[i] != max(case[i-1], case[i], case[i+1])) :
            result += 1

    print(f'#{t+1} {result}')