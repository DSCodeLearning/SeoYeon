for t in range(int(input())) :
    n = int(input())
    case = sorted(list(map(int, input().split())))
    print(f'#{t+1}', end=' ')
    for i in case : print(i, end=' ')
    print()
