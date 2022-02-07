for t in range(int(input())) :
    n = sum(map(int, input().split()))
    if n>=24 : print(f'#{t+1} {n-24}')
    else : print(f'#{t+1} {n}')